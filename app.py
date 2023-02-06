# 1. Library imports
import pandas as pd
import uvicorn
import joblib
from fastapi import FastAPI
from preprocessing import get_data_for_training

X_train_os, y_train_os, X_test, y_test = get_data_for_training()

# 2. Create app and model objects
app = FastAPI(  
    title="Fraud Classification",
    description='Clasification model that predict is a claim is fraud or not',
    version="0.1",
    contact={
        "name": "Laura Orozco",
        "email": "laura.orozco.ceron@gmail.com",
    },
)
model = joblib.load('/Users/esperanza.orozco/LauraOrozco/r5-ds-challenge/models/xgb_model.sav')

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predict")
def predict(record: dict): 
    record_df = pd.DataFrame.from_dict([record])
    record_df.columns = record_df.columns.str.lower()

    record_dummies = pd.get_dummies(record_df, columns=['monthh', 'weekofmonth', 'dayofweek', 'make', 'accidentarea', 'dayofweekclaimed', 'monthclaimed',
                                    'weekofmonthclaimed', 'sex', 'maritalstatus', 'fault', 'vehiclecategory', 'vehicleprice',
                                    'driverrating', 'days_policy_accident', 'days_policy_claim', 'pastnumberofclaims', 'ageofvehicle',
                                    'ageofpolicyholder', 'policereportfiled', 'witnesspresent', 'agenttype', 'numberofsuppliments',
                                    'addresschange_claim', 'numberofcars', 'basepolicy', 'policytype'])

    record_dummies.drop(['policynumber', 'repnumber', 'yearr'], axis=1, inplace=True)

    test_case = pd.DataFrame(columns=X_test.columns)
    test_final = pd.concat([test_case, record_dummies],axis=0)

    dummified_record_df = test_final.values.reshape(1, -1)

    predict_class = model.predict(dummified_record_df)

    predict_poroba = model.predict_proba(dummified_record_df)

    return {"class": int(predict_class[0]),
            "prob": float(predict_poroba[:, 1])}




# 4. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    