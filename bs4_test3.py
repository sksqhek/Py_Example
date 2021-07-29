from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://covid19.ei.go.kr/eisp/eih/es/cv/retrieveCv604Info.do")

bsObject = BeautifulSoup(html, "html.parser")

#질문 부분 추출
question = bsObject.find_all("h4", {"class":"titlex"})
listq = []
for q in question:
    listq.append(q.get_text())#질문을 리스트에 저장

#답변 부분 추출
answer = bsObject.find_all("div",{'class':'cont1'})
lista = []
for a in answer:
    lista.append(a.find('li').get_text())#답변을 리스트에 저장


#저장된 질문과 답변을 출력
for i in range(len(listq)):
    print(listq[i])
    print(lista[i])
    print()