import pandas as pd
import numpy as np

Data=pd.read_csv('FactTab.csv',usecols=['RowID','ProdID','OrderDateID','ShipDateID','Sales','Quantity','Discount','Profit','ShippingCost','CityID','RegionID',
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

Data=pd.merge(Data,MergeData,how='left',left_on='CityID',right_on='CityID')

Data=Data.drop(['City','State','Country'],axis=1)
getRegion=pd.read_csv('dimRegion.csv')
getMarket=pd.read_csv('dimMarket.csv')

getRegion=pd.merge(getRegion,getMarket,how='left',left_on='MarketID',right_on='MarketID')

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
Data.CountryID=Data.CountryID.str.replace('CO','0')
Data.CountryID=pd.to_numeric(Data.CountryID,errors='coerce').fillna(0).astype(np.int64)

Data.DateDif=Data.DateDif.str.replace(' days 00:00:00.000000000','')
Data.DateDif=pd.to_numeric(Data.DateDif,errors='coerce').fillna(0).astype(np.int64)

getSubCat=pd.read_csv('dimSubCategory.csv')
getCat=pd.read_csv('dimCategory.csv')
Data=pd.merge(Data,getSubCat,how='left',left_on='SubCategoryID',right_on='SubCategoryID')
Data=pd.merge(Data,getCat,how='left',left_on='CategoryID',right_on='CategoryID')

Data.CategoryID=Data.CategoryID.str.replace('CA','0')
Data.CategoryID=pd.to_numeric(Data.CategoryID,errors='coerce').fillna(0).astype(np.int64)

Data.SubCategoryID=Data.SubCategoryID.str.replace('SC','0')
Data.SubCategoryID=pd.to_numeric(Data.SubCategoryID,errors='coerce').fillna(0).astype(np.int64)
Data=Data.drop(['ShipDate','OrderDate','SubCategory','Category','ProductName','ProductID'],axis=1)

print(Data.shape)
print(Data.head())
Data.set_index('RowID',inplace=True)
Data.to_csv('NumericData.csv')
