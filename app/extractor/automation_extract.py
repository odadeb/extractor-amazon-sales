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
                "download.default_directory": r"C:\Users\odair\OneDrive\Ambiente de Trabalho\Study\P01\extractor-public-transport-brazil\app\sources\\", # IMPORTANT - ENDING SLASH V IMPORTANT
                "safebeowsing.enabled" :True,
                "download.prmpt_for_download": False

        }
        chrome_options.add_experimental_option("prefs",prefs)
        self.driver = webdriver.Chrome()

    def selenium_opening_page(self):
        url_Gov = 'https://dados.gov.br/dataset/marcelo-geraldo-batista'
        self.driver.get(url=url_Gov)
        time.sleep(4)
        button_signInSubmit = self.driver.find_element(By.XPATH,'//*[@id="dataset-resources"]/ul/li[1]/div/a')
        button_signInSubmit.click()
        time.sleep(3)
        button_ir_para_recurso = self.driver.find_element(By.XPATH,'//*[@id="dataset-resources"]/ul/li[1]/div/ul/li[2]/a')
        button_ir_para_recurso.click()
        time.sleep(10)
        self.driver.close()
    
    def run(self):
        
        self.selenium_opening_page()







        


