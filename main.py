from bs4 import BeautifulSoup
import requests
#
# with open("serebii.html",'r',) as serebii_file: #analisando pagina inicial pelo arquivo serebii.html
#     content = serebii_file.read()
#     #print(content)
#     soup = BeautifulSoup(content,'lxml')
#     #print(soup.prettify())
#     tag = soup.find_all("h2")
#     for i in tag:
#        print(i.text)

dex= requests.get('https://www.serebii.net/pokedex/fire.shtml')
#print(dex.text)
soup = BeautifulSoup(dex.text, "lxml")#.text necessario
infos = soup.find_all(class_="fooinfo")
textos_li= soup.find_all("li")

for i in infos:
    
        print(i.text.replace("\n"," "))  #mostra todos os pokemon de fogo da gen 1 com os stats sem os \n