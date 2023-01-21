import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_home(self):

        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login") 
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("ada") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(3)
        driver.get("https://itera-qa.azurewebsites.net/")
        time.sleep(3)

    def test_home_article(self): 
        
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net/Login") 
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("ada") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div/div[1]/form/table/tbody/tr[7]/td[2]/input[1]").click() 
        time.sleep(3)
        driver.get("https://itera-qa.azurewebsites.net/")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/p[2]/a"),click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/p[2]/a"),click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[2]/p[2]/a"),click()
        time.sleep(1)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[3]/p[2]/a"),click()
        time.sleep(1)

    def test_practice(self): 
        
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("ada") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.get("https://itera-qa.azurewebsites.net/home/practice")
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/p/button").click() 
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/p/button").click() 
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/p/button").click() 
        time.sleep(3)
        driver.find_element(By.XPATH,"/html/body/div[2]/div[4]/p/button").click() 
        time.sleep(3)

    def test_search_customer_name(self): 
        
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("ada") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.get("https://itera-qa.azurewebsites.net/Dashboard")
        time.sleep(3)
        driver.find_element(By.ID,"searching").send_keys("mas")
        time.sleep(1)
        driver.find_element(By,XPATH,"/html/body/div[2]/div/form/input[2]").click()
        time.sleep(3)

    def test_search_customer_email(self): 
        
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("ada") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.get("https://itera-qa.azurewebsites.net/Dashboard")
        time.sleep(3)
        driver.find_element(By.ID,"searching").send_keys("maskumambang@gmail.com")
        time.sleep(1)
        driver.find_element(By,XPATH,"/html/body/div[2]/div/form/input[2]").click()
        time.sleep(3)

    def test_testautomation_practice_form(self):

        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net")
        driver.maximize_window()

        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("ada") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.get("https://itera-qa.azurewebsites.net/home/automation")
        time.sleep(3)
        wait = WebDriverWait(driver,20)
        driver.find_element(By.ID,"name").send_keys("Mas")
        time.sleep(3)
        driver.find_element(By.ID,"phone").send_keys("01224443588")
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("maskumambang@gmail.com")
        time.sleep(3)
        driver.find_element(By.ID,"password").send_keys("adaadasaja")
        time.sleep(3)
        driver.find_element(By.ID,"adress").send_keys("Bandung")
        time.sleep(3)
        driver.find_element(By.ID,"Male").is_selected()
        time.sleep(1)
        driver.find_element(By.ID,"Male").click()
        time.sleep(1)
        driver.find_element(By.ID,"Sunday").click()
        time.sleep(1)
        driver.find_element(By.ID,"Saturday").click()
        time.sleep(1)
        element = driver.find_element(By.XPATH,"//body//div//div//div//div//select")
        drp = Select(element)
        drp.select_by_index(2)
        time.sleep(1)
        driver.switch_to_frame(0)
        driver.find_element(By.ID,"inputGroupFile02").send_keys("C:/Users/techg/OneDrive/Pictures/23732.jpg")
        driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[2]/div/div/div[2]/span").click()

    def test_testautomation_practice_form_negatif(self):

        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net")
        driver.maximize_window()

        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("ada") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.get("https://itera-qa.azurewebsites.net/home/automation")
        time.sleep(3)
        wait = WebDriverWait(driver,20)
        driver.find_element(By.ID,"name").send_keys("")
        time.sleep(3)
        driver.find_element(By.ID,"phone").send_keys("")
        time.sleep(3)
        driver.find_element(By.ID,"email").send_keys("")
        time.sleep(3)
        driver.find_element(By.ID,"password").send_keys("")
        time.sleep(3)
        driver.find_element(By.ID,"adress").send_keys("")
        time.sleep(3)
        driver.find_element(By.ID,"Male").is_selected()
        time.sleep(1)
        driver.find_element(By.ID,"Male").click()
        time.sleep(1)
        driver.find_element(By.ID,"Sunday").click()
        time.sleep(1)
        driver.find_element(By.ID,"Saturday").click()
        time.sleep(1)
        element = driver.find_element(By.XPATH,"//body//div//div//div//div//select")
        drp = Select(element)
        drp.select_by_index(2)
        time.sleep(1)
        driver.switch_to_frame(0)
        driver.find_element(By.ID,"inputGroupFile02").send_keys("")
        driver.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[2]/div/div/div[2]/span").click()

    def test_tutorial_page(self):
        
        driver = self.driver
        driver.get("https://itera-qa.azurewebsites.net")
        driver.maximize_window()

        time.sleep(3)
        driver.find_element(By.ID,"Username").send_keys("ada") 
        time.sleep(1)
        driver.find_element(By.ID,"Password").send_keys("test123") 
        time.sleep(1)
        driver.get("https://itera-qa.azurewebsites.net/home/tutorial")
        time.sleep(3)


    def tearDown(self): 
        self.driver.close() 

if __name__ == "__main__": 
    unittest.main()
