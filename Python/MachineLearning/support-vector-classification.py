# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:09:08 2021

@author: Furkan
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

veriler=pd.read_csv('veriler.csv')

x=veriler.iloc[:,1:4].values
y=veriler.iloc[:,4:].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33, random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()

X_train=sc.fit_transform(x_train)
X_test=sc.transform(x_test)

from sklearn.svm import SVC
#Hatırlamıyorsan kernel tricki araştır.
#Doğal parametresi rbf'tir. linear, poly, sigmoid, precomputed kullanılabilir.
svc=SVC(kernel='rbf')
svc.fit(X_train, y_train)

y_pred=svc.predict(X_test)
print(y_pred)

from sklearn.metrics import confusion_matrix
#X_testin tahminlerini gerçek değerlerle karşılaştır.
cm=confusion_matrix(y_test,y_pred)
print(cm)