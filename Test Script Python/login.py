import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Login(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_tc01_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik button login
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.ID,"welcome").text
        response_data = browser.find_element(By.ID,"menu_dashboard_index").text

        self.assertIn('Welcome', response_message)
        self.assertEqual(response_data, 'Dashboard')
        

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()