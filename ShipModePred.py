from sklearn.model_selection import cross_val_score
from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import scipy
from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

Data=pd.read_csv('NumericData.csv',usecols=['ProdID','Sales','Quantity','Discount','Profit','ShippingCost','CityID','RegionID',
                                        'SubCategoryID','CategoryID','SellingPricePerUnit','PurchasingPricePerUnit','DateDif','OrderPriorityID','ShipModeID','MarketID','StateID','CountryID'])

#[16 13  4  3 15  2 17  7  8  5 12 10 11  1  6 14  9]
X=Data[['ProdID','Sales','Quantity','Discount','Profit','OrderPriorityID','CityID','RegionID',
                                        'SubCategoryID','CategoryID','SellingPricePerUnit','ShippingCost','PurchasingPricePerUnit','DateDif','MarketID','StateID','CountryID']]
X=Data[['DateDif']]
y=Data['ShipModeID']

logreg = LogisticRegression()
scores = cross_val_score(logreg, X, y, cv=10, scoring='accuracy')
print(scores.mean())

k_range = list(range(1,60))
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())
print(k_scores)

plt.plot(k_range,k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()