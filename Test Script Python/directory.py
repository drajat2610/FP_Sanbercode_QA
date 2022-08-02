import unittest
import time
import login
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Directory(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_tc13_success_search_directory(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_directory_viewDirectory").click()
        time.sleep(1)
        browser.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys("Jasmine Morgan")
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[2]/ul/li[1]/b").text

        self.assertIn('Jasmine Morgan', response_data)
        
    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()