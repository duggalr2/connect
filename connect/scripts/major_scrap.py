from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3

# Scrap all the uoft majors: http://www.artsci.utoronto.ca/current/program/enrolment-instructions/program-codes-contacts

url = 'http://www.artsci.utoronto.ca/current/program/enrolment-instructions/program-codes-contacts#M'
soup = BeautifulSoup(urlopen(url))
table = soup.findAll('table')[2]
rows = table.find_all('tr')
# rows = [sing_row.find_all('td') for sing_row in rows if len(sing_row.find_all('td')) > 1]
list_of_majors = []
for sing_row in rows:
    if len(sing_row.find_all('td')) > 1:
        new_row = sing_row.find_all('td')
        major = new_row[1].text
        major = major.replace('\n', '')
        major = major.replace('\r', '')
        major = major.replace('  ', '')
        list_of_majors.append(major)


conn = sqlite3.connect('/Users/Rahul/Desktop/Side_projects/project1/db.sqlite3', check_same_thread=False)
c = conn.cursor()
id = 0
for major in list_of_majors:
    c.execute("INSERT INTO connect_major VALUES (?, ?)",
                      (id, major))
    conn.commit()
    id += 1
