import requests
from bs4 import BeautifulSoup

params = {
    'q': 'EPA:BRNTB',
    'startdate': 'Jan 01, 2016',
    'enddate': 'Jun 02, 2016',
}
#response = requests.get('https://www.google.com/finance/historical', params=params)
#print(response.request.url)

text = '''<div id=prices class="gf-tablewrapper sfe-break-bottom-16">
<table class="gf-table historical_price">
    <tr class=bb>
        <th class="bb lm lft">Date
        <th class="rgt bb">Open
        <th class="rgt bb">High
        <th class="rgt bb">Low
        <th class="rgt bb">Close
        <th class="rgt bb">Volume
    <tr>
        <td class="lm">Feb 28, 2014
        <td class="rgt">100.71
        <td class="rgt">100.71
        <td class="rgt">100.71
        <td class="rgt rm">0
</table>'''


#html = response.text
html = text
soup = BeautifulSoup(html, 'html.parser')  # 여기 봐주세요)
for tr_tag in soup.select('#prices > table > tr'):
    row = [td_tag.text.strip() for td_tag in tr_tag.select('th, td')]
    print(row)
