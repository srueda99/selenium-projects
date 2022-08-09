# Imports
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class HelloWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
    
    def testNetflix(self):
        # Go to Netflix.com and click on Sign In
        self.driver.get('https://www.netflix.com')
        signIn_Btn = self.driver.find_element(by = By.XPATH, value = '//*[@id="appMountPoint"]/div/div/div/div/div/div[1]/div/a')
        signIn_Btn.click()
        # Put the username and password for the Netflix account
        username = self.driver.find_element(by = By.ID, value = 'id_userLoginId')
        password = self.driver.find_element(by = By.ID, value = 'id_password')
        signIn_Btn = self.driver.find_element(by = By.XPATH, value = '//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
        # Fill the values
        username.send_keys('s_rueda_m@hotmail.com')
        password.send_keys('Netflix_family123')
        signIn_Btn.click()
        # Choose a profile to watch
        profile = self.driver.find_element(by = By.XPATH, value = '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a')
        profile.click()
        # Select the fist recommendation
        media = self.driver.find_element(by = By.ID, value = 'title-card-1-0')
        media.click()
        start_Btn = self.driver.find_element(by = By.XPATH, value = '//*[@id="appMountPoint"]/div/div/div[1]/div[2]/div/div[1]/div[4]/div/div[1]/div[1]/a/button')
        start_Btn.click()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'netflix-login'))