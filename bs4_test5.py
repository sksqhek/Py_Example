from bs4 import BeautifulSoup

html = '''
<ol>
    <li>NEVER - 국민의 아들</li>
    <li>SIGNAL - TWICE</li>
    <li>LONELY - 씨스타</li>
    <li>I LUV IT - PSY</li>
    <li>New Face - PSY</li>
</ol>
'''

soup = BeautifulSoup(html, 'html.parser')
for tag in soup.select('li'):
    print(tag.text)
