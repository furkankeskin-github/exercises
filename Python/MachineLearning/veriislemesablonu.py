# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:52:26 2021

@author: Furkan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

veriler=pd.read_csv('satislar.csv')
print(veriler)

#iloc ile de bu işlemi yapabilirdik.
#satislar=veriler.iloc[:,:1].values gibi

aylar=veriler[['Aylar']]
print(aylar)

satislar=veriler[['Satislar']]
print(satislar)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

x_train,x_test,y_train,y_test=train_test_split(aylar,satislar, test_size=0.3, random_state=0)

scaler=StandardScaler()
X_train=scaler.fit_transform(x_train)
X_test=scaler.transform(x_test)