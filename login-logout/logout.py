import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogout(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_logout_successfully(self): 
        # steps
        browser = self.browser 
        browser.get("https://itera-qa.azurewebsites.net/Login") 
        time.sleep(3)
        browser.find_element(By.ID,"Username").send_keys("muthi4&c7") 
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("muthia16") 
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)
        browser.find_element(By.CSS_SELECTOR,"#navbarColor01 > form > ul > li:nth-child(2) > a").click()
        time.sleep(1)
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()