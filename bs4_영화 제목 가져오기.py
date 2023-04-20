from urllib import request
from bs4 import BeautifulSoup

text = request.urlopen('http://www.cgv.co.kr/movies')
soup = BeautifulSoup(text, 'html.parser')
dataList = soup.select('div.box-contents > a > strong.title')

number = 1
for x in dataList[:5]:
    print(number, ":", x.string)
    number += 1