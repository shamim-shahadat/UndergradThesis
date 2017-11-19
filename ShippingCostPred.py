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
from sklearn import svm


Data=pd.read_csv('FactTab.csv',usecols=['ProdID','OrderDateID','ShipDateID','Sales','Quantity','Discount','Profit','ShippingCost','CityID','RegionID',
                                        'OrderPriorityID','ShipModeID'])

# df=Data.groupby(['ProdID']).ProdID.agg(['count'])
# print(df['count'].sort_values())
getProduct=pd.read_csv("dimNewProduct.csv",encoding='latin-1')
Data=pd.merge(Data,getProduct,how='left',left_on='ProdID',right_on='ProdID')

Data.ProdID=Data.ProdID.str.replace('P','0')
Data.ProdID=pd.to_numeric(Data.ProdID,errors='coerce').fillna(0).astype(np.int64)

Data.OrderPriorityID=Data.OrderPriorityID.str.replace('OP','0')
Data.OrderPriorityID=pd.to_numeric(Data.OrderPriorityID,errors='coerce').fillna(0).astype(np.int64)

Data.ShipModeID=Data.ShipModeID.str.replace('SM','0')
Data.ShipModeID=pd.to_numeric(Data.ShipModeID,errors='coerce').fillna(0).astype(np.int64)

getCity=pd.read_csv('dimCity.csv',encoding='latin-1')
getState=pd.read_csv('dimState.csv',encoding='latin-1')
getCountry=pd.read_csv('dimCountry.csv')
MergeData=pd.merge(getCity,getState,how='left',left_on='StateID',right_on='StateID')
MergeData=pd.merge(MergeData,getCountry,how='left',left_on='CountryID',right_on='CountryID')
print(Data.shape)
Data=pd.merge(Data,MergeData,how='left',left_on='CityID',right_on='CityID')
print(Data.shape)
Data=Data.drop(['City','State','Country'],axis=1)
getRegion=pd.read_csv('dimRegion.csv')
getMarket=pd.read_csv('dimMarket.csv')
print(getRegion.shape)
getRegion=pd.merge(getRegion,getMarket,how='left',left_on='MarketID',right_on='MarketID')
print(getRegion.shape)
getRegion=getRegion.drop(['Region','Market'],axis=1)
Data=pd.merge(Data,getRegion,how='left',left_on='RegionID',right_on='RegionID')

Data.MarketID=Data.MarketID.str.replace('MA','0')
Data.MarketID=pd.to_numeric(Data.MarketID,errors='coerce').fillna(0).astype(np.int64)

Data.CityID=Data.CityID.str.replace('CI','0')
Data.CityID=pd.to_numeric(Data.CityID,errors='coerce').fillna(0).astype(np.int64)

Data.RegionID=Data.RegionID.str.replace('RE','0')
Data.RegionID=pd.to_numeric(Data.RegionID,errors='coerce').fillna(0).astype(np.int64)

Data.StateID=Data.StateID.str.replace('ST','0')
Data.StateID=pd.to_numeric(Data.StateID,errors='coerce').fillna(0).astype(np.int64)

getShipdate=pd.read_csv('dimShipDate.csv',usecols=['ShipDateID','ShipDate'])
getOrderdate=pd.read_csv('dimOrderDate.csv',usecols=['OrderDateID','OrderDate'])
getShipdate.ShipDate=pd.to_datetime(getShipdate.ShipDate)
getOrderdate.OrderDate=pd.to_datetime(getOrderdate.OrderDate)

Data=pd.merge(Data,getShipdate,how='left',left_on='ShipDateID',right_on='ShipDateID')
Data=pd.merge(Data,getOrderdate,how='left',left_on='OrderDateID',right_on='OrderDateID')

diff=Data.ShipDate-Data.OrderDate

Data['DateDif']=diff
Data.DateDif=Data.DateDif.astype(str)
print(Data.dtypes)
Data.CountryID=Data.CountryID.str.replace('CO','0')
Data.CountryID=pd.to_numeric(Data.CountryID,errors='coerce').fillna(0).astype(np.int64)

Data.DateDif=Data.DateDif.str.replace(' days 00:00:00.000000000','')
Data.DateDif=pd.to_numeric(Data.DateDif,errors='coerce').fillna(0).astype(np.int64)
print(Data.head())
df=Data[Data.ProdID==4640]
#2.50422536013  2.50454490188
# X=df[['Sales','Quantity','OrderPriorityID','ShipModeID','MarketID','DateDif','Profit','CountryID']]
# y=df['ShippingCost']
X=df[['Sales','Quantity','OrderPriorityID','ShipModeID','RegionID']]
y=df['ShippingCost']
# poly = PolynomialFeatures(degree=2)
# X_ = poly.fit_transform(X)
pca=decomposition.PCA()
Data_pca=pca.fit_transform(X)
print(pca.explained_variance_ratio_)
print(pca.explained_variance_ratio_.sum())


print("Score Of KFOLD: ")
linreg = linear_model.LinearRegression()
scores = cross_val_score(linreg, X, y, cv=10, scoring='neg_mean_squared_error')

mse = -scores

rmse = np.sqrt(mse)

print('Linear RMSE',rmse.mean())

# sns.pairplot(df, x_vars=['Profit','Quantity','Discount'], y_vars='Sales', size=6, aspect=0.7, kind='reg')
# plt.show()

clf = linear_model.Lasso(alpha=.1)
scores = cross_val_score(clf, X, y, cv=10, scoring='neg_mean_squared_error')

mse = -scores

rmse = np.sqrt(mse)
print('Lasso RMSE',rmse.mean())

clf = Ridge(alpha=.1)
scores = cross_val_score(clf, X, y, cv=10, scoring='neg_mean_squared_error')

mse = -scores
rmse = np.sqrt(mse)
print('Ridge RMSE',rmse.mean())

clf = svm.SVR()
scores = cross_val_score(clf, X, y, cv=10, scoring='neg_mean_squared_error')

mse = -scores
rmse = np.sqrt(mse)

print('SVM RMSE',rmse.mean())

print("Score Of test split: ")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)
print('Y intercepsts:',linreg.intercept_)
print('X coefficients:',linreg.coef_)
print('Accuracy',linreg.score(X_test,y_test))
