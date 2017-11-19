import pandas as pd

FactTable=pd.read_excel('DB.xls',encoding='latin-1')
FactTable.rename(columns={'Order ID':'OrderID','Order Date':'OrderDate','Ship Date':'ShipDate','Ship Mode':'ShipMode',
                           'Customer ID': 'CustomerID','Product ID':'ProductID','Sub-Category':'SubCategory','Shipping Cost':'ShippingCost',
                           'Order Priority': 'OrderPriority','Customer Name': 'CustomerName','Row ID':'RowID','Product Name':'ProductName'},inplace=True)

OrderPrio=pd.read_csv('dimOrderPriority.csv')
MergeData = pd.merge(FactTable, OrderPrio, how='left', on=['OrderPriority'])
MergeData=MergeData.drop('OrderPriority',axis=1)

ShipMode=pd.read_csv('dimShipMode.csv')
MergeData = pd.merge(MergeData, ShipMode, how='left', on=['ShipMode'])
MergeData=MergeData.drop(['ShipMode','Postal Code'],axis=1)


GetOrderDate=pd.read_csv('dimOrderDate.csv')
MergeData.OrderDate=pd.to_datetime(MergeData.OrderDate)
GetOrderDate.OrderDate=pd.to_datetime(GetOrderDate.OrderDate)
MergeData.ShipDate=pd.to_datetime(MergeData.ShipDate)
MergeData = pd.merge(MergeData, GetOrderDate, how='left', on=['OrderDate'])
MergeData=MergeData.drop(['OrderDate','Year','Month','Quarter'],axis=1)

GetShipDate=pd.read_csv('dimShipDate.csv')
GetShipDate.ShipDate=pd.to_datetime(GetShipDate.ShipDate)
MergeData.ShipDate=pd.to_datetime(MergeData.ShipDate)
MergeData = pd.merge(MergeData,GetShipDate, how='left', on=['ShipDate'])
MergeData=MergeData.drop(['ShipDate','Year','Month','Quarter'],axis=1)
print(MergeData.shape)

GetCity=pd.read_csv('dimCity.csv',encoding='latin-1')
GetState=pd.read_csv('dimState.csv',encoding='latin-1')
merg=pd.merge(GetCity,GetState,how='left',left_on='StateID',right_on='StateID')
GetContry=pd.read_csv('dimCountry.csv')
merg=pd.merge(merg,GetContry,how='left',left_on='CountryID',right_on='CountryID')
MergeData = pd.merge(MergeData, merg, how='left',left_on=['City','State','Country'],right_on=['City','State','Country'])
print(MergeData.shape)
MergeData=MergeData.drop(['City','StateID','CustomerName','Segment','State','Country','StateID','CountryID'],axis=1)


GetRegion=pd.read_csv('dimRegion.csv')
GetMarket=pd.read_csv('dimMarket.csv')
Merg=pd.merge(GetRegion,GetMarket,how='left',left_on='MarketID',right_on='MarketID')
MergeData = pd.merge(MergeData,Merg, how='left',left_on=['Region','Market'],right_on=['Region','Market'])
MergeData=MergeData.drop(['Region','Market','MarketID'],axis=1)
print(MergeData.shape)

MergeData=MergeData.drop(['Category','SubCategory'],axis=1)
GetProduct=pd.read_csv('dimNewProduct.csv',encoding='latin-1')
MergeData.ProductName=MergeData.ProductName.str.replace('“','')
MergeData.ProductName=MergeData.ProductName.str.replace('/',' ')
MergeData.ProductName=MergeData.ProductName.str.replace('”','')
MergeData=pd.merge(MergeData,GetProduct,how='left',on=['ProductID','ProductName'])


MergeData=MergeData.drop(['ProductID','ProductName','SellingPricePerUnit','PurchasingPricePerUnit'],axis=1)
MergeData=MergeData[['RowID','OrderID','OrderDateID','ShipDateID','ShipModeID','CustomerID','ProdID','CityID',
                      'RegionID','Sales','Quantity','Discount','Profit','ShippingCost','OrderPriorityID']]
MergeData.set_index('RowID',inplace=True)
print(MergeData.columns)
print(MergeData.shape)

MergeData.to_csv('FactTab.csv')