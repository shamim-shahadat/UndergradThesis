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
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

Data=pd.read_csv('FactTab.csv',usecols=['ProdID','Sales','Quantity','Discount','Profit'])

ProductInfo=pd.read_csv('dimNewProduct.csv',encoding='latin-1')
Data=pd.merge(Data,ProductInfo,how='left',left_on='ProdID',right_on='ProdID')

Data.ProdID=Data.ProdID.str.replace('P','0')
Data.ProdID=pd.to_numeric(Data.ProdID,errors='coerce').fillna(0).astype(np.int64)


X=Data[['ProdID','SellingPricePerUnit','PurchasingPricePerUnit','Sales','Quantity','Discount']]
y=Data['Profit']

print("Score Of KFOLD: ")
linreg = linear_model.LinearRegression()
scores = cross_val_score(linreg, X, y, cv=10, scoring='neg_mean_squared_error')

mse= -scores

rmse = np.sqrt(mse)
print('RMSE Values',rmse)
print('RMSE :', rmse.mean())

print("Score Of test split: ")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)
print('Y intercept',linreg.intercept_)
print('X intercepts',linreg.coef_)
print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))



print('Polynomial')
poly = PolynomialFeatures(degree=3)
X_ = poly.fit_transform(X)
#predict_ = poly.fit_transform(y)
linreg = linear_model.LinearRegression()
scores = cross_val_score(linreg, X_, y, cv=10, scoring='neg_mean_squared_error')

mse = -scores

rmse = np.sqrt(mse)
print('RMSE Values:',rmse)

print ('RMSE :', rmse.mean())
