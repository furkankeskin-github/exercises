işçi = list()

ArızaDurumu = {
    "Bakım",
    "Bozuk",
}


def pEkle():
    işçi.append({
        "ad": input("işçi adını giriniz: "),
        "soyad": input("işçi Soyadını giriniz: "),
        "kullanıcıAdı": "biyoser21",
        "şifre": "bct2021"
    }, )

    print("ekleme başarılı")


def pListele():
    for value, i in enumerate(personel, 1):
        print("işçi " + str(value), end="\n\t")
        print("adı: " + i["ad"], end="\n\t")
        print("soyadı: " + i["soyad"])


def pSil():
    while True:

        try:
            pListele()
            deger = input("kaçıncı işçi silinecek (örnek:1): ")
            işçi.remove(işçi[int(deger) - 1])
            break
        except:
            print("Yanlış değer girdiniz: ")


def mEkle():
    with open("MüşteriListesi.txt", "a", encoding="UTF-8") as dosya:
        deger = input("Müşteri adını giriniz: ") + "-" \
                + input("Müşteri soyadını giriniz: ") + "-" \
                + input("Telefon Numarsını giriniz: ") + "-" \
                + input("E-Mail adresini giriniz: ") + "-" \
                + input("Ev adresini giriniz: ") + "-" \
                + input("Hastane adı: ") + " \n"

        dosya.write(deger)


def mListele():
    list = ["ad: ", "soyad: ", "numara: ", "E-mail adresi: ", "Ev adresi: ", "Hastane Adı: "]
    with open("MüşteriListesi.txt", "r", encoding="UTF-8") as dosya:
        for value, i in enumerate(dosya.readlines(), 1):
            print(str(value) + ". Müşteri")
            for index, y in enumerate(i.split("-"), 0):

                try:

                    print(list[index] + y)
                except:

                    break


def mSil():
    mListele()
    index = input("Kaçıncı müşteri silinsin: ")
    with open("MüşteriListesi.txt", "r", encoding="UTF-8") as dosya:
        deger = str()
        for val, i in enumerate(dosya.readlines(), 1):
            if val != int(index):
                deger += i

    with open("MüşteriListesi.txt", "w", encoding="UTF-8") as dosya:
        dosya.write(deger)


def sEkle():
    for index, i in enumerate(ArızaDurumu, 1):
        print(str(index) + ": " + i)

    deger = input("arıza tipini seçiniz:")

    for val, i in enumerate(ArızaDurumu, 1):

        if int(deger) == val:
            musteriadi = input("Müşteri adını giriniz: ")
            hepsi = musteriadi + "-" + i + "-" + input("Arızanızı yazınız: ") + "-"
            arizamaliyeti = input("Arıza Maliyeti: ")
            hepsi += arizamaliyeti + " \n"
            with open("ServisTalepleriDevam.txt", "a", encoding="UTF-8") as dosya:
                dosya.write(hepsi)

            with open("ServisTalepleri.txt", "a", encoding="UTF-8") as dosya:
                dosya.write(hepsi)

            with open("MusteriMaliyet.txt", "a", encoding="UTF-8") as dosya:
                dosya.write(musteriadi + "-" + arizamaliyeti + " \n")

            with open(f"{musteriadi}.txt", "a", encoding="UTF-8") as dosya:
                dosya.write(musteriadi + "-" + arizamaliyeti + " \n")


def sListele():
    list = ["Müşteri adı: ", "Arıza Durumu: ", "Arıza Açıklaması: ", "Arıza Maliyeti"]
    with open("ServisTalepleriDevam.txt", "r", encoding="UTF-8") as dosya:
        for value, i in enumerate(dosya.readlines(), 1):
            print(str(value) + ". Arıza")
            for index, y in enumerate(i.split("-"), 0):
                try:
                    print(list[index] + y)
                except:

                    break


def sSil():
    sListele()
    index = input("Kaçıncı Arıza silinsin: ")
    with open("ServisTalepleriDevam.txt", "r", encoding="UTF-8") as dosya:
        deger = str()
        for val, i in enumerate(dosya.readlines(), 1):
            if val != int(index):
                deger += i
            else:
                with open("ServisTalepleriBiten.txt", "a", encoding="UTF-8") as dosya:
                    dosya.write(i)

    with open("ServisTalepleriDevam.txt", "w", encoding="UTF-8") as dosya:
        dosya.write(deger)


