# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:24:06 2021

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


from sklearn.neighbors import KNeighborsClassifier
#Doğal parametreleri bunlardır.
#n_neighbors 5 iken 0 doğru, 1 hata, 6 hata 1 doğru bulurken
#1 iken 1 doğru, 0 hata, 1 hata 6 doğru buldu.
knn=KNeighborsClassifier(n_neighbors=1, metric='minkowski')
knn.fit(X_train,y_train)

#X_testten sonucunu tahmin et.
y_pred=knn.predict(X_test)

from sklearn.metrics import confusion_matrix
#X_testin tahminlerini gerçek değerlerle karşılaştır.
cm=confusion_matrix(y_test,y_pred)
print(cm)
