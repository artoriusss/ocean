import pandas as pd

def feature_engineering(df):
    X = df[['navDesc', 'courseOverGround', 'speedOverGround', 'typeName']]
    y = df['lead_time']

    X = pd.get_dummies(X, columns=['navDesc', 'typeName'])
    return X, y