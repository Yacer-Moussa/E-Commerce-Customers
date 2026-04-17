import pandas as pd

def load_data(path="data/ecommerce-customers.csv"):
    ecom=pd.read_csv(path)
    return ecom 