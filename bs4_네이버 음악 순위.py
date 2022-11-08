from bs4 import BeautifulSoup
import urllib.request

print('  ○>> #오늘의 #음원 #종합 #TOP10 \n')
webpage = urllib.request.urlopen('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%9D%8C%EC%9B%90%EC%B0%A8%ED%8A%B8&oquery=%EB%A9%9C%EB%A1%A0%EC%B0%A8%ED%8A%B8&tqi=UrZ0HsprvN8ssK5ZP%2BsssssstVh-314088')

toptenlist = []
artistlist = []

Rank = 10
soup = BeautifulSoup(webpage, 'html.parser')

for a in soup.select('.album_info'):#음악 한개 단위로 읽기
    info = a.select('a')#제목 가수를 얻어오기

    for i in range(len(info)):#테그를 값만 추출해서 다시 저장
        info[i] = info[i].text

    toptenlist.append(info[0])#제목
    artistlist.append(info[2:])#가수 여러명 일경우 때문에 리스트 사용

for i in range(Rank):
    print(' - %2d위  : %s - %s'%(i+1, artistlist[i], toptenlist[i]))