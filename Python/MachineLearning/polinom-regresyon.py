# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 16:59:02 2021

@author: Furkan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataFrame= pd.read_csv('maaslar.csv')

x=dataFrame.iloc[:,1:2]
y=dataFrame.iloc[:,2:]



#Polinom regresyonla çalışılması gereken bir data ile lineer regresyonla çalışmayı deneyelim.
from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(x.values,y.values)

#Veriler grafiğe yazıldı
plt.scatter(x.values,y.values, color='green')
#Lineer tahmin çizgimiz
plt.plot(x,lr.predict(x.values), color='red')

#-----------------------------------------------------------------------------
X=x.values
Y=y.values
#polynomial regression
from sklearn.preprocessing import PolynomialFeatures
#4. dereceden bir polynomialFeatures objesi oluşturduk
#4. dereceden olmasının sebebi verinin tam olarak buna uygun hazırlanması
pr=PolynomialFeatures(degree=4)

#X değerini 4. dereceden polinom değerlerine dönüştürüyoruz.
x_poly=pr.fit_transform(X)
print(x_poly)

#Lineer regresyon çizer gibi bu veriye göre lr'yi eğitiyoruz.
lr2=LinearRegression()
lr2.fit(x_poly,y)

plt.scatter(X, Y, color='green')
plt.plot(X,lr2.predict(pr.fit_transform(X, )), color='blue')

#-----------------------------------------------------------------------------
#Lineer eğitim ve Polinomal eğitim arasındaki tahmin farkları
print(lr.predict([[11]]))
print(lr2.predict(pr.fit_transform([[11]])))
