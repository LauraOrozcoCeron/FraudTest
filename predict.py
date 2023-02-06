import joblib
import pandas as pd
from preprocessing import get_data_for_training

X_train_os, y_train_os, X_test, y_test = get_data_for_training()
xgb_from_joblib = joblib.load('/Users/esperanza.orozco/LauraOrozco/r5-ds-challenge/models/xgb_model.sav')


# New case
record = {
    "Monthh": "Dec",
    "WeekOfMonth": 5,
    "DayOfWeek": "Wednesday",
    "Make": "Honda",
    "AccidentArea": "Urban",
    "DayOfWeekClaimed": "Tuesday",
    "MonthClaimed": "Jan",
    "WeekOfMonthClaimed": 1,
    "Sex": "Female",
    "MaritalStatus": "Single",
    "Age": 21,
    "Fault": "Policy Holder",
    "PolicyType": "Sport - Liability",
    "VehicleCategory": "Sport",
    "VehiclePrice": "more than 69000",
    "FraudFound_P": 0,
    "PolicyNumber": 1,
    "RepNumber": 12,
    "Deductible": 300,
    "DriverRating": 1,
    "Days_Policy_Accident": "more than 30",
    "Days_Policy_Claim": "more than 30",
    "PastNumberOfClaims": "none",
    "AgeOfVehicle": "3 years",
    "AgeOfPolicyHolder": "26 to 30",
    "PoliceReportFiled": "No",
    "WitnessPresent": "No",
    "AgentType": "External",
    "NumberOfSuppliments": "none",
    "AddressChange_Claim": "1 year",
    "NumberOfCars": "3 to 4",
    "Yearr": 1994,
    "BasePolicy": "Liability"
}

record_df = pd.DataFrame.from_dict([record])
record_df.columns = record_df.columns.str.lower()

record_dummies = pd.get_dummies(record_df, columns=['monthh', 'weekofmonth', 'dayofweek', 'make', 'accidentarea', 'dayofweekclaimed', 'monthclaimed',
                                 'weekofmonthclaimed', 'sex', 'maritalstatus', 'fault', 'vehiclecategory', 'vehicleprice',
                                 'driverrating', 'days_policy_accident', 'days_policy_claim', 'pastnumberofclaims', 'ageofvehicle',
                                 'ageofpolicyholder', 'policereportfiled', 'witnesspresent', 'agenttype', 'numberofsuppliments',
                                 'addresschange_claim', 'numberofcars', 'basepolicy', 'policytype'])


record_dummies.drop(['policynumber', 'repnumber', 'yearr', 'fraudfound_p'], axis=1, inplace=True)

test_case = pd.DataFrame(columns=X_test.columns)
test_final = pd.concat([test_case, record_dummies],axis=0)

dummified_record_df = test_final.values.reshape(1, -1)

y_pred = xgb_from_joblib.predict(dummified_record_df)
y_pred_proba = xgb_from_joblib.predict_proba(dummified_record_df)

print('Los datos del caso particular son: ' + str(record_df))
print('la clase predicha es: ' + str(y_pred))
print('La probabilidad predicha de ocurrencia para este individuo es: ' + str(y_pred_proba[:, 1]))