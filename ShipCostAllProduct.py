import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Lasso
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from sklearn.linear_model import Ridge
from sklearn import decomposition
from sklearn.decomposition import PCA


Data=pd.read_csv('NumericData.csv',usecols=['ProdID','Sales','Profit','Quantity','RegionID','ShippingCost','SubCategoryID','CategoryID','OrderPriorityID','ShipModeID'])

df=Data[Data.ProdID==4640]
#2.50422536013  2.50454490188
# X=df[['Sales','Quantity','OrderPriorityID','ShipModeID','MarketID','DateDif','Profit','CountryID']]
# y=df['ShippingCost']
X=df[['Sales','Profit','SubCategoryID','CategoryID','OrderPriorityID','ShipModeID','Quantity','RegionID']]
y=df['ShippingCost']

pca=decomposition.PCA()
Data_pca=pca.fit_transform(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.sum())


print("Score Of KFOLD: ")
linreg = linear_model.LinearRegression()
scores = cross_val_score(linreg, X, y, cv=5, scoring='neg_mean_squared_error')

mse = -scores

rmse = np.sqrt(mse)
print('RMSE',rmse.mean())

poly = PolynomialFeatures(degree=1)
X_ = poly.fit_transform(X)
linreg = linear_model.LinearRegression()
scores = cross_val_score(linreg, X_, y, cv=3, scoring='neg_mean_squared_error')

mse = -scores

rmse = np.sqrt(mse)
print('RMSE',rmse.mean())

# sns.pairplot(df, x_vars=['Profit','Quantity','Discount'], y_vars='Sales', size=6, aspect=0.7, kind='reg')
# plt.show()
#
# clf = linear_model.Lasso(alpha=.1)
# scores = cross_val_score(clf, X, y, cv=10, scoring='neg_mean_squared_error')
#
# mse = -scores
# print(mse)
#
# rmse = np.sqrt(mse)
# print('RMSE Values',rmse)
# print('RMSE',rmse.mean())
#
# clf = Ridge(alpha=.1)
# scores = cross_val_score(clf, X, y, cv=10, scoring='neg_mean_squared_error')
#
# mse = -scores
# print(mse)
#
# rmse = np.sqrt(mse)
# print('RMSE Values',rmse)
# print('RMSE',rmse.mean())
