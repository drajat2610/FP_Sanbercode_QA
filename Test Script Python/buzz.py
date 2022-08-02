import unittest
import time
import login
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Buzz(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    # fitur update status
    def test_tc14_success_update_status(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_buzz_viewBuzz").click()
        time.sleep(1)
        browser.find_element(By.ID,"status-tab-label").click()
        time.sleep(1)
        browser.find_element(By.ID,"createPost_content").send_keys("ini adalah postingan saya")
        time.sleep(1)
        browser.find_element(By.ID,"postSubmitBtn").click()
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"buzz").text

        self.assertIn('ini adalah postingan saya', response_data)
        
    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()