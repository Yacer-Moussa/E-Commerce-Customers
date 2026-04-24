
import seaborn as sns

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

from src.data_loader import load_data
from src.evaluate import evaluate_model
from src.train import train_model
from src.visualisation import plot_all

sns.set_style("whitegrid")
sns.set_palette("coolwarm")

ecom =load_data("data/ecommerce-customers.csv")

ecom.head()
ecom.info()
ecom.describe().round(1)

plot_all(ecom)

X,y,X_train,X_test,y_train,y_test,lm=train_model(ecom)

lm.coef_

y_pred, mae, mse, rmse, coeff=evaluate_model(lm,X_test,y_test,X.columns)


print(y_pred)
print(mae)
print(mse)
print(rmse)
print(coeff)    

