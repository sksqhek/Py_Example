import requests
from bs4 import BeautifulSoup

res = requests.get('http://corners.auction.co.kr/corner/categorybest.aspx?catetab=9')
soup = BeautifulSoup(res.content, 'html.parser')

data = soup.select('div.info')
for index, item in enumerate(data):
    title = item.select_one('em a')
    price = item.select_one('span')
    print(str(index + 1) + '.' , title.get_text(), price.get_text())
