import pandas as pd

#Dataset açma
df = pd.read_csv("datasets/data.csv")
result=df

#Sütunları öğrenme
result=df.columns

#İlk 5 veriyi alma
result=df.head()

#Baştan itibaren belirli sayıda veriyi alma
result=df.head(15)

#Sondan 5 veriyi alma
result=df.tail()

#Sondan itibaren belirli sayıda veriyi alma
result=df.tail(15)

#Toplam veri sayısını öğrenme
result=len(df.index)

#Belirli bir sütundan veriyi alma
result = df["Cinsiyet"]

#Belirli bir sütundan ilk 5 veriyi alma
result=df["Cinsiyet"].head()

#AKP'li olanları alma
result=df[df["parti"]=="AKP"]

#AKP'li olanların sayısını alma
result=len(df[df["parti"]=="AKP"].index)

#AKP'li olup, ekonominin iyi olduğunu düşünen lisans mezunları
result=df[(df['parti']=='AKP') & (df['soru1']=='Evet') & (df['Egitim']=='Lisans')]

#AKP'li olup, ekonominin iyi olduğunu düşünen lisans mezunlarının sayısı
result=len(df[(df['parti']=='AKP') & (df['soru1']=='Evet') & (df['Egitim']=='Lisans')].index)

print(result)