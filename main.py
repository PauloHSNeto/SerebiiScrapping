from bs4 import BeautifulSoup
import requests
#
# with open("serebii.html",'r',) as serebii_file:
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
charizard = infos.find("")
for i in infos:
    print(i.text)  #mostra todos os pokemon de fogo da gen 1 com os stats