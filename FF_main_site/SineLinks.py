from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
 
html_page = urlopen("https://ems.aily.team/")
soup = BeautifulSoup(html_page)
links = []
ErrorLink = 'https://www.youtube.com/channel/UCoNzxqor_7Lyiyo_tNhJh8g/featured, https://www.facebook.com/FashionFlashEvent, https://www.instagram.com/fashionflashevent/, https://bit.ly/FashionFlashWhatsApp'
 
for link in soup.findAll('a'):
	if link.get('href') not in ErrorLink:
		links.append('https://fashion-flash.de'+link.get('href'))
 
print(links)