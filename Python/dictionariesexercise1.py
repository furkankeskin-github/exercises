#Sözlük oluşturma
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Değer yazdırma
print(thisdict["model"])

#Değer değiştirme
thisdict["year"]=2020

#Tüm anahtar kelimeleri yazdırma
for x in thisdict:
  print(x)

#Tüm değerleri yazdırma
for x in thisdict:
  print(thisdict[x])
#veya
for x in thisdict.values():
  print(x)

#Tüm anahtar kelimeleri ve değerleri yazdırma
for x, y in thisdict.items():
    print(x, y)

#Sözlükte anahtar kelime var mı diye kontrol etmek
if "model" in thisdict:
    print("model anahtarı sözlükte var.")

#Sözlük uzunluğunu öğrenme
print(len(thisdict))

#Sözlüğe ekleme yapma
thisdict["color"]="red"

#Sözlükten silme
thisdict.pop("model")
#veya
#del thisdict["model"]

#Son ekleneni silme
thisdict.popitem()

#Sözlüğü silme
#del thisdict

#Sözlüğü kopyalama
mydict=thisdict.copy()

#Sözlüğün içini boşaltma
thisdict.clear()

#Tüm her şeyi yazdırma
print(thisdict)
print(mydict)