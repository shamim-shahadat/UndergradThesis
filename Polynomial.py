import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso
from sklearn import linear_model

from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model

Data=pd.read_csv('FactTab.csv',usecols=['ProdID','Sales','Quantity','Discount','Profit'])

# df=Data.groupby(['ProdID']).ProdID.agg(['count'])
# print(df['count'].sort_values())
Data.ProdID=Data.ProdID.str.replace('P','0')



Data.ProdID=pd.to_numeric(Data.ProdID,errors='coerce').fillna(0).astype(np.int64)
#print(Data)
# Data.ProdID.astype(np.int64)
print(Data.ProdID.dtype)

df=Data[Data.ProdID==4640]
# print(df)

X=df[['Profit','Quantity','Discount']]
y=df['Sales']

poly = PolynomialFeatures(degree=1)
X_ = poly.fit_transform(X)
#predict_ = poly.fit_transform(y)
linreg = linear_model.LinearRegression()
scores = cross_val_score(linreg, X_, y, cv=10, scoring='neg_mean_squared_error')

mse_scores = -scores
print(mse_scores)

rmse_scores = np.sqrt(mse_scores)
print(rmse_scores)

print(rmse_scores.mean())

X=df[['Sales','Quantity','Discount']]
y=df['Profit']

poly = PolynomialFeatures(degree=1)
X_ = poly.fit_transform(X)
#predict_ = poly.fit_transform(y)
linreg = linear_model.LinearRegression()
scores = cross_val_score(linreg, X_, y, cv=10, scoring='neg_mean_squared_error')

mse_scores = -scores
print(mse_scores)

rmse_scores = np.sqrt(mse_scores)
print(rmse_scores)

print(rmse_scores.mean())