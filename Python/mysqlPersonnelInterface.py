import mysql.connector
import sys

mydb=mysql.connector.connect(
    host= "localhost",
    user="root",
    password="1234",
    database="exercise2"
)
mycursor=mydb.cursor(buffered=True)

def pListele():
    print("\n Personel Listesi \n")
    mycursor.execute("SELECT * FROM personel")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x[0],x[1],x[2], sep="---")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")

def pEkle():
    print("\n Personel Ekleme \n")
    sql=("INSERT INTO personel (personelname,personelsurname) VALUES (%s,%s)")
    isim=input("Personel ismini giriniz:")
    soyisim=input("Personel soy adını giriniz:")
    val=(isim,soyisim)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"tane veri eklendi.")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")


def pSil():
    print("\n Personel Silme \n")
    sql=("DELETE FROM personel WHERE idpersonel=%s ")
    mycursor.execute("SELECT * FROM personel")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x)
    kullanicigirisi=input("Silmek istediğiniz personelin id'sini giriniz:")
    val=(kullanicigirisi,)
    mycursor.execute(sql,val)
    mydb.commit()
    print("\n Personel Silindi \n")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")

def sEkle():
    print("\n Servis Ekleme \n")
    sql=("INSERT INTO servis (servistalep,servissahibino,servispersonel) VALUES (%s,%s,%s)")
    servistalep=input("Servis talebini kısa şekilde giriniz:")
    servismüsteri=input("Talepte bulunan müşterinin id'sini giriniz:")
    servispersonel=input("Taleple ilgilenecek personel id'sini giriniz:")
    val=(servistalep,servismüsteri,servispersonel)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"tane veri eklendi.")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")
    
def sListele():
    print("\n Servis Listeleme \n")
    mycursor.execute("SELECT servis.idservis, servis.servistalep, müsteri.müsteriname, müsteri.müsterisurname, personel.personelname, personel.personelsurname FROM servis INNER JOIN müsteri ON servis.servissahibino=müsteri.idmüsteri INNER JOIN personel ON servis.servispersonel=personel.idpersonel")
    myresult=mycursor.fetchall()
    for x in myresult:
        print(x[0],x[1],x[2],x[3],x[4],x[5],sep="---")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")
def sSil():
    print("\n Servis Kaydı Silme \n")
    sql=("DELETE FROM servis WHERE idservis=%s")
    mycursor.execute("SELECT * FROM servis")
    servisresult=mycursor.fetchall()
    for x in servisresult:
        print(x)
    kullanicigirisi=input("Silmek istediğiniz talebin id'si:")
    val=(kullanicigirisi,)
    mycursor.execute(sql,val)
    print(mycursor.rowcount,"tane veri silindi.")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")

def personel():
    while True:
        islem = input('1- Personel Ekleme\n2- Personel Listeleme\n3- Personel Silme\n4- Üst Menü\n')

        if islem == '1':
            print("Personel Ekleme")
            pEkle()
        elif islem == '2':
            print("Personel Listeleme")
            pListele()
        elif islem == '3':
            print("Personel Silme")
            pSil()
        elif islem == '4':    
            sistem()
        else :
            print("Yanlış Tuşa Bastınız. Tekrar Deneyiniz.")
            continue

def servis():
    while True:
        islem = input('1- Servis Talep Ekleme\n2- Servis Talepleri Görüntüleme\n3- Servis Talepleri Kapatma\n4- Üst Menü\n')

        if islem == '1':
            print("Servis Talep Ekleme")
            sEkle()
        elif islem == '2':
            print("Servis Talepleri Görüntüleme")
            sListele()
        elif islem == '3':
            print("Servis Talepleri Kapatma")
            sSil()
        elif islem == '4':    
            sistem()
        else :
            print("Yanlış Tuşa Bastınız. Tekrar Deneyiniz.")
            continue

