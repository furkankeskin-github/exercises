# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:51:12 2021

@author: Furkan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataFrame= pd.read_csv('maaslar.csv')

x=dataFrame.iloc[:,1:2]
y=dataFrame.iloc[:,2:]
X=x.values
Y=y.values

#SVR'da uç noktalar çok etki yaptığı için verileri scale ettik.
from sklearn.preprocessing import StandardScaler
scaler1=StandardScaler()
scaler2=StandardScaler()
x_sc=scaler1.fit_transform(X)
y_sc=scaler2.fit_transform(Y)



#------------------------------------------------------------------------
#KARAR AGACI
from sklearn.tree import DecisionTreeRegressor
r_dt=DecisionTreeRegressor(random_state=0)
r_dt.fit(X,Y)

plt.scatter(X, Y, color='green')
plt.plot(X,r_dt.predict(X),color='blue')

#Decision tree'nin değerleri aynı kümeye indirgediğini göstermek için X değerine
#0.5 ekleyip, 0.4 çıkarıyoruz. 0.4 olmasının nedeni 0.5 iken bir alt değere yuvarlaması.
Z=X+0.5
K=X-0.4

plt.plot(X,r_dt.predict(Z),color='red')
plt.plot(X,r_dt.predict(K),color='yellow')
print(r_dt.predict([[11]]))
print(r_dt.predict([[6.6]]))