import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

#import Data
hse_data_file = "../datasets/melb_data.csv"
#create dataframe and examine data
hse_data = pd.read_csv((hse_data_file))
print(hse_data.describe())

print(hse_data.head())
#define features
feature_list=['Rooms','Distance','Bedroom2','Bathroom','Car','Landsize','YearBuilt','BuildingArea']
#define target
y = hse_data.Price
X = hse_data[feature_list]
hse_price_model = DecisionTreeRegressor(random_state=1)
hse_price_model.fit(X,y)
print("Predict price information for these houses:")
print(X.head())
print("Price Information:")
print(hse_price_model.predict(X.head()))