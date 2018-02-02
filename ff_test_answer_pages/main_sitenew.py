import unittest
import requests
from requests.auth import HTTPBasicAuth
import SineLinks


class MainSite(unittest.TestCase):

		def test_Main_page(self):

			for href in SineLinks.links:
				Link = requests.get(href, auth=HTTPBasicAuth('aily.team', 'e,theyc33'))
				Status = Link.status_code
				if Status == 200:
					print(href+" :Passed")
				else:
					print(href+" :Faild. Reason "+str(Status)+"!=200")

if __name__ == "__main__":
	unittest.main()