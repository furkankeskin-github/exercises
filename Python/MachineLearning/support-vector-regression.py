# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 17:57:55 2021

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

from sklearn.svm import SVR
svr_reg=SVR(kernel='rbf')
svr_reg.fit(x_sc, y_sc)

plt.scatter(x_sc, y_sc, color='green')
#Elimizdeki her bir x_sc için bilgisayarın tahminini çizdiriyoruz
plt.plot(x_sc, svr_reg.predict(x_sc), color='blue')