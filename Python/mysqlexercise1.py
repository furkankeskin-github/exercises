import mysql.connector

#Database'e bağlanma
mydb = mysql.connector.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "1234",
    database= "school"
    #database = "node-app" şeklinde istediğimiz database'e bağlanabiliriz. Ayrıca database'in var olup, olmadığını kontrol edebiliriz.
)
print(mydb)

#Database'e cursoru koyma. buffered kullanılmazsa tek veri çekimlerinde fetchall sorun yaratır.
mycursor = mydb.cursor(buffered=True)

#Var olan Database'leri görme
mycursor.execute('SHOW DATABASES')
print("\n Var olan veri tabanları \n")
for x in mycursor:
    print(x)

#Tablo yaratma
mycursor.execute("CREATE TABLE sınıflar (name VARCHAR(50))")

#Var olan tabloya benzersiz numara atama
mycursor.execute("ALTER TABLE sınıflar ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#Tablodaki her veriye benzersiz numara atama
mycursor.execute("CREATE TABLE sınıflar2 (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(50))")
mycursor.execute("ALTER TABLE sınıflar2 ADD COLUMN surname VARCHAR(50)")

#Var olan tabloları görme
mycursor.execute('SHOW TABLES')
print("\n Var olan tablolar \n")
for x in mycursor:
    print(x)

#Sütun'a veri girişi
sql="INSERT INTO sınıflar2 (name,surname) VALUES (%s,%s)"
val=[('Uğur','Al'),
('Ceyda', 'Tütüncü'),
('Ceren','Teksoy'),
('Asena','Turan')]

#Birden çok veri girdiğimiz için execute'un sonuna many ekledik
mycursor.executemany(sql,val)
mydb.commit()

#Eklenen verileri sayma
print(mycursor.rowcount,"tane veri eklendi.")

#Eklenen son verinin id'sini alma
print("Son verinin id'si:", mycursor.lastrowid)

#Tablodaki tüm verileri alma
mycursor.execute('SELECT * FROM sınıflar2')
myresult=mycursor.fetchall()

for x in myresult:
    print(x)

#Tablodaki seçili sütunları alma
mycursor.execute('SELECT id,surname FROM sınıflar2')
myresult1=mycursor.fetchall()

for x in myresult1:
    print(x)

#Sadece tek satırdaki verileri çekmek 
mycursor.execute('SELECT * FROM sınıflar2')
myresult2=mycursor.fetchone()

print(myresult2)

#Database'de sorgu yapma
sql="SELECT * FROM sınıflar2 WHERE name='Tansel' "
mycursor.execute(sql)
myresultname=mycursor.fetchall()

for x in myresultname:
    print(x)

#Database'de içereni bulma
sql="SELECT * FROM sınıflar2 WHERE name LIKE '%ü%' "
mycursor.execute(sql)
myresultname2=mycursor.fetchall()

for x in myresultname2:
    print(x)

#Kullanıcıdan giriş alarak sorgu yapma
sql="SELECT * FROM sınıflar2 WHERE name=%s"
#"Asena"dan sonra virgül olmak zorunda
name=("Asena",)
mycursor.execute(sql,name)
myresultname3=mycursor.fetchall()

for x in myresultname3:
    print(x)

#Sorguları sıralama
print("\nOrdering by name\n")
sql="SELECT * FROM sınıflar2 ORDER BY name"
mycursor.execute(sql)
myresultnameorder=mycursor.fetchall()

for x in myresultnameorder:
    print(x)

#Sorguları azalan şekilde sıralama
print("\nOrdering by name as descending\n")
sql="SELECT * FROM sınıflar2 ORDER BY name DESC"
mycursor.execute(sql)
myresultnameorder=mycursor.fetchall()

for x in myresultnameorder:
    print(x)

#Veritabanından veri silme
sql=("DELETE FROM sınıflar2 WHERE name='Uğur'")
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "tane veri silindi")

#Kullanıcıya Veri Sildirme
sql=("DELETE FROM sınıflar2 WHERE name=%s")
name=("Tansel",)
mycursor.execute(sql,name)
mydb.commit()

print(mycursor.rowcount, "tane veri silindi")

#Tablo silme
sql=("DROP TABLE sınıflar2")
mycursor.execute(sql)

#Eğer varsa tabloyu silme
sql=("DROP TABLE IF EXISTS sınıflar2")
mycursor.execute(sql)

#Veri değiştirme
sql=("UPDATE sınıflar2 SET name='Aylin' WHERE name='Ayda'")
mycursor.execute(sql)
mydb.commit()

print(mycursor.rowcount, "tane veri değiştirildi")

#Kullanıcıya veri değiştirtme
sql=("UPDATE sınıflar2 SET name=%s WHERE name=%s")
val=("Aycan","Aylin")
mycursor.execute(sql,val)
mydb.commit()

print(mycursor.rowcount, "tane veri değiştirildi")

#İlk 5 kaydı alma
print("\n ilk 5 kaydı alma\n")
mycursor.execute("SELECT * FROM sınıflar2 LIMIT 5")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#Belirli kayıtları alma. OFFSET değeri index gibidir.
print("\n belirli kayıtları alma\n")
mycursor.execute("SELECT * FROM sınıflar2 LIMIT 2 OFFSET 2")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)