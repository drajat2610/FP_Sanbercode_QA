import unittest
import time
import login
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Time(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    # submodul timesheets >> employee timesheets
    def test_tc09_success_search_timesheet(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_time_viewTimeModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_time_Timesheets").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_time_viewEmployeeTimesheet").click()
        time.sleep(1)
        browser.find_element(By.ID,"employee").send_keys("Garry White")
        time.sleep(1)
        browser.find_element(By.ID,"btnView").click()
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"viewTimesheetForm").text

        self.assertIn('Garry White', response_data)

    # submodul project info >> customer
    def test_tc10_success_add_customer(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_time_viewTimeModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_ProjectInfo").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewCustomers").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"addCustomer_customerName").send_keys("Indonesia Eximbank")
        time.sleep(1)
        browser.find_element(By.ID,"addCustomer_description").send_keys("Lembaga Pembiayaan Ekspor Indonesia")
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CLASS_NAME,"fadable").text
        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertEqual(response_message, 'Successfully Saved') 
        self.assertIn('Indonesia Eximbank', response_data)
        
    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()