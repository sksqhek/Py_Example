from bs4 import BeautifulSoup
import requests

url = 'https://www.thoughtco.com/a-to-z-chemistry-dictionary-4143188'
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

articles = soup.findAll("p", {"class":"comp mntl-sc-block mntl-sc-block-html"})
for article in range(1,len(articles)):
    temp = articles[article].text
    print(temp)
