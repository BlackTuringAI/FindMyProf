import requests
import re
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def scrape_citation(prof, school):
    webdriver_service = Service('D:/pycharm/pythonProject1/chromedriver.exe')
    webdriver_service.start()

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("window-size=1920,1080")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    driver.get('https://www.google.com/')

    search_input = driver.find_element(By.NAME, 'q')
    search_input.send_keys(f'{prof} {school} google scholar')
    search_input.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'search')))

    try:
        for i in range(1, 11):
            temp_str = '//*[@id="rso"]/div[' + str(i) + ']/div/div/div[1]/div/div/span/a'
            link = driver.find_element(By.XPATH, temp_str)
            if "scholar.google.com" in link.get_attribute("href"):
                link.click()
                break
        table = driver.find_element(By.XPATH, '//*[@id="gsc_rsb_st"]')
        rows = table.find_elements(By.TAG_NAME, 'tr')

        data = [row.text for row in rows]
        data = [i.split(" ") for i in data]
        data[0] = ["Time", "All", "Last 3 years"]
        print(data)
        df = pd.DataFrame(data)
        driver.quit()
    except:
        driver.quit()
        data = [['All', 'Since 2019'],
                ['Citations', 0, 0],
                ['h-index', 0, 0],
                ['i10-index', 0, 0]]

        df = pd.DataFrame(data)
        return data
    return data


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

class Pro(object):
   def __init__(self, eng_name, education, unit, phone, email, room, citation, h_index, i10_index):
       self.eng_name = eng_name
       self.degree = degree
       self.education = education
       self.unit = unit
       self.phone = phone
       self.email = email
       self.room = room
       self.citation = citation
       self.h_index = h_index
       self.i10_index = i10_index

for link in link_list:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    eng_name = ""
    education = ""
    unit = ""
    phone = ""
    email = ""
    room = ""
    citation = ""
    h_index = ""
    i10_index = ""

    # English Name
    temp1 = soup.find_all('span', class_='name-eng')
    match1 = re.search('\n(.*?)\n', str(temp1))
    if match1:
        eng_name = (match1.group(1)).strip()

    # Education
    temp3 = soup.find_all('div', class_='edu')
    edu1 = re.search("PhD\sin\s[A-Za-z\s]+", str(temp3))
    edu2 = re.search(r'[A-Za-z\s]+,\s+\d+', str(temp3))
    if edu1 and edu2:
        degree = edu1.group(0).strip()
        education = edu2.group(0).strip()


    # Unit
    temp4 = soup.find_all('span', class_='unit')
    match4 = re.search('\n(.*?)\n', str(temp4))
    if match4:
        unit = (match4.group(1)).strip()

    # Post
    temp5 = soup.find_all('div', class_='post')

    # Phone
    temp6 = soup.find_all('ul', class_='fa-ul')
    match6 = re.search(r'\(\d+\)\s\d+\s\d+', str(temp6))
    if match6:
        phone = (match6.group(0)).strip()

    # Email
    email = link.split("-")[-1] + "@ust.hk"

    # Room
    temp8 = soup.find_all('a')
    match8 = re.search("Room\s\w+", str(temp8))
    if match8:
        room = (match8.group(0)).strip()

    # citation h_index and i10 index
    temp_ = scrape_citation(eng_name, "HKUST")
    print(temp_)
    citation = temp_[1][2]
    if len(temp_[2]) > 1:
        h_index = temp_[2][-1]
        i10_index = temp_[3][-1]
    else:
        h_index = 0
        i10_index = 0

    pro_temp = Pro(eng_name, education, unit, phone, email, room, citation, h_index, i10_index)
    professor_list.append(pro_temp)


# Specify the desired CSV file path
csv_file = "output.csv"

# Define the CSV file header
fieldnames = ["English Name","Degree", "Education", "Unit", "Phone", "Email", "Room", "Citation(last 3yrs)", "h_index(last 3yrs)", "i10_index(last 3yrs)"]

# Open the CSV file in write mode and write the objects' data
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data for each Pro object in the list
    for pro in professor_list:
        education = pro.education.replace('\n', ' ')
        writer.writerow({
            "English Name": pro.eng_name,
            "Degree": pro.degree,
            "Education": pro.education,
            "Unit": pro.unit,
            "Phone": pro.phone,
            "Email": pro.email,
            "Room": pro.room,
            "Citation(last 3yrs)": pro.citation,
            "h_index(last 3yrs)": pro.h_index,
            "i10_index(last 3yrs)": pro.i10_index
        })