def mBakiyeSorgulama():
    list = ["Müşteri adı: ", "Arıza Maliyeti"]
    musteri = input("Musteri adını giriniz:")
    try:
        with open(f"{musteri}.txt", "r", encoding="UTF-8") as dosya:
            for index, i in enumerate(dosya.readlines()):
                print(list[index] + i)
    except:
        print("musteri bulunmamaktadır")


def mBakiyeSorgulamaHepsi():
    list = ["Müşteri adı: ", "Arıza Maliyeti"]

    try:
        with open(f"MusteriMaliyet.txt", "r", encoding="UTF-8") as dosya:
            for index, i in enumerate(dosya.readlines()):
                print(list[index] + i)


    except:
        pass


def ekran():
    while True:
        print("1.işçi İşlemleri", "2.Servis Talep İşlemleri", "3.Müşteri İşlemleri", "4.Cari Hesap İşlemleri","5.Çıkış",sep="\n")
        istek = input("Gitmek istediğiniz servisin değerini seçiniz(örnek:1,5 gibi):")
        if istek == "1":
            print("1.işçi İşlemleri", "a) işçi Ekleme",
                          "b) işçi listeleme", "c) işçi Silme",
                          "İşlem yapmak istediğiniz degeri giriniz(örnek:a,b gibi):",sep="\n\t")
            deger=input()
            if deger == "a":
                pEkle()
            elif deger == "b":
                pListele()
            elif deger == "c":
                pSil()
        elif istek == "2":

            print("2.Servis Talep İşlemleri", "a) Servis Talep Ekleme",
                          "b) Servis Talepleri Görüntüleme ",
                          "c) Servis Talepleri Silme",
                          "İşlem yapmak istediğiniz degeri giriniz(örnek:a,b gibi):",sep="\n\t")
            deger=input()
            if deger == "a":
                sEkle()
            elif deger == "b":
                sListele()
            elif deger == "c":
                sSil()
        elif istek == "3":
            print("3.Müşteri İşlemleri", "a) Müşteri Kaydı Ekleme ",
                          "b) Müşteri Kaydı Listeleme ", "c)Müşteri Kaydı Silme",
                          "İşlem yapmak istediğiniz degeri giriniz(örnek:a,b gibi):",sep="\n\t")
            deger=input()
            if deger == "a":
                mEkle()
            elif deger == "b":
                mListele()
            elif deger == "c":
                mSil()
        elif istek == "4":
            print("4.Cari Hesap İşlemleri", "a) Müşteri Bakiye Sorgulama",
                          "b) Müşteri Bakiyeleri Listeleme ",
                          "İşlem yapmak istediğiniz degeri giriniz(örnek:a,b gibi):",sep="\n\t")
            deger=input()
            if deger == "a":
                mBakiyeSorgulama()
            elif deger == "b":
                mBakiyeSorgulamaHepsi()

        elif istek == "5":
            break
        else:
            print("yanlış giriş!!!! Tekrar Deneyin")


def kullanicigirisi(kullaniciad='biyoser20', kullanicisifre='bct2020'):
    for i in range(3, 0, -1):
        print(f"{i} giriş hakkınız kaldı")
        ad = input('adınızı giriniz: ')
        while len(ad) <= 5 or len(ad) >= 15:
            print('adınız 5 ten büyük ve 15ten küçük olmak zorunda')
            ad = input('yeni ad giriniz: ')

        şifre = input('şifre giriniz: ')
        while len(şifre) <= 6 or len(şifre) >= 15:
            print('şifreniz 6 ten büyük ve 15 ten küçük olmak zorunda')
            şifre = input('yeni şifrenizi giriniz: ')

        if ad.upper() == kullaniciad.upper() and şifre.upper() == kullanicisifre.upper():
            print('giriş başarılı')
            ekran()
            return True
        elif ad.upper() != kullaniciad.upper() and şifre.upper() == kullanicisifre.upper():
            print('adınız yanlış şifreniz doğru')
        elif ad.upper() == kullaniciad.upper() and şifre.upper() != kullanicisifre.upper():
            print('adınız doğru şifreniz yanlış')
        elif ad.upper() != kullaniciad.upper() and şifre.upper() != kullanicisifre.upper():
            print('adınız ve şifreniz yanlış')
    return False


kullanicigirisi()