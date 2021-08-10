html_doc = """
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>İlk web sayfam</title>
</head>
<body>

    <h1 id="header">
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
        <h2>
            Django
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""
from bs4 import BeautifulSoup
#Parse ettik. (html.parser-lxml-lxml-xml-html5lib)
soup=BeautifulSoup(html_doc,"html.parser")
#Kodları daha anlaşılabilir hale getirdik.
result=soup.prettify()
#Karşılaştığımız ilk başlığı aldık
result=soup.title
#Karşılaştığımız ilk head'i aldık
result = soup.head
#Karşılaştığımız ilk body'i aldık
result = soup.body
#Title'ın adını aldık. Metnini değil. title1,title2 gibi.
result=soup.title.name
#Başlığın metnini aldık.
result=soup.title.string
#h1'i aldık
result = soup.h1
#h2'yi aldık
result = soup.h2
#h2'nin adını aldık. Metnini değil.
result = soup.h2.name
#h2 ve h1'in metnini aldık
result = soup.h2.string
result = soup.h1.string
#h2 başlığına sahip her şeyi aldık
result = soup.find_all('h2')
#h2 başlığına sahip elemanları tek tek alma
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1]
#div için aynı işlemler
result = soup.div
result = soup.find_all('div')[1]
#Seçtiğimizin içerisinden de seçim  yapabiliyoruz.
result = soup.find_all('div')[1].ul.find_all('li')
#ilk div'in altındakileri verir.
result = soup.div.findChildren()
#Sonraki ve önceki div'lere ulaşma
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()
#'a' içerenleri bulma
result = soup.find_all('a')
#'a' içerenleri yazdırdık
for link in result:
    print(link)
#'a' içeren href'leri aldık
"""for link in result:
    print(link.get('href'))"""
#İçerdiği tüm metinleri alma
result=soup.get_text()
#Metni değiştirme
soup.title.string="GALATASARAY"
result=soup.title.string
print(result)