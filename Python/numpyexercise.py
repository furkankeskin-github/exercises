import numpy as np
#Numpy array'i oluşturma
result=np.array([2,3,4,5,6])
#Sıralı array oluşturma
result=np.arange(1,22)
#50'ye kadar sıralı dizi oluşturma
result = np.arange(50)
#3'er atlayan sıralı array oluşturma
result=np.arange(27,107,3)
#3 elemanlı 0 dizisi oluşturma
result=np.zeros(3)
#5 elemanlı 1 dizisi oluşturma
result=np.ones(5)
#Aralığı eş parçaya bölüp, dizi oluşturma
result=np.linspace(0,33,4)
#Aralıkta rastgele sayılarla dizi oluşturma
result=np.random.randint(0,27,5)
#Rastgele sayi
result=np.random.randint(27)
#Rastgele 5 sayili dizi oluşturma(0 ile 1 arasında)
result = np.random.rand(5)
#Rastgele 5 sayili dizi oluşturma(-2 ile 2 arasında)
result = np.random.randn(5)
#Dizi oluşturma ve şekillendirme
array=np.arange(0,50)
array1=array.reshape(5,10)
print(array1)
#Arrayi soldan sağa toplama
print(array1.sum(axis=1))
#Arrayi baştan aşağı toplama
print(array1.sum(axis=0))
#Dizideki en büyük elemanı almak
result=array1.max()
#Dizideki en küçük elemanı almak
result=array1.min()
#Dizi ortalamasını almak
result=array.mean()
#En büyük elemanın indexini verir
result=array.argmax()
#En küçük elemanın indexini verir
result=array.argmin()

print(result)