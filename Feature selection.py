from sklearn.feature_selection import RFECV
from sklearn.model_selection import StratifiedKFold
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import scipy
from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr
from sklearn.linear_model import LogisticRegression

Data=pd.read_csv('NumericData.csv',usecols=['ProdID','Sales','Quantity','Discount','Profit','ShippingCost','CityID','RegionID',
                                        'SubCategoryID','CategoryID','SellingPricePerUnit','PurchasingPricePerUnit','DateDif','OrderPriorityID','ShipModeID','MarketID','StateID','CountryID'])


X=Data[['ProdID','Sales','Quantity','Discount','Profit','OrderPriorityID','CityID','RegionID',
                                        'SubCategoryID','CategoryID','SellingPricePerUnit','ShippingCost','PurchasingPricePerUnit','DateDif','MarketID','StateID','CountryID']]
y=Data['ShipModeID']
logreg=LogisticRegression()
rfecv = RFECV(estimator=logreg, step=1, cv=2,
              scoring='accuracy')
rfecv.fit(X, y)

print(rfecv.n_features_)
print(rfecv.ranking_)