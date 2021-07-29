import requests
from bs4 import BeautifulSoup

url = 'https://talk.op.gg/s/lol/all?sort=top&page=5'
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")
sublink = []
links = soup.find_all("div", {"class":"article-list-item__content"})

for link1 in links:
    a = link1.find("a")["href"]
    print(a)