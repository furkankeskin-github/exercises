from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Tarayıcı seçme (Eğer aynı klasörde değilse tarayıcının konumunu parantez içerisinde yazmalısın)
browser=webdriver.Chrome()

#Siteye Gitme
browser.get('http://google.com')

#Tarayıcı başlığının google olup, olmadığını kontrol eder. Eğer değilse hata verir.
assert 'Google' in browser.title

#Sayfa yüklenene kadar bekleme
time.sleep(2)

#Tarayıcıyı tam ekran yapma
browser.maximize_window()

#Arama kutusunun ve arama butonunun yolunu bulduk
sorgukutusu=browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
aramabutonu=browser.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")

#Aramaya gönderilecek harfleri gönderme ve arama yapma
sorgukutusu.send_keys('Galatasaray'+Keys.ENTER)
#aramabutonu.click() ile arama butonuna da tıklayabiliriz

#Ekran Görüntüsü alma ve isimlendirme
#browser.save_screenshot("googlearamasonucları.png")

#İleri Geri Gitme
# driver.back()
# driver.forward()

#Tarayıcıyı kapatma
time.sleep(2)
browser.close()