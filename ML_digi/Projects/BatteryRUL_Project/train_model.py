
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
from sklearn.metrics import mean_squared_error
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--data', default='data/battery_data.csv')
parser.add_argument('--out', default='model/rul_model_rf.joblib')
args = parser.parse_args()

df = pd.read_csv(args.data)
X = df[['voltage','current','temperature','cycle']]
y = df['RUL']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

preds = model.predict(X_test)
mse = mean_squared_error(y_test, preds)
print(f'RMSE: {mse**0.5:.3f}')

joblib.dump(model, args.out)
print('Model saved to', args.out)
