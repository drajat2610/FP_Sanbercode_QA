import unittest
import time
import login
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Leave(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    # submodul configure >> leave types
    def test_tc08_success_create_leave_type(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_Configure").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_leaveTypeList").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"leaveType_txtLeaveTypeName").send_keys("Cuti Melahirkan")
        time.sleep(1)
        browser.find_element(By.ID,"saveButton").click()
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CLASS_NAME,"fadable").text
        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertEqual(response_message, 'Successfully Saved') 
        self.assertIn('Cuti Melahirkan', response_data)
        
    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()