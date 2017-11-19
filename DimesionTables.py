import pandas as pd
import calendar
import numpy as np

'''''
#Dimesion Table For Shipmode
ShipModeData=pd.read_excel('DB.xls',usecols=['Ship Mode'])
ShipModeData=ShipModeData.drop_duplicates()
ShipModeData.index=range(0,len(ShipModeData))
ShipModeData['ShipModeID']=ShipModeData.index
NewID=ShipModeData.ShipModeID.astype(str)
NewID='SM'+NewID
ShipModeData['ShipModeID']=NewID
ShipModeData.set_index('ShipModeID',inplace=True)
ShipModeData.rename(columns={'Ship Mode':'ShipMode'},inplace=True)
print(type(ShipModeData))
ShipModeData.to_csv('dimShipMode.csv')

#Dimesion Table For Order Priority
OrderPrioData=pd.read_excel('DB.xls',usecols=['Order Priority'])
OrderPrioData=OrderPrioData.drop_duplicates()
OrderPrioData.index=range(0,len(OrderPrioData))
OrderPrioData['OrderPriorityID']=OrderPrioData.index
NewID=OrderPrioData.OrderPriorityID.astype(str)
NewID='OP'+NewID
OrderPrioData['OrderPriorityID']=NewID
OrderPrioData.set_index('OrderPriorityID',inplace=True)
print(type(OrderPrioData))
OrderPrioData.rename(columns={'Order Priority':'OrderPriority'},inplace=True)
OrderPrioData.to_csv('dimOrderPriority.csv')

#Dimesion Table For Order Table
OrderData=pd.read_excel('DB.xls',usecols=['Order ID','Order Priority'])
print(OrderData.shape)
OrderData=OrderData.drop_duplicates()
OrderData.rename(columns={'Order Priority':'OrderPriority','Order ID':'OrderID'},inplace=True)
print(OrderData.shape)
OrderPrio=pd.read_csv('dimOrderPriority.csv')
MergeData = pd.merge(OrderData, OrderPrio, how='left', on=['OrderPriority'])
MergeData=MergeData.drop('OrderPriority',axis=1)
MergeData.set_index('OrderID',inplace=True)
MergeData.to_csv('dimOrder.csv')



#Dimesion Table For Country
CountryData=pd.read_excel('DB.xls',usecols=['Country'])
CountryData=CountryData.drop_duplicates()
CountryData.index=range(0,len(CountryData))
CountryData['CountryID']=CountryData.index
NewID=CountryData.CountryID.astype(str)
NewID='CO'+NewID
CountryData['CountryID']=NewID
CountryData.set_index('CountryID',inplace=True)
CountryData.to_csv('dimCountry.csv')


#dimension table for state
StateData=pd.read_excel('DB.xls',usecols=['Country','State'])
StateData=StateData.drop_duplicates()
print(StateData)

Countries=pd.read_csv('dimCountry.csv')

MergeData = pd.merge(StateData,Countries, how='left', on=['Country'])
MergeData=MergeData.drop('Country',axis=1)
print(MergeData)

MergeData.index=range(0,len(MergeData))
MergeData['StateID']=MergeData.index
NewID=MergeData.StateID.astype(str)
NewID='ST'+NewID
MergeData['StateID']=NewID
MergeData.set_index('StateID',inplace=True)
#MergeData.to_csv("dimState.csv")



#Dimesion Table For City Table
CityData=pd.read_excel('DB.xls',usecols=['City','State','Country'])
CityData=CityData.drop_duplicates()

States=pd.read_csv('dimState.csv',encoding='latin-1')
Contry=pd.read_csv('dimCountry.csv')

Merg=pd.merge(States,Contry,how='left',left_on='CountryID',right_on='CountryID')
MergeData = pd.merge(CityData,Merg, how='left',left_on=['State','Country'],right_on=['State','Country'])
MergeData=MergeData.drop(['State','CountryID','Country'],axis=1)

MergeData.index=range(0,len(MergeData))
MergeData['CityID']=MergeData.index
NewID=MergeData.CityID.astype(str)
NewID='CI'+NewID
MergeData['CityID']=NewID
MergeData.set_index('CityID',inplace=True)
MergeData.to_csv("dimCity.csv")


#Dimesion Table For Segment
SegmentData=pd.read_excel('DB.xls',usecols=['Segment'])
SegmentData=SegmentData.drop_duplicates()
SegmentData.index=range(0,len(SegmentData))
SegmentData['SegmentID']=SegmentData.index
NewID=SegmentData.SegmentID.astype(str)
NewID='SE'+NewID
SegmentData['SegmentID']=NewID
SegmentData.set_index('SegmentID',inplace=True)
SegmentData.to_csv('dimSegment.csv')


#Dimesion Table For Customer Table
CustomerData=pd.read_excel('DB.xls',usecols=['Customer ID','Customer Name','Segment'])
CustomerData=CustomerData.drop_duplicates(subset=['Customer ID','Customer Name'])

Segments=pd.read_csv('dimSegment.csv')
MergeData = pd.merge(CustomerData,Segments, how='left', on=['Segment'])

MergeData=MergeData.drop('Segment',axis=1)
MergeData.rename(columns={'Customer ID':'CustomerID','Customer Name':'CustomerName'},inplace=True)
MergeData.set_index('CustomerID',inplace=True)
MergeData.to_csv('dimCustomer.csv')


#Dimesion Table For Market
MarketData=pd.read_excel('DB.xls',usecols=['Market'])
MarketData=MarketData.drop_duplicates()
MarketData.index=range(0,len(MarketData))
MarketData['MarketID']=MarketData.index
NewID=MarketData.MarketID.astype(str)
NewID='MA'+NewID
MarketData['MarketID']=NewID
MarketData.set_index('MarketID',inplace=True)
MarketData.to_csv('dimMarket.csv')

#Dimesion Table For Region
RegionData=pd.read_excel('DB.xls',usecols=['Region','Market'])
RegionData=RegionData.drop_duplicates()

Markets=pd.read_csv('dimMarket.csv',encoding='latin-1')
MergeData = pd.merge(RegionData,Markets, how='left',left_on='Market',right_on='Market')
print(MergeData.shape)

MergeData=MergeData.drop(['Market'],axis=1)

MergeData.index=range(0,len(MergeData))
MergeData['RegionID']=MergeData.index
NewID=MergeData.RegionID.astype(str)
NewID='RE'+NewID
MergeData['RegionID']=NewID
MergeData.set_index('RegionID',inplace=True)
print(MergeData)
MergeData.to_csv("dimRegion.csv")


#Dimesion Table For Category
CategoryData=pd.read_excel('DB.xls',usecols=['Category'])
CategoryData=CategoryData.drop_duplicates()
CategoryData.index=range(0,len(CategoryData))
CategoryData['CategoryID']=CategoryData.index
NewID=CategoryData.CategoryID.astype(str)
NewID='CA'+NewID
CategoryData['CategoryID']=NewID
CategoryData.set_index('CategoryID',inplace=True)
CategoryData.to_csv('dimCategory.csv')

#Dimesion Table For SubCategory
SubCategoryData=pd.read_excel('DB.xls',usecols=['Category','Sub-Category'])
SubCategoryData=SubCategoryData.drop_duplicates()

Catgory=pd.read_csv('dimCategory.csv')
MergeData = pd.merge(SubCategoryData,Catgory, how='left',on='Category')
print(MergeData.shape)

MergeData=MergeData.drop(['Category'],axis=1)

MergeData.index=range(0,len(MergeData))
MergeData['SubCategoryID']=MergeData.index
NewID=MergeData.SubCategoryID.astype(str)
NewID='SC'+NewID
MergeData['SubCategoryID']=NewID
MergeData.set_index('SubCategoryID',inplace=True)
MergeData.rename(columns={'Sub-Category':'SubCategory'},inplace=True)
print(MergeData)
MergeData.to_csv("dimSubCategory.csv")



#Dimesion Table For Order Date
OrderDateData=pd.read_excel('DB.xls',usecols=['Order Date'])
OrderDateData=OrderDateData.drop_duplicates()
OrderDateData.rename(columns={'Order Date':'OrderDate'},inplace=True)

OrderDateData.index=range(0,len(OrderDateData))
OrderDateData['OrderDateID']=OrderDateData.index
NewID=OrderDateData.OrderDateID.astype(str)
NewID='OD'+NewID
OrderDateData['OrderDateID']=NewID
OrderDateData.set_index('OrderDateID',inplace=True)
OrderDateData.OrderDate=pd.to_datetime(OrderDateData.OrderDate)
OrderDateData['Year']=OrderDateData.OrderDate.dt.year
OrderDateData['Month']=OrderDateData.OrderDate.dt.month
OrderDateData['Month'] = OrderDateData['Month'].apply(lambda x: calendar.month_abbr[x])
OrderDateData['Quarter']=OrderDateData.OrderDate.dt.quarter
print(OrderDateData.Quarter.dtype)

NewQ='Q'+OrderDateData.Quarter.astype(str)
OrderDateData['Quarter']=NewQ
OrderDateData.to_csv('dimOrderDate.csv')

#Dimesion Table For Order Date
ShipDateData=pd.read_excel('DB.xls',usecols=['Ship Date'])
ShipDateData=ShipDateData.drop_duplicates()
ShipDateData.rename(columns={'Ship Date':'ShipDate'},inplace=True)

ShipDateData.index=range(0,len(ShipDateData))
ShipDateData['ShipDateID']=ShipDateData.index
NewID=ShipDateData.ShipDateID.astype(str)
NewID='SD'+NewID
ShipDateData['ShipDateID']=NewID
ShipDateData.set_index('ShipDateID',inplace=True)
ShipDateData.ShipDate=pd.to_datetime(ShipDateData.ShipDate)
ShipDateData['Year']=ShipDateData.ShipDate.dt.year
ShipDateData['Month']=ShipDateData.ShipDate.dt.month
ShipDateData['Month'] = ShipDateData['Month'].apply(lambda x: calendar.month_abbr[x])
ShipDateData['Quarter']=ShipDateData.ShipDate.dt.quarter
print(ShipDateData.Quarter.dtype)

NewQ='Q'+ShipDateData.Quarter.astype(str)
ShipDateData['Quarter']=NewQ
print(ShipDateData.head())
ShipDateData.to_csv('dimShipDate.csv')

'''''
#Dimesion Table For Product
# ProductData=pd.read_excel('DB.xls',usecols=['Product ID','Product Name','Sub-Category','Sales','Quantity','Discount','Profit'])
# ProductData.rename(columns={'Product ID':'ProductID','Product Name':'ProductName','Sub-Category':'SubCategory'},inplace=True)
# ProductData=ProductData.drop_duplicates(subset=['ProductID','ProductName'])
#
# ProductData.ProductName=ProductData.ProductName.str.replace('“','')
# ProductData.ProductName=ProductData.ProductName.str.replace('/',' ')
# ProductData.ProductName=ProductData.ProductName.str.replace('”','')
#
# UnitPrice=ProductData.Sales/ProductData.Quantity
# SellPrice=UnitPrice/(1.0-ProductData.Discount)
# ProductData['SellingPricePerUnit']=SellPrice
#
# PurchasingPrice=(ProductData.Sales-ProductData.Profit)/ProductData.Quantity
# ProductData['PurchasingPricePerUnit']=PurchasingPrice
# #ProductData.set_index(['ProductID','ProductName'],inplace=True)
# ProductData=ProductData.drop(['Sales','Quantity','Discount','Profit'],axis=1)
#
# SubCat=pd.read_csv('dimSubCategory.csv')
# MergeData = pd.merge(ProductData,SubCat, how='left',on='SubCategory')
#
# MergeData=MergeData.drop(['SubCategory','CategoryID'],axis=1)
# MergeData.set_index(['ProductID','ProductName'],inplace=True)
# MergeData.to_csv('dimProduct.csv')
#
# #Dimesion Table For Product
# ProdData=pd.read_csv('dimProduct.csv',encoding='latin-1')
# ProdData.index=range(0,len(ProdData))
# ProdData['ProdID']=ProdData.index
# NewID=ProdData.ProdID.astype(str)
# NewID='P'+NewID
# ProdData['ProdID']=NewID
# ProdData.set_index('ProdID',inplace=True)
# print(ProdData)
# ProdData.to_csv('dimNewProduct.csv')



