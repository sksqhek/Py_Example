import requests
from bs4 import BeautifulSoup
from csv import writer

'''
# page 2
https://vn.indeed.com/jobs?q=python+developer&l=H%C3%A0+N%E1%BB%99i&start=10
# page 3
https://vn.indeed.com/jobs?q=python+developer&l=H%C3%A0+N%E1%BB%99i&start=20
'''
url = 'https://vn.indeed.com/jobs?q=python+developer&l=H%C3%A0+N%E1%BB%99i'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('div', class_='slider_container')

salary = ''

with open('indeed_jobs.csv', 'w', newline='', encoding='utf-8') as f:
    thewriter = writer(f)
    header = ['Title', 'Company', 'Salary']
    thewriter.writerow(header)

    for result in results:
        try:
            title = result.find('h2', class_='jobTitle').find_all('span')[1].text.strip()
        except:
            title = result.find('h2', class_='jobTitle').find_all('span')[0].text.strip()
        company = result.find('span', class_='companyName').text.strip()
        salary1 = result.find('span', class_='salary-snippet')
        if salary1:
            salary = salary1.text.strip()
        else:
            salary = 'Not mentioned!'
        jobinfo = [title, company, salary]
        thewriter.writerow(jobinfo)
