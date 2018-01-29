import unittest
import requests
from requests.auth import HTTPBasicAuth
import HtmlTestRunner

class MainSite(unittest.TestCase):
        
        def test_Main_page(self):
            Link = requests.get("https://preprod.fashion-flash.de", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)

        def test_Unser_Event_Konzept(self):
            Link = requests.get("https://preprod.fashion-flash.de/wie", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)

        def test_uber_uns(self):
            Link = requests.get("https://preprod.fashion-flash.de/uber_uns", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)


        def test_kooperationen(self):
            Link = requests.get("https://preprod.fashion-flash.de/kooperationen", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)

        def test_presse(self):
            Link = requests.get("https://preprod.fashion-flash.de/presse", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)

        def test_jobs(self):
            Link = requests.get("https://preprod.fashion-flash.de/jobs", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)

        def test_Main_kontakt(self):
            Link = requests.get("https://preprod.fashion-flash.de/kontakt", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)

        def test_Impressum(self):
            Link = requests.get("https://preprod.fashion-flash.de/impressum#impressum", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)

        def test_agb(self):
            Link = requests.get("https://preprod.fashion-flash.de/agb#agb", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)

        def test_Main_page(self):
            Link = requests.get("https://preprod.fashion-flash.de/datenschutzerklarung#daten", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)

        def test_tickets(self):
            Link = requests.get("https://preprod.fashion-flash.de/tickets", auth=HTTPBasicAuth('', ''))
            Status = Link.status_code
            self.assertEqual(Status,200)


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='example_dir'))
