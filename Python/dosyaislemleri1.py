# 'r' modu: Dosyayı sadece okumak için açar. Bu mod varsayılan moddur.
# 'r+' modu: Dosyayı hem okumak hem de yazmak için açar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturulmaz.
# 'w' modu: Dosyayı sadece yazmak için açar. Varolan dosyanın üzerine yazma işlemini yapar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturur.
# 'w+' modu: Dosyayı hem okumak hem de yazmak için açar. Varolan dosyanın üzerine yazma işlemini yapar. Eğer çağrılan dosya bulunamadıysa yeni bir dosya oluşturur.
# 'a' modu: Dosyayı ekleme işlemi için açar. Eğer çağrılan dosya bulunursa, en sonundan eklemeye devam eder. Eğer dosya yoksa sadece yazma işlemi yapacak yeni bir dosya oluşturur.
# 'a+' modu: Dosyayı hem ekleme hem de okuma işlemi için açar. Eğer çağrılan dosya bulunursa, en sonundan eklemeye devam eder. Eğer dosya yoksa yazma ve okuma işlemleri yapacak yeni bir dosya oluşturur.

#Dosyaya ekleme yapmak
#Encoding türkçe karakterleri okuyabilmek için var.
dosya=open("dosyaislemleri1.txt","a+",encoding="utf-8")
dosya.write("\nEkleme başarılı")
dosya.close()

#Dosyayı sürekli kapatıp açmamak için with kullanılabilir
with open("dosyaislemleri1.txt","a+",encoding="utf-8") as dosya:
    dosya.write("\nDosyamızı with ile açtık")

#OS modülü
#önce import edilmeli
# os.path.abspath : Eğer bir dosyanın en genel biçimde dosya yolunu edinmek istiyorsanız os.path.abspath fonksiyonunu kullanabilirsiniz.
# os.path.exists: Eğer bir dosyanın belirttiğiniz dosya yolunda var olup olmadığını kontrol etmek istiyorsanız os.path.exists fonksiyonunu kullanabilirsiniz.
# os.path.isdir : Elde ettiğiniz metinsel verinin bir dosya yolu(Ör: C:/Metinler) olup olmadığını kontrol etmek isterseniz os.path.isdir fonksiyonunu kullanabilirsiniz.
# os.path.isfile : Elde ettiğiniz verinin bir dosya(Ör: C:/Metinler/deneme.txt) olup olmadığını kontrol etmek isterseniz os.path.isfile fonksiyonunu kullanabilirsiniz.
# os.listdir : Eğer belirli bir dosya yolundaki dosyaların isimlerini almak istiyorsanız os.listdir fonksiyonunu kullanabilirsiniz.

#Dosyayı okuma
dosya=open("dosyaislemleri1.txt","r",encoding="utf-8")
for i in dosya:
    print(i)
dosya.close()

