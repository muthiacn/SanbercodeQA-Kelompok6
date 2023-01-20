import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_login_successfully(self): 
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

    def test_login_blank_field(self): 
        browser = self.browser 
        browser.get("https://itera-qa.azurewebsites.net/Login") 
        time.sleep(3)
        browser.find_element(By.ID,"Username").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)

        response_message = browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[5]/td/label").text
        self.assertEqual(response_message, 'Wrong username or password')

    def test_login_invalid_password(self): 
        browser = self.browser 
        browser.get("https://itera-qa.azurewebsites.net/Login") 
        time.sleep(3)
        browser.find_element(By.ID,"Username").send_keys("muthi4&c7") 
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("muthia17")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)

        response_message = browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[5]/td/label").text
        self.assertEqual(response_message, 'Wrong username or password')

    def test_login_invalid_username(self): 
        browser = self.browser 
        browser.get("https://itera-qa.azurewebsites.net/Login") 
        time.sleep(3)
        browser.find_element(By.ID,"Username").send_keys("muthi4&c6") 
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("muthia17")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(1)

        response_message = browser.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[5]/td/label").text
        self.assertEqual(response_message, 'Wrong username or password')
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()