def mEkle():
    print("\n Müşteri Ekleme \n")
    sql=("INSERT INTO müsteri (müsteriname,müsterisurname,müsteribakiye) VALUES (%s,%s,%s)")
    müsteriname=input("Müşteri adını giriniz:")
    müsterisurname=input("Müşteri soy adını giriniz:")
    müsteribakiye=int(input("Müşteri Bakiyesini Giriniz:"))
    val=(müsteriname,müsterisurname,müsteribakiye)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"tane veri eklendi.")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")

def mListele():
    print("\n Müşteri Listeleme \n")
    mycursor.execute("SELECT * FROM müsteri")
    müsteriresult=mycursor.fetchall()
    for x in müsteriresult:
        print(x[0],x[1],x[2], sep="---")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")

def mSil():
    print("\n Müşteri Silme \n")
    sql=("DELETE FROM müsteri WHERE idmüsteri=%s ")
    mycursor.execute("SELECT * FROM müsteri")
    müsteriresult=mycursor.fetchall()
    for x in müsteriresult:
        print(x)
    kullanicigirisi=input("Silinecek müşterinin id'sini giriniz:")
    val=(kullanicigirisi,)
    mycursor.execute(sql,val)
    mydb.commit()
    print(mycursor.rowcount,"tane veri silindi.")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")
    
def mBakiyeSorgulama():
    print("\n Müşteri Bakiye Sorgulama \n")
    sql=("SELECT müsteribakiye FROM müsteri WHERE müsteriname=%s and müsterisurname=%s")
    müsteriad=input("Müşteri adını giriniz:")
    müsterisoyad=input("Müşteri soy adını giriniz:")
    val=(müsteriad.lower(),müsterisoyad.lower(),)
    mycursor.execute(sql,val)
    myresult=mycursor.fetchall()
    for x in myresult:
        myresult=x[0]
    print(f"Müşterinin Bakiyesi {myresult} Türk Lirasıdır")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")
    
def mBakiyeListeleme():
    print("\n Müşteri Bakiye Listeleme \n")
    sql=("SELECT * FROM müsteri")
    mycursor.execute(sql)
    result=mycursor.fetchall()
    for x in result:
        print(x[0],x[1],x[2],x[3], sep="---")
    input("Personel menüsüne çıkmak için herhangi bir tuşa basınız...")
def müsteri():
    while True:
        islem = input('1- Müşteri Kaydı Ekleme\n2- Müşteri Kaydı Listeleme\n3- Müşteri Kaydı Silme\n4- Üst Menü\n')

        if islem == '1':
            print("Müşteri Kaydı Ekleme")
            mEkle()
        elif islem == '2':
            print("Müşteri Kaydı Listeleme")
            mListele()
        elif islem == '3':
            print("Müşteri Kaydı Silme")
            mSil()
        elif islem == '4':    
            sistem()
        else :
            print("Yanlış Tuşa Bastınız. Tekrar Deneyiniz.")
            continue

def carihesap():
    while True:
        islem = input('1- Müşteri Bakiye Sorma\n2- Müşteri Bakiye Listeleme\n3- Üst Menü\n')

        if islem == '1':
            print("Müşteri Bakiye Sorma")
            mBakiyeSorgulama()
        elif islem == '2':
            print("Müşteri Bakiye Listeleme")
            mBakiyeListeleme()
        elif islem == '3':    
            sistem()
        else :
            print("Yanlış Tuşa Bastınız. Tekrar Deneyiniz.")
            continue


def sistem():
    while True:
        islem = input('1- Personel İşlemleri\n2- Servis Talep İşlemleri\n3- Müşteri İşlemleri\n4- Cari Hesap İşlemleri\n5-Çıkış İçin Q harfine basınız\n')

        if islem == '1':
            personel()
        elif islem == '2':
            servis()
        elif islem == '3':
            müsteri()
        elif islem == '4':    
            carihesap()
        elif islem.lower() == "q":
            mydb.close()
            sys.exit(0)
        else :
            print("Yanlış Tuşa Bastınız. Tekrar Deneyiniz.")
            continue

sistem()