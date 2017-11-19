import pandas as pd
import numpy as np
import scipy
from scipy.stats.stats import pearsonr
from scipy.stats import spearmanr

Data=pd.read_csv('NumericData.csv',usecols=['ProdID','Sales','Quantity','Discount','Profit','ShippingCost','CityID','RegionID',
                                        'SubCategoryID','CategoryID','DateDif','OrderPriorityID','ShipModeID','MarketID','StateID','CountryID'])


X=Data[['ProdID','Sales','Quantity','Discount','Profit','ShippingCost','CityID','RegionID',
                                        'SubCategoryID','CategoryID','DateDif','MarketID','StateID','CountryID']]
#
y=Data['ShipModeID']
Pr=X.corr()
print(Pr)


ss=spearmanr(Data['ShippingCost'].values,Data['OrderPriorityID'].values)
print(ss)

table=pd.crosstab(y,Data['Sales'])
from  scipy.stats import chi2_contingency
chi2,p,dof,expected=chi2_contingency(table.values)
print(p)
table=pd.crosstab(y,Data['Quantity'])
chi2,p,dof,expected=chi2_contingency(table.values)
print(p)
# table=pd.crosstab(y,Data['ShipModeID'])
# chi2,p,dof,expected=chi2_contingency(table.values)
# print(p)
table=pd.crosstab(y,Data['MarketID'])
chi2,p,dof,expected=chi2_contingency(table.values)
print(p)
table=pd.crosstab(y,Data['DateDif'])
chi2,p,dof,expected=chi2_contingency(table.values)
print(p)
table=pd.crosstab(y,Data['Sales'])
from  scipy.stats import chi2_contingency
chi2,p,dof,expected=chi2_contingency(table.values)
print(p)
table=pd.crosstab(y,Data['Quantity'])
chi2,p,dof,expected=chi2_contingency(table.values)
print(p)
# table=pd.crosstab(y,Data['ShipModeID'])
# chi2,p,dof,expected=chi2_contingency(table.values)
# print(p)
table=pd.crosstab(y,Data['MarketID'])
chi2,p,dof,expected=chi2_contingency(table.values)
print(p)
table=pd.crosstab(y,Data['DateDif'])
chi2,p,dof,expected=chi2_contingency(table.values)
print(p)
