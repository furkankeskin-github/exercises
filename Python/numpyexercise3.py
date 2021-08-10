import numpy as np

# (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturma
array9=np.random.randint(10,50,(3,5))
result=array9
# Matrisin satır, sütun ve bütün toplamı
rowTotal=array9.sum(axis=1)
print("Satır Toplamı:",rowTotal)
colTotal=array9.sum(axis=0)
print("Sütun Toplamı:",colTotal)
Total=array9.sum()
print("Array Toplamı:",Total)

# (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçme
arr=np.arange(10,20)
result=arr[:3]

# Matrisi tersten yazırma
result=arr[::-1]

# Matrisin ilk satırını alma
result=array9[0]

# Matrisin 2. satırındaki 3. elemanı alma
result=array9[1,2]

# Matrisin tüm satırlarındaki ilk elemanı alma
result=array9[:,0]

# Matrisin karesini alma
result=array9**2

# Matris elemanlarının çift ve pozitif olanlarını alma
ciftler=array9[array9%2==0]
pozitifciftler=ciftler[ciftler>0]
result=pozitifciftler
print(result)