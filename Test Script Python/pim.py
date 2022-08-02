import unittest
import time
import login
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Pim(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    # submodul pim >> add employee
    def test_tc05_success_create_employee(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_addEmployee").click()
        time.sleep(1)
        browser.find_element(By.ID,"firstName").send_keys("John")
        time.sleep(1)
        browser.find_element(By.ID,"middleName").send_keys("Maverick")
        time.sleep(1)
        browser.find_element(By.ID,"lastName").send_keys("Michele")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()

        # validasi
        response_message1 = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/div/h1").text
        response_message2 = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/h1").text

        self.assertIn('Maverick', response_message1)
        self.assertIn('Personal Details', response_message2)

    # submodul pim >> add employee
    def test_tc06_failed_create_employee(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_addEmployee").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()

        # validasi
        response_message1 = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[1]/span").text
        response_message2 = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[3]/span").text

        self.assertIn('Required', response_message1)
        self.assertIn('Required', response_message2)

    # submodul reports
    def test_tc07_search_report_name(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_core_viewDefinedPredefinedReports").click()
        time.sleep(1)
        browser.find_element(By.ID,"search_search").send_keys("Job Details")
        time.sleep(1)
        browser.find_element(By.NAME,"_search").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"resultTable").text
        
        self.assertIn('Job Details', response_data)
        
    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()