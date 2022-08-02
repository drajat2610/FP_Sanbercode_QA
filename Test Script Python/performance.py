import unittest
import time
import login
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Performance(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    # submodul configure >> KPIs
    def test_tc11_success_create_kpi(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu__Performance").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_Configure").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_searchKpi").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID, "defineKpi360_jobTitleCode").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/select/option[2]").click()
        time.sleep(2)
        browser.find_element(By.ID,"defineKpi360_keyPerformanceIndicators").send_keys("test input KPI")
        time.sleep(2)
        browser.find_element(By.ID,"defineKpi360_minRating").clear()
        time.sleep(1)
        browser.find_element(By.ID,"defineKpi360_minRating").send_keys("30")
        time.sleep(1)
        browser.find_element(By.ID,"defineKpi360_maxRating").clear()
        time.sleep(1)
        browser.find_element(By.ID,"defineKpi360_maxRating").send_keys("100")
        time.sleep(1)
        browser.find_element(By.ID,"saveBtn").click()
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"resultTable").text
        response_message = browser.find_element(By.CLASS_NAME,"fadable").text

        self.assertIn('test input KPI', response_data)
        self.assertEqual(response_message, 'Successfully Saved')

    # submodul configure >> KPIs
    def test_tc12_success_search_kpi(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu__Performance").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_Configure").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_searchKpi").click()
        time.sleep(1)
        browser.find_element(By.ID,"kpi360SearchForm_jobTitleCode").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li/select/option[2]").click()
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click()
        time.sleep(2)

        # validasi
        response_data = browser.find_element(By.ID,"resultTable").text

        self.assertIn('Automation Tester', response_data)
        
    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()