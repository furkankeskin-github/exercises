
#Farklı naive bayes türleri var.

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


from sklearn.tree import DecisionTreeClassifier
#default parametresi gini. İkisi de aynı sonucu verdi.
dtc=DecisionTreeClassifier(criterion='entropy')
dtc.fit(X_train,y_train)

y_pred=dtc.predict(X_test)
print(y_pred)

from sklearn.metrics import confusion_matrix
#X_testin tahminlerini gerçek değerlerle karşılaştır.
cm=confusion_matrix(y_test,y_pred)
print(cm)