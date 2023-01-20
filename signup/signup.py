import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_sign_up_successfully(self): 
        browser = self.browser 
        browser.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser") 
        time.sleep(3)
        browser.find_element(By.ID,"FirstName").send_keys("Kelompok 6") 
        time.sleep(1)
        browser.find_element(By.ID,"Surname").send_keys("Batch 41") 
        time.sleep(1)
        browser.find_element(By.ID,"E_post").send_keys("kelompok.6@gmail.com") 
        time.sleep(1)
        browser.find_element(By.ID,"Mobile").send_keys("0987654321") 
        time.sleep(1)
        browser.find_element(By.ID,"Username").send_keys("kelompok6b41") 
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("kelompok6")
        time.sleep(1)
        browser.find_element(By.ID,"ConfirmPassword").send_keys("kelompok6") 
        time.sleep(1)
        browser.find_element(By.ID,"submit").click() 
        time.sleep(1)

    def test_signup_blank_field(self): 
        browser = self.browser 
        browser.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser") 
        time.sleep(3)
        browser.find_element(By.ID,"FirstName").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"Surname").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"E_post").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"Mobile").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"Username").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("")
        time.sleep(1)
        browser.find_element(By.ID,"ConfirmPassword").send_keys("") 
        time.sleep(1)
        browser.find_element(By.ID,"submit").click() 
        time.sleep(1)

        #error-message
        response_message = browser.find_element(By.ID,"FirstName-error").text
        self.assertEqual(response_message, 'Please enter first name')

        response_message = browser.find_element(By.ID,"Surname-error").text
        self.assertEqual(response_message, 'Please enter surname')

        response_message = browser.find_element(By.ID,"Username-error").text
        self.assertEqual(response_message, 'Please enter username')

        response_message = browser.find_element(By.ID,"Password-error").text
        self.assertEqual(response_message, 'Please enter password')

    def test_signup_registered_user(self): 
        browser = self.browser 
        browser.get("https://itera-qa.azurewebsites.net/UserRegister/NewUser") 
        time.sleep(3)
        browser.find_element(By.ID,"FirstName").send_keys("Muthia") 
        time.sleep(1)
        browser.find_element(By.ID,"Surname").send_keys("Conita") 
        time.sleep(1)
        browser.find_element(By.ID,"E_post").send_keys("social.muthia@gmail.com") 
        time.sleep(1)
        browser.find_element(By.ID,"Mobile").send_keys("0987654321") 
        time.sleep(1)
        browser.find_element(By.ID,"Username").send_keys("muthi4&c1") 
        time.sleep(1)
        browser.find_element(By.ID,"Password").send_keys("muthia16")
        time.sleep(1)
        browser.find_element(By.ID,"ConfirmPassword").send_keys("muthia16") 
        time.sleep(1)
        browser.find_element(By.ID,"submit").click() 
        time.sleep(1)

        #error-message
        response_message = browser.find_element(By.CSS_SELECTOR,"body > div > form > div > div:nth-child(12) > div > label").text
        self.assertEqual(response_message, 'Username already exist')
    
    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()