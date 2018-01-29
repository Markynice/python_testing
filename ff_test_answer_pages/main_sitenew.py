import unittest
import requests
from requests.auth import HTTPBasicAuth


class MainSite(unittest.TestCase):
	ArrayLink = ["https://preprod.fashion-flash.de","https://preprod.fashion-flash.de/wie","https://preprod.fashion-flash.de/kooperationen","https://preprod.fashion-flash.de/presse","https://preprod.fashion-flash.de/jobs","https://preprod.fashion-flash.de/kontakt"]
	def test_Main_page(self):
		for Links in ArrayLink:
			Link = requests.get(Links, auth=HTTPBasicAuth('', ''))
			Status = Link.status_code
			self.assertEqual(Status,200)

if __name__ == "__main__":
	unittest.main()
