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
#print(X.describe())
#print(X.head())
mel_model = DecisionTreeRegressor(random_state=1)
mel_model.fit(X,y)
print("Making predictions for House prices:")
print(X.head())
print("House Price predictions are:")
print(mel_model.predict(X.head()))
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y,mel_model.predict(X))
print(mae)

from sklearn.model_selection import train_test_split
train_X,val_X,train_y,val_y = train_test_split(X,y,random_state=1)
#view validation data
print("Valiation Data Summary")
print(val_y.head())
#define model
mel_model2= DecisionTreeRegressor(random_state=1)
#fit model to train data
mel_model2.fit(train_X,train_y)
#predict data
predict_2 = mel_model2.predict(val_X)
#get mean absolute error
mae2 = mean_absolute_error(val_y,predict_2)
print(mae2)