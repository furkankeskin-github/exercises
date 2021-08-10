import requests
import json
#SİTEDEN VERİ ALMA
"""
r=requests.get("https://api.exchangeratesapi.io/latest")
#json datası yoksa hata verecek satır
r.json()
#site içeriğini yazdırma
print(r.text)
#Json'dan dict'e dönüştürme
result=json.loads(r.text)
# Dict'den Json'a string olarak dönüştürme
# result = json.dumps(r.text)
print(type(result))
print(result["rates"])
"""

#TARİHE GÖRE KUR ÇEKME UYGULAMASI
"""
#Base urlyi aldık
url=("https://api.exchangeratesapi.io/")
#Tarihi aldık
yil=input("Yılı giriniz:")
ay= input("Ayı giriniz:")
gün=input("Günü giriniz:")
#Url'ye tarihi ekleyip veriyi aldık
result=requests.get(url+yil+"-"+ay+"-"+gün)
#Veriyi json metnine çevirdik
result=json.loads(result.text)
#Yazdırdık
print(result)
"""
#Döviz Bozma Uygulaması
"""
#Base URL Alındı
url=api_url = "https://api.exchangeratesapi.io/latest?base="
#Döviz türleri ve miktarları alındı
bozdurulan=input("Bozulacak Döviz Türünü Giriniz:")
alinan=input("Alınacak Döviz Türünü Giriniz:")
miktar=int(input("Miktarı Giriniz:"))
#Siteden veriyi almak
result=requests.get(url+bozdurulan)
#Veriyi Json metnine dönüştürmek
result=json.loads(result.text)
#print(result)
#Kuru yazdırdık.
print("1 {0} = {1} {2}".format(bozdurulan,result["rates"][alinan],alinan))
#Döviz Bozdurma işlemini yaptık
print("{0} {1} karşılığında {2} {3} aldınız...".format(miktar,bozdurulan,miktar*result["rates"][alinan],alinan))
"""