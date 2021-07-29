import requests
from bs4 import BeautifulSoup
import re

url = 'https://m.blog.naver.com/PostView.nhn?blogId=atsuki42&logNo=220994575513&proxyReferer=https:%2F%2Fwww.google.com%2F'
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

links = soup.find_all("span")

data = []

dic = {}
key = ''
prev = ''

def specialProcess(startChar , endChar):
    str = result.text

    try:
        f = str.index(startChar)
        str = str[f:]
        e = str.index(endChar)
        str = str[:e+1]

        strlist = re.findall(">(.*?)<", str)

        for s in strlist:
            if s != '':
                dic[startChar].append(s)

        for d in dic[startChar]:
            if d == ' ':
                dic[startChar].remove(d)
    except:
        pass


for link1 in links:
    data.append(link1.get_text())#테그안에 있는 문자열만 저장


front = data.index("<ㄱ>")#데이터 시작지덤 찾기
data = data[front:]

rear = data.index("흠집")#데이터 끝부분 찾기
data = data[:rear+1]

prevkey = ''
for d in data:
    if len(d) == 3 and d[0] == '<' and d[2] == '>':#키문자를 찾으면
        key = d[1:2]#키저장

        # 일반적이지 않은 테그로된 부분을 찾으면(이전 키로 읽어온것이 없으면)
        if prevkey != '' and len(dic[prevkey]) == 1:
            specialProcess(prevkey, key)

        dic[key] = []
        prevkey = key
    else:
        dic[key].append(d)#사전에 저장

while True:
    key = input(">")
    x = dic.get(key, 0)
    if x == 0:
        print('없는 키입니다')
        continue

    for out in dic[key]:
        print(out)

    print()

