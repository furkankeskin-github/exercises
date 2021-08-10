import pandas as pd

df=pd.read_csv("datasets/nba.csv")

#Maaş ortalamasını alma
result=df['Salary'].mean()

#En yüksek maaşı alma
result=df['Salary'].max()

#En düşük maaşı alma
result=df['Salary'].min()

#En yüksek maaşı alan oyuncuyunun sadece adını alma
result=df[df['Salary']==df['Salary'].max()]['Name'].iloc[0]

#20-25 yaş oyuncuların yaşlarına göre sıralı oynadıkları takım listesi
result=df[(df['Age']>= 20) & (df['Age']<=25)][['Name','Team','Age']].sort_values('Age',ascending=False)

#Kobe Bryant'ın takımını bulma
result=df[df['Name']=='Kobe Bryant']['Team'].iloc[0]

#Takımlara göre ortalama maaş
result=df.groupby('Team').mean()['Salary']

#Kaç farklı takım olduğunu bulma
result=len(df.groupby('Team'))
#veya
result = df["Team"].nunique()

#Her takımda kaç oyuncu bulunmaktadır
result=df['Team'].value_counts()

#Boş verileri düşürme(inplace ile yapılırsa df'ye kaydolur. Diğer türlü geçici işlem)
df.dropna(how='any',inplace=True)
#Any olursa herhangi bir eksik ise veri silinir
#All olursa tüm değerleri eksik ise veri silinir

#İsminde 'and' geçenleri alma
result=df[df['Name'].str.contains("and")]
#veya
def str_bul(name):
    if 'and' in name.lower():
        return True
    return False
result=df[df['Name'].apply(str_bul)]

print(result)