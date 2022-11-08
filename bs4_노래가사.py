import requests
from bs4 import BeautifulSoup

#title = "리무진"#input("title: ")
#artist = "비오"#input("artist: ")
title = "love dive"
artist = "아이브(ive)"

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sug.pre&fbm=1&acr=1&acq=tlsghemd+rktk&qdt=0&ie=utf8&query=' + artist  + '+' + title + '+' + '가사'

response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    lyrics = soup.select_one('div.intro_box > p')
    if lyrics == None:
        # 원래 유형의 결과가 나오면 처리 하는 부분(첫번째 스크린샷)
        lyrics = soup.select_one('div.lyrics_txt')
        if lyrics == None:
            #세번째 유형일때 처리 하는 부분
            lyrics = soup.select_one('div.text_expand > span.desc')
            if lyrics == None:
                print("찾으시는 곡의 가사 정보를 찾을 수 없습니다.")
            else:
                lines = lyrics.contents

                while len(lines) > 1:
                    if len(lines) == 2:
                        print(lines[0].get_text())
                        lines = lines[1].contents
                    elif len(lines) > 2:
                        for i in range(0, len(lines), 2):
                            print(lines[i])
                        break
        else:
            lines = lyrics.select('p')
            for line in lines:
                print(line.get_text())
    else:
        #두번째 유형의 결과가 나오면 처리 하는 부분
        lines = lyrics.contents

        while len(lines) > 1:
            if len(lines) == 2:
                print(lines[0].get_text())
                lines = lines[1].contents
            elif len(lines) > 2:
                for i in range(0, len(lines), 2):
                    print(lines[i])
                break
else :
    print(response.status_code)