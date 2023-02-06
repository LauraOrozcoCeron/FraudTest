
import pandas as pd
import numpy as np
import configparser
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler


def get_data_for_training():
    
    config = configparser.ConfigParser()
    config.read_file(open('/Users/esperanza.orozco/LauraOrozco/r5-ds-challenge/config.ini'))
    host = config['dbcredentials']['db_host']
    user = config['dbcredentials']['username']
    passwd = config['dbcredentials']['password']
    db = config['dbcredentials']['db_name']

    engine = create_engine(f'postgresql+psycopg2://{user}:{passwd}@{host}/{db}')
    with engine.connect() as con:
    
        query = """SELECT DISTINCT monthh,
                weekofmonth, 
                dayofweek, 
                AVG(FraudFound_P)  OVER (PARTITION BY monthh) AS percentage_fraud_month,
                AVG(FraudFound_P)  OVER (PARTITION BY monthh, weekofmonth) AS percentage_fraud_month_week, 
                AVG(FraudFound_P)  OVER (PARTITION BY monthh, weekofmonth, dayofweek) AS percentage_fraud_month_week_day
            FROM fraudes"""

        statement = text(query)

        query_result = con.execute(statement)

        data_percentage = query_result.all()


    with engine.connect() as con:
    
        query = """SELECT * FROM fraudes"""

        statement = text(query)

        query_result = con.execute(statement)

        data_fraud = query_result.all()

    fraud_percentage = pd.DataFrame(data_percentage)
    fraud = pd.DataFrame(data_fraud)

    fraud_final = fraud.merge(fraud_percentage, how='left', on=['monthh', 'weekofmonth', 'dayofweek'])

    categorical = ['monthh', 'dayofweek', 'make', 'accidentarea', 'dayofweekclaimed', 'monthclaimed', 'sex', 
               'maritalstatus', 'fault', 'policytype', 'vehiclecategory', 'fraudfound_p', 'driverrating',
              'policereportfiled','witnesspresent', 'agenttype', 'basepolicy', 'policereportfiled', 'numberofsuppliments',
              'numberofcars', 'addresschange_claim', 'vehicleprice', 'days_policy_accident', 'days_policy_claim',
              'pastnumberofclaims', 'ageofvehicle', 'ageofpolicyholder']

    numerical = ['weekofmonth', 'age', 'policynumber', 'repnumber', 'deductible', 'yearr', 'percentage_fraud_month',
            'percentage_fraud_month_week', 'percentage_fraud_month_week_day']

    for col in categorical:
        fraud_final[col] = fraud_final[col].astype('category')

    fraud_final[numerical] = fraud_final[numerical].apply(pd.to_numeric)

    fraud_final.drop(['policynumber', 'repnumber', 'yearr'], axis=1, inplace=True)

    fraud_dummies = pd.get_dummies(fraud_final, columns=['monthh', 'weekofmonth', 'dayofweek', 'make', 'accidentarea', 'dayofweekclaimed', 'monthclaimed',
                                 'weekofmonthclaimed', 'sex', 'maritalstatus', 'fault', 'vehiclecategory', 'vehicleprice',
                                 'driverrating', 'days_policy_accident', 'days_policy_claim', 'pastnumberofclaims', 'ageofvehicle',
                                 'ageofpolicyholder', 'policereportfiled', 'witnesspresent', 'agenttype', 'numberofsuppliments',
                                 'addresschange_claim', 'numberofcars', 'basepolicy', 'policytype']
)


    X = fraud_dummies.drop(columns=['fraudfound_p'])
    y = fraud_dummies['fraudfound_p']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=137, stratify=y)

    oversampler = RandomOverSampler(sampling_strategy='minority', random_state=137)
    X_train_os, y_train_os = oversampler.fit_resample(X_train, y_train)


    return X_train_os, y_train_os, X_test, y_test
