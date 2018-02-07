import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time

class TestM(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("https://preprod.fashion-flash.de/")
		time.sleep(5)


	def test_get_tickets(self):
		driver = self.driver
		event = ['Köln']
		tickets = driver.find_element_by_xpath('//*[@id="square_ticket_block"]/a')
		eventsList = driver.find_element_by_link_text(event[0]) #driver.execute_script("arguments[0].click();", tickets)
		eventsList.click()
		time.sleep(3)
		url1 = driver.current_url
		
		element = driver.find_element_by_css_selector("div.col-xs-12.citySelect.splitText")

		if event[0] in element.text:
			print('Passed')
		else:
			print('Failed')
		
		vorname = driver.find_element_by_id('tickets_firstName')
		email = driver.find_element_by_id('tickets_email')
		plz = driver.find_element_by_id('tickets_plz')
		phone = driver.find_element_by_id('tickets_phone')

		

		vorname.send_keys('Marky')
		email.send_keys('aily.teamqa+2004@gmail.com')
		plz.send_keys('45423')

		check = driver.find_element_by_id('label-condition')
		driver.execute_script("arguments[0].click();", check)

		button = driver.find_element_by_id('get-ticket')
		button.click()
		time.sleep(2)

		resend = driver.find_element_by_id('resend-ticket')
		
		if resend.is_displayed():
			driver.execute_script("arguments[0].click();", resend)
			print('resend')
		else:
			print('does not resend')
		time.sleep(3)
		url2 = driver.current_url


		self.assertEqual(url1,"https://preprod.fashion-flash.de/tickets")
		self.assertEqual(url2,"https://preprod.fashion-flash.de/reg/success")




	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()
