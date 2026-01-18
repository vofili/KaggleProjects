import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

#import Data
hse_data_file = "../datasets/melb_data.csv"

hse_data = pd.read_csv(hse_data_file)
#explore initial values in dataset
print(hse_data.head())
#explore columns(features) in the dataset
print(hse_data.columns)

# features = ['Su']
# hse_model = DecisionTreeRegressor(random_state=1)
#
# hse_model.fit(X,y)