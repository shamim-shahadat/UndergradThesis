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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFECV


Data=pd.read_csv('NumericData.csv',usecols=['ProdID','Sales','Quantity','Discount','Profit','ShippingCost','CityID','RegionID',
                                        'SubCategoryID','CategoryID','SellingPricePerUnit','PurchasingPricePerUnit','DateDif','OrderPriorityID','ShipModeID','MarketID','StateID','CountryID'])


X=Data[['ProdID','Sales','Quantity','Discount','Profit','ShippingCost','CityID','RegionID',
                                        'SubCategoryID','CategoryID','SellingPricePerUnit','PurchasingPricePerUnit','DateDif','ShipModeID','MarketID','StateID','CountryID']]

#[13  7  2  1 11  6 12  4  5  3  1  1  8 10  9]
# df=Data[Data.ProdID==4640]
# X=df[['Sales','Quantity','OrderPriorityID','ShipModeID','MarketID','DateDif','Profit','CountryID']]
# y=df['ShippingCost']
#['Sales','Quantity','ShipModeID','ShippingCost','DateDif','MarketID']
#X=Data[['ProdID','Sales','Quantity','Discount','Profit','ShippingCost','CityID','RegionID','ShipModeID']]

#62%
#X=Data[['ShipModeID','ShippingCost','DateDif','MarketID','Sales']]
#62.7%
X=Data[['Discount','DateDif','CategoryID']]

y=Data['OrderPriorityID']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)
#
# #check classification accuracy of KNN with K=5
# knn = KNeighborsClassifier(n_neighbors=7)
# knn.fit(X_train, y_train)
# y_pred = knn.predict(X_test)
# print(metrics.accuracy_score(y_test, y_pred))

# k_range = list(range(1,100))
# k_scores = []
# for k in k_range:
#     knn = KNeighborsClassifier(n_neighbors=k)
#     scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
#     k_scores.append(scores.mean())
# print(k_scores)


# knn = KNeighborsClassifier(n_neighbors=20)
# scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
# print(scores.mean())

logreg = LogisticRegression()
# scores = cross_val_score(logreg, X, y, cv=10, scoring='accuracy')
# print(scores.mean())

# clf = DecisionTreeClassifier()
# scores = cross_val_score(clf, X, y, cv=10, scoring='accuracy')
# print(scores.mean())

# m=RFECV(RandomForestClassifier(),scoring='accuracy')
# m.fit(X_train,y_train)
# print(m.score(X_test,y_test))

from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold

rfecv = RFECV(estimator=logreg, step=1, cv=StratifiedKFold(2),
              scoring='accuracy')
rfecv.fit(X, y)

#print("Optimal number of features : %d" % rfecv.ranking_)
print(rfecv.ranking_)