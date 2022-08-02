import unittest
import time
import login
import random
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Admin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    # submodul user management >> user
    def test_tc02_failed_create_user(self):
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_UserManagement").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewSystemUsers").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(1)

        # validasi
        response_message1 = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        response_message2 = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/span").text
        response_message3 = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[6]/span").text

        self.assertIn('Employee does not exist', response_message1)
        self.assertIn('Required', response_message2)
        self.assertIn('Required', response_message3) 

    # submodul job >> job title
    def test_tc03_success_create_job_title(self):
        browser = self.browser
        listjob = ["job1", "job2", "job3", "job4", "job5", "job6", "job7", "job8", "job9", "job10"]

        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        # step pilih menu
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_Job").click() # klik menu job
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewJobTitleList").click() # klik sub menu job title
        time.sleep(1)

        # step create job title
        browser.find_element(By.ID,"btnAdd").click() # klik buttton add
        time.sleep(1)
        browser.find_element(By.ID,"jobTitle_jobTitle").send_keys(random.choice(listjob)) # isi job title
        time.sleep(1)
        browser.find_element(By.ID,"jobTitle_jobDescription").send_keys("test description 123") # isi job description
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click() # klik button save
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.CLASS_NAME,"fadable").text

        self.assertEqual(response_message, 'Successfully Saved')      

    # submodul qualifications >> skills
    def test_tc04_failed_create_skill(self): 
        # steps
        browser = self.browser
        login.Login.test_tc01_success_login(self) # memanggil tc01 login
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_Qualifications").click()
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewSkills").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/span").text

        self.assertIn('Required', response_message)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()