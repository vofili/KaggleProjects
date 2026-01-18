import pandas as pd
from sklearn.tree import DecisionTreeRegressor
src_data = "../datasets/melb_data.csv"
mel_hsedata = pd.read_csv(src_data)
mel_hsedata.describe()

print(mel_hsedata.columns)

mel_hsedata.dropna(axis=0)
y = mel_hsedata.Price
#print(y)

mel_features = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude']
X = mel_hsedata[mel_features]
#print(X)
print(X.describe())
print(X.head())
