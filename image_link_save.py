import urllib.request

file = open("메모장.txt","r")

for link in file.readlines():
    tok = link.split(",")
    tok[1] = tok[1].strip('\n')
    urllib.request.urlretrieve(tok[0], tok[1]+".jpg")
    print(tok)

#url = "https://cdn.ownerclan.com/i_9LOcRT6oVujdssAOehCb1glPErM7hGcamBAzRtV6Q/marketize/auto/as/v1.jpg"
#savename = 'save_by_urllib.jpg'

#urllib.request.urlretrieve(url,savename)
#print("저장완료")