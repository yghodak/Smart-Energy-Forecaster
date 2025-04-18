import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def prepare_features(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.day
    df['weekday'] = df['timestamp'].dt.weekday
    df['month'] = df['timestamp'].dt.month
    return df

def train_forecaster(df):
    df = prepare_features(df)
    X = df[['hour', 'day', 'weekday', 'month']]
    y = df['energy_kWh']
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

def predict_future_usage(model, periods=24):
    future = pd.date_range(start=pd.Timestamp.now(), periods=periods, freq='H')
    df_future = pd.DataFrame({'timestamp': future})
    df_future = prepare_features(df_future)
    X_future = df_future[['hour', 'day', 'weekday', 'month']]
    df_future['predicted_energy_kWh'] = model.predict(X_future)
    return df_future
