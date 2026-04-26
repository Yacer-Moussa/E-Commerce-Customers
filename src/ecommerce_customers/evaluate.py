import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error

def evaluate_model(lm, X_test, y_test,X_columns):
    y_pred=lm.predict(X_test)

    mae=mean_absolute_error(y_test,y_pred)
    mse=mean_squared_error(y_test,y_pred)
    rmse=np.sqrt(mse)

    coeff=pd.DataFrame(lm.coef_,X_columns)
    coeff.columns=['Coefficient']

    return y_pred, mae, mse, rmse, coeff