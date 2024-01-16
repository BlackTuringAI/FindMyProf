import requests
from bs4 import BeautifulSoup
import csv

url = 'https://facultyprofiles.hkust.edu.hk/facultylisting.php'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
professors = soup.find_all('span', {'class': 'name-eng'})

with open('professors.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Professor', 'URL'])
    for professor in professors:
        url = professor.find('a')['href']
        writer.writerow([professor.text.strip(), url])

