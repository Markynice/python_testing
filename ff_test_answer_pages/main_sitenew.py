import unittest
import requests
from requests.auth import HTTPBasicAuth
import SineLinks


class MainSite(unittest.TestCase):
<<<<<<< HEAD

		def test_Main_page(self):

			for href in SineLinks.links:
				Link = requests.get(href, auth=HTTPBasicAuth('aily.team', 'e,theyc33'))
				Status = Link.status_code
				if Status == 200:
					print(href+" :Passed")
				else:
					print(href+" :Faild. Reason "+str(Status)+"!=200")
=======
	ArrayLink = ["https://preprod.fashion-flash.de","https://preprod.fashion-flash.de/wie","https://preprod.fashion-flash.de/kooperationen","https://preprod.fashion-flash.de/presse","https://preprod.fashion-flash.de/jobs","https://preprod.fashion-flash.de/kontakt"]
	def test_Main_page(self):
		for Links in ArrayLink:
			Link = requests.get(Links, auth=HTTPBasicAuth('', ''))
			Status = Link.status_code
			self.assertEqual(Status,200)
>>>>>>> 0f623b5d745ecdd64e8bb02e0607c1cd4440b617

if __name__ == "__main__":
	unittest.main()
