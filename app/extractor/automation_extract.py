# Autor Odair Rodrigues Junior Linkdin: https://www.linkedin.com/in/odair-rodrigues-junior/
import pandas as pandas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Extract_data_gov:
    def __init__(self):
        '''settings for run selenium'''
        #for using selenium need chrome driver (Documetation) -->   https://chromedriver.chromium.org/downloads
        #question on how to use the Selenium (tutorial) --> https://www.javatpoint.com/selenium-python
        

        self.driver_Chrome = 'app/sources/chromedriver'
        chrome_options = webdriver.ChromeOptions()
        prefs = {
                "safebeowsing.enabled" :True,
                "download.prmpt_for_download": False

        }
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome()

    def selenium_opening_page(self):
        url_Gov = 'https://dados.gov.br/dataset/marcelo-geraldo-batista'
        self.driver.get(url=url_Gov)
        time.sleep(40)
    
    def run(self):
        self.selenium_opening_page()







        


