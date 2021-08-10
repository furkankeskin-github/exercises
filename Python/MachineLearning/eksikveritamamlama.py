#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri yukleme

veriler = pd.read_csv('eksikveriler.csv')
#pd.read_csv("veriler.csv")

print(veriler)

#veri on isleme

boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)


#eksik veriler
#sci - kit learn

#Boş kolonları o kolonun ortalamasıyla doldurma
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)

#ülke gibi sınıflandırma değerlerini sayısal değere çevirme
#satırdayken sütuna geçiş yaptıracağız

#tüm satırlardaki, 0'dan 1'e kadar olan sütunları al ve ülke değişkenine ata.
ulke= veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

#Sayısallaştırma işlemini bununla yapacağız
#Label encoding her bir sayısal olmayan değere sırasıyla bir sayı verir
#Ama bu sayıyı makine anlamlandıramayacağı için one hit encoding ile kullanmak daha mantıklıdır

le=preprocessing.LabelEncoder()

#listenin içindeki her bir listeye gidip onun ilk index değerini aldık

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe= preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)


#Elimizdeki verileri toplayıp, birleştiriyoruz
#fr tr us sırası 0-1-2 rakamlarına göre verildi

print(list(range(22)))
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc)

sonuc2 = pd.DataFrame(data=Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

#Cinsiyet datasını tutuyor
sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ['cinsiyet'])
print(sonuc3)

#ülke ve diğer değişkenleri tutuyor
s=pd.concat([sonuc,sonuc2], axis=1)
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)


#Cinsiyeti tahmin etmek için veriyi bölüyoruz
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test=train_test_split(s, sonuc3, test_size=0.33, random_state=0)

#Scale ediyoruz
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()

X_train= scaler.fit_transform(x_train)
X_test= scaler.fit_transform(x_test)


