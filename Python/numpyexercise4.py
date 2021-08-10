import numpy as np
#Arraylerle matematik işlemleri yapılabilir
numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

#Dizi elemanlarının trigonometrik değerlerini alma
result = np.sin(numbers1)
result = np.cos(numbers1)
result = np.sqrt(numbers1)
result = np.log(numbers1)

#Dizileri alt alta stackleme
result = np.vstack((numbers1,numbers2))

#Dizileri yan yana stackleme
result = np.hstack((numbers1,numbers2))

#Dizileri tekrar vektör haline getirme
array=np.random.randint(10,100,(3,5))
vector=np.resize(array,(15))
result=vector

#Dizileri birleştirme (integer olmaları gerekir)(sütun sayısı eşit olmalı)
AR=np.zeros((3,2), dtype=int)
AR2=np.ones((3,2), dtype=int)
result=np.concatenate((AR,AR2))

print(result)