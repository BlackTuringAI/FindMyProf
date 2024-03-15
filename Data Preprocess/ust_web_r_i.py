import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import pandas as pd

df = pd.read_csv('output.csv')
r_i = []
tempp = []
# Make a GET request to the website
url = 'https://facultyprofiles.hkust.edu.hk/facultylisting.php'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the professors' names and email addresses
professors = soup.find_all('div', class_='results-body')

link_list = []
for professor in professors:
    links = professor.find_all('span', class_='mt-auto ml-auto p-2')
    for link in links:
        match = re.search('href="(.*?)"', str(link))
        if match:
            extracted_string = match.group(1)
            temp = "https://facultyprofiles.hkust.edu.hk/" + extracted_string
            link_list.append(temp)
print(len(link_list))
professor_list = []

for link in link_list:
    response = requests.get(link)
    html = response.content

    # 创建解析器并解析HTML文档
    parser = etree.HTMLParser()
    tree = etree.fromstring(html, parser)

    # 使用XPath表达式获取所有内容
    i=1
    content_list = []
    while True:
        try:
            xpath_expression = "/html/body/div[2]/div[2]/div/div[2]/div[3]/div[1]/div/div/div/ul/li["+ str(i) +"]/text()"
            if len(tree.xpath(xpath_expression)) != 0:
                content_list.append(tree.xpath(xpath_expression))
            else:
                break
            i += 1
        except:
            break

    for content in content_list:
        print(str(content[1])[30:-26])
        tempp.append(str(content[1])[30:-26])
    temp = ''
    for j in range(1,i):
        if j == 1:
            temp += tempp[-j]
        else:
            temp += ', '
            temp += tempp[-j]
    r_i.append(temp)

df["Research Interest"] = r_i
df.to_csv('output_update.csv', index=False)