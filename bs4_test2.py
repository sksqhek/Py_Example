import requests
from bs4 import BeautifulSoup

url = 'https://m.blog.naver.com/decilion2/221087273324'
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

links = soup.find_all("span")

data = []

for link1 in links:
    data.append(link1.get_text())#테그안에 있는 문자열만 저장


front = data.index("가/")#데이터 시작지덤 찾기
data = data[front:]

rear = data.index("힘센바위턱트로그")#데이터 끝부분 찾기
data = data[:rear+1]

dic = {}
key = ''
prev = ''

for d in data:
    if prev == d or len(d) == 0:#똑같은 문자열이 나오거나 없는 문자열이면
        continue#건너뛰기

    if len(d) == 2 and d[1] == '/':#키문자를 찾으면
        key = d[:1]#키저장
        dic[key] = []
        prev = key
    else:
        if len(d) == 1:#읽어온 문자열이 한개 라면
            continue#건너뛰기
        else:
            dic[key].append(d)#사전에 저장
            prev = d#똑같은 문자열이 나오나 검사 하기 위해

while True:
    key = input(">")
    x = dic.get(key, 0)
    if x == 0:
        print('없는 키입니다')
        continue

    for out in dic[key]:
        print(out)

    print()

