# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 14:04:38 2021

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

#Çoklu öğrenme metodu
from sklearn.ensemble import RandomForestRegressor
#n_estimators kaç tane decision tree çizileceğini belirler.
rf_reg=RandomForestRegressor(n_estimators=10, random_state=0)
#numpy.ravel() == numpy.reshape(-1) çok boyutlu diziyi tek boyutlu yapar.
#Sonuca etki etmedi?
rf_reg.fit(X,Y.ravel())

print(rf_reg.predict([[6.6]]))
plt.scatter(X,Y,color='green')
plt.plot(X, rf_reg.predict(X),color='blue')

Z=X+0.5
K=X-0.4

#Decision tree'de bunlar üst üste binerken, çoklu öğrenmede farklı sonuçlar elde ettik.
plt.plot(X,rf_reg.predict(Z),color='red')
plt.plot(X,rf_reg.predict(K),color='yellow')
