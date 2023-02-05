import joblib
from preprocessing import get_data_for_training

X_train_os, y_train_os, X_test, y_test = get_data_for_training()
xgb_from_joblib = joblib.load('/Users/esperanza.orozco/LauraOrozco/r5-ds-challenge/models/xgb_model.sav')

new_case = X_test.iloc[1066]
new_case_values = new_case.values.reshape(1, -1) 

y_pred = xgb_from_joblib.predict(new_case_values)
y_pred_proba = xgb_from_joblib.predict_proba(new_case_values)

print('Los datos del caso particular son: ' + str(new_case))
print('la clase predicha es: ' + str(y_pred))
print('La probabilidad predicha de ocurrencia para este individuo es: ' + str(y_pred_proba[:, 1]))