from bs4 import BeautifulSoup
from urllib.request import urlopen

# Scrap all the uoft majors: http://www.artsci.utoronto.ca/current/program/enrolment-instructions/program-codes-contacts

soup = BeautifulSoup(urlopen('http://www.artsci.utoronto.ca/current/program/enrolment-instructions/program-codes-contacts'))

print(soup.find_all('td'))

