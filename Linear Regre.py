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

Data=pd.read_csv('FactTab.csv',usecols=['ProdID','Sales','Quantity','Discount','Profit'])

# df=Data.groupby(['ProdID']).ProdID.agg(['count'])
# print(df['count'].sort_values())
Data.ProdID=Data.ProdID.str.replace('P','0')

Data.ProdID=pd.to_numeric(Data.ProdID,errors='coerce').fillna(0).astype(np.int64)

print(Data.ProdID.dtype)

df=Data[Data.ProdID==4640]

# sns.pairplot(df, x_vars=['Profit','Quantity','Discount'], y_vars='Sales', size=6, aspect=0.7, kind='reg')
# plt.show()

X=df[['Profit','Quantity','Discount']]
y=df['Sales']

# fill_0 = Imputer(missing_values=0, strategy="mean", axis=0)
# X = fill_0.fit_transform(X)

correlation = df.corr()
print(correlation)
# Dividing the plot into subplots for increasing size of plots
fig, heatmap = plt.subplots(figsize=(5, 5))
# Plotting the correlation heatmap
heatmap.matshow(correlation)
# Adding xticks and yticks
plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)
# Displaying the graph
plt.show()

#Blue -> Cyan -> Yellow -> Red -> Dark Red

print(df.head())
print("Score Of KFOLD: ")
linreg = linear_model.LinearRegression()
scores = cross_val_score(linreg, X, y, cv=10, scoring='neg_mean_squared_error')

mse = -scores

rmse = np.sqrt(mse)
print('RMSE',rmse.mean())


print("Score Of test split: ")
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg.fit(X_train, y_train)
y_pred = linreg.predict(X_test)
print('Y intercepsts:',linreg.intercept_)
print('X coefficients:',linreg.coef_)
print('RMSE',np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
print(linreg.predict([[-163.152,8,0.7]]))
#
#
#
# print("Profit prediction:")
# X=df[['Sales','Quantity','Discount']]
# y=df['Profit']
#
#
# # sns.pairplot(df, x_vars=['Sales','Quantity','Discount'], y_vars='Profit', size=6, aspect=0.7, kind='reg')
# # plt.show()
#
# linreg = linear_model.LinearRegression()
# scores = cross_val_score(linreg, X, y, cv=10, scoring='neg_mean_squared_error')
#
# mse_scores = -scores
#
# rmse = np.sqrt(mse_scores)
# print('RMSE Values:',rmse)
#
# print('RMSE',rmse.mean())