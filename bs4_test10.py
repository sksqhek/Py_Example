import requests
from bs4 import BeautifulSoup

pic_links=[]

for i in range(2, 54):
    res = requests.get('https://asiansister.com/_page'+ str(i))
    soup = BeautifulSoup(res.content, 'html.parser')

    answer = soup.find_all("div",{'class':'itemBox'})
    for link1 in answer:
        a = link1.find("a")["href"]
        pic_links.append(a)

fp = open("pic_links.txt","w")

for i in range(len(pic_links)):
    fp.write("https://asiansister.com/" + pic_links[i] + "\n")
