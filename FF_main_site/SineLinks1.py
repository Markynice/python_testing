from bs4 import BeautifulSoup
from urllib.request import urlopen	
import re


html_page = urlopen("https://preprod.fashion-flash.de")
ListOfEvents = []
soup = BeautifulSoup(html_page, 'lxml')
BlockDiv = soup.find('tbody', {'class':'visibleTable'})

EventName = BlockDiv.findAll('a', {'class':'wa-link tableGetTickt tickTable', 'href':True})

for name in EventName:
	ListOfEvents.append(name.string)