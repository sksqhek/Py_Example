import requests
from bs4 import BeautifulSoup
import urllib.request

opener=urllib.request.build_opener()

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]

urllib.request.install_opener(opener)

for i in range(1, 623):

    url = 'https://truemoa2.com/bbs/board.php?bo_table=photobbs&page=' + str(i)
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    links = soup.find_all("li", {"class":"td wr-subject"})

    try:
        for link1 in links:
            a = link1.find("a")["href"]
            sub_result = requests.get(a)
            sub_soup = BeautifulSoup(sub_result.text, "html.parser")

            sub_links = sub_soup.find_all("div", {"class": "f-content"})

            for sub_link1 in sub_links[0].select('p'):
                sub_a = sub_link1.find('img')['src']
                print(sub_a)

                originNames = sub_a.split("/")
                renameFile = originNames[len(originNames) - 1]

                urllib.request.urlretrieve(sub_a, f'./pic/'+renameFile)
    except:
        pass