from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
import joblib
import numpy as np

from preprocessing import get_data_for_training

X_train_os, y_train_os, X_test, y_test = get_data_for_training()

# kfold
folds = StratifiedKFold(n_splits=5, random_state=137, shuffle=True)

# processing and clasification model
steps = [('procesamiento', StandardScaler(with_mean=False)),
         ('clasificador', XGBClassifier(n_jobs=-1, use_label_encoder=False, random_state=137))]

# grid search 
pipe = Pipeline(steps)
param_grid =  {
        "clasificador__n_estimators" : [50, 100, 150],
        "clasificador__learning_rate" : [0.05, 0.1, 0.2],
        "clasificador__max_depth" : [3, 4, 6],
    }

# tuning hiperparameters
pipe_grid = GridSearchCV(pipe, param_grid, cv=folds)
pipe_grid.fit(X_train_os, y_train_os)

# best model
xgb_classifier = pipe_grid.best_estimator_

y_pred = pipe_grid.best_estimator_.predict(X_test)
y_pred_proba = pipe_grid.best_estimator_.predict_proba(X_test)


# performance metrics
print('AUC Score: ' + str(np.round(roc_auc_score(y_test, y_pred_proba[:,1]),4)))
print('Accuracy Score: ' + str(accuracy_score(y_test, y_pred)))

# save model
filename = '/Users/esperanza.orozco/LauraOrozco/r5-ds-challenge/models/xgb_model.sav'
joblib.dump(xgb_classifier, filename)