import unittest
import time
import login
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Dashboard(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    # fitur update status
    def test_tc15_success_redirect_page(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[1]/div/a/span").click()
        time.sleep(1)
        
        # validasi
        response_url1 = browser.current_url
        self.assertIn('/index.php/leave/assignLeave', response_url1)

        # steps
        browser.find_element(By.ID,"menu_dashboard_index").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[2]/div/a/span").click()
        time.sleep(1)
        
        # validasi
        response_url2 = browser.current_url
        self.assertIn('/index.php/leave/viewLeaveList', response_url2)

        # steps
        browser.find_element(By.ID,"menu_dashboard_index").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[3]/div/a/span").click()
        time.sleep(1)
        
        # validasi
        response_url3 = browser.current_url
        self.assertIn('/index.php/time/viewEmployeeTimesheet', response_url3)

        # steps
        browser.find_element(By.ID,"menu_dashboard_index").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[4]/div/a/span").click()
        time.sleep(1)
        
        # validasi
        response_url4 = browser.current_url
        self.assertIn('/index.php/leave/applyLeave', response_url4)

        # steps
        browser.find_element(By.ID,"menu_dashboard_index").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[5]/div/a/span").click()
        time.sleep(1)
        
        # validasi
        response_url5 = browser.current_url
        self.assertIn('/index.php/leave/viewMyLeaveList', response_url5)

        # steps
        browser.find_element(By.ID,"menu_dashboard_index").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[6]/div/a/span").click()
        time.sleep(1)
        
        # validasi
        response_url6 = browser.current_url
        self.assertIn('/index.php/time/viewMyTimesheet', response_url6)
        
    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()