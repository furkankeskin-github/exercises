# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:11:43 2021

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

#Fit eğitme, transform ise o eğitimi kullanma.
#X_Test için yeniden öğrenmeyip, daha önce öğrenilen yöntem kullanılıyor.
X_train=sc.fit_transform(x_train)
X_test=sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
log_reg=LogisticRegression(random_state=0)
log_reg.fit(X_train,y_train)

y_pred=log_reg.predict(X_test)
print(y_pred)
print(y_test)

from sklearn.metrics import confusion_matrix,classification_report
cm=confusion_matrix(y_test, y_pred)
print(cm)

print(classification_report(y_test,y_pred))