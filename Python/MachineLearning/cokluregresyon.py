#kutuphaneler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#veri yukleme

veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")

print(veriler)

boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy','kilo']]
print(boykilo)

#Boş kolonları o kolonun ortalamasıyla doldurma
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

#Aslında burda sadece yaş değil, diğer değişkenler de dolduruluyor.
Yas = veriler.iloc[:,1:4].values
print(Yas)
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)


#Kategorik-->Numerik
ulke= veriler.iloc[:,0:1].values
print(ulke)
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

ohe= preprocessing.OneHotEncoder()
ulke=ohe.fit_transform(ulke).toarray()
print(ulke)

#Erkek ve Kadın olarak 2 kolona ayırdık.
#Ancak bunlara dummy variable deniyor.
#Bu kolonlardan birini sistemi yanıltmasın diye sileceğiz.
c= veriler.iloc[:,0:1].values
print(c)
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
c[:,-1] = le.fit_transform(veriler.iloc[:,-1])
print(c)

ohe= preprocessing.OneHotEncoder()
c=ohe.fit_transform(c).toarray()
print(c)

sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc2 = pd.DataFrame(data=Yas, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

sonuc3 = pd.DataFrame(data = c[:,:1], index = range(22), columns = ['cinsiyet'])
print(sonuc3)

#dataframe birlestirme islemi
s=pd.concat([sonuc,sonuc2], axis=1)
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()

#x_train ile y_train arasında kendince lineer bir bağ kur.
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

#Boy kolonunu düşürdük, veriyi düzenledik.
boy=s2.iloc[:,3:4].values
print(boy)

veri=s2.drop(s2.iloc[:,3:4], axis=1)
print(veri)

x_train, x_test,y_train,y_test = train_test_split(veri, boy, test_size=0.33, random_state=0)

regressor2=LinearRegression()
regressor2.fit(x_train,y_train)
y_pred = regressor2.predict(x_test)

#BACKWARD ELIMINATION
import statsmodels.api as sm
#Çoklu regresyonda bir sabit çarpana ihtiyaç var.
#Birlerle dolu kolonu o yüzden ekledik
X=np.append(arr=np.ones((22,1)).astype(int), values=veri, axis=1)

#veriden tüm satırları al, 6 tane kolonu al
X_l=veri.iloc[:,[0,1,2,3,4,5]].values

#Ordinary least squares raporunu hazırlatıyoruz.
#Örneğin tarlaya en kısa boruları döşeyerek sulamak istersek bundan yararlanırız.
#Borular düz döşenmek zorundadır.
X_l=np.array(X_l, dtype=float)
model=sm.OLS(boy,X_l).fit()
print(model.summary())

#Test sonucunda x5 yani 4. indexteki kolonun p değeri yüksek olduğu için onu veriden atacağız.
X_l=veri.iloc[:,[0,1,2,3,5]].values

X_l=np.array(X_l, dtype=float)
model=sm.OLS(boy,X_l).fit()
print(model.summary())