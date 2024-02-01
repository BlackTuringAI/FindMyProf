import requests
import re
import csv
from bs4 import BeautifulSoup

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
   def __init__(self, eng_name, degree, education, unit, phone, email, room):
       self.eng_name = eng_name
       self.degree = degree
       self.education = education
       self.unit = unit
       self.phone = phone
       self.email = email
       self.room = room



for link in link_list:
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    eng_name = ""
    education = ""
    unit = ""
    phone = ""
    email = ""
    room = ""

    #English Name
    temp1 = soup.find_all('span', class_='name-eng')
    match1 = re.search('\n(.*?)\n', str(temp1))
    if match1:
        eng_name = (match1.group(1)).strip()

    #Education
    temp3 = soup.find_all('div', class_='edu')
    edu1 = re.search("PhD\sin\s[A-Za-z\s]+", str(temp3))
    edu2 = re.search(r'[A-Za-z\s]+,\s+\d+', str(temp3))
    if edu1 and edu2:
        degree = edu1.group(0).strip()
        education = edu2.group(0).strip()


    #Unit
    temp4 = soup.find_all('span', class_='unit')
    match4 = re.search('\n(.*?)\n', str(temp4))
    if match4:
        unit = (match4.group(1)).strip()

    #Post
    temp5 = soup.find_all('div', class_='post')

    #Phone
    temp6 = soup.find_all('ul', class_='fa-ul')
    match6 = re.search(r'\(\d+\)\s\d+\s\d+', str(temp6))
    if match6:
        phone = (match6.group(0)).strip()

    #Email
    email = link.split("-")[-1] + "@ust.hk"

    #Room
    temp8 = soup.find_all('a')
    match8 = re.search("Room\s\w+", str(temp8))
    if match8:
        room = (match8.group(0)).strip()

    pro_temp = Pro(eng_name, degree, education, unit, phone, email, room)
    professor_list.append(pro_temp)

# Specify the desired CSV file path
csv_file = "output.csv"

# Define the CSV file header
fieldnames = ["English Name","Degree", "Education", "Unit", "Phone", "Email", "Room"]

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
            "Room": pro.room
        })


