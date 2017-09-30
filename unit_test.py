from selenium import webdriver
import unittest, time, re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


class NewTest(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []

    def test_new(self):
        fox = webdriver.Firefox()
        fox.get("URL")
        try:
            element = WebDriverWait(ff, 10).until(EC.presence_of_element_located((By.ID, "insert-point")))
            element.click()
        finally:
            fox.quit



    def tearDown(self):
        self.selenium.stop()
      
        self.assertEqual([], self.verificationErrors)
