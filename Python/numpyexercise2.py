import numpy as np
#10 ile 70 arasında 5,10 boyutunda array oluşturma
array=np.random.randint(low=10,high=70, size=(5,10))
print(array)
#Array'in türünü öğrenme
print(type(array))
#Array'in kaç boyutlu olduğunu öğrenme
print(array.ndim)
#Array'in şeklini öğrenme
print(array.shape)