# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:21:33 2021

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

from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor(n_estimators=10, random_state=0)
rf_reg.fit(X,Y.ravel())

#r2_score'u import ettik
#r2 1'e yaklaştıkça olumlu olur. 
#En kötü algoritma 0'dır. Altında alan iq olarak zayıftır.
from sklearn.metrics import r2_score
#Doğru değerler ve tahmin değerleri
#X'ten y değerlerini tahmin etti ve r^2'e göre puanlandırdı.
print(r2_score(Y,rf_reg.predict(X)))


#Decision tree test aşamasında mükkemmel çıkabilir. Ama gerçek verilerle öyle değildir.
#R2 değeri çok ciddiye alınmamalı.