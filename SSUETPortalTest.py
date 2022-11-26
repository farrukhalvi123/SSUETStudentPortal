import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class SsuetPortal_Test(unittest.TestCase):
    @classmethod  #This Method Executes Before All/each Test Case(s)
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://edusmartz.ssuet.edu.pk/FacultyPortal/Faculty/EDU_EBS_FCT_Login.aspx")
        cls.driver.maximize_window()
    def test_login(self):
        self.driver.find_element(By.ID,"txtLogin_cs").send_keys("102551")
        self.driver.find_element(By.ID,"txtPassword_m6cs").send_keys("123456789")
        self.driver.find_element(By.ID,"btnlgn").click()
        self.driver.save_screenshot(r"C:\Users\Administrator\Desktop\SSUETStudentPortal\Screenshots\image.png")

    def test_logout(self):
        try:
            self.test_login()
            topright = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(((By.ID, "ctl00_lblUser"))))
            self.driver.execute_script("arguments[0].click();", topright)
            time.sleep(2)
            logout = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(((By.ID, "ctl00_lblogout"))))
            logout.click()
        except:
            topright = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(((By.ID, "ctl00_lblUser"))))
            self.driver.execute_script("arguments[0].click();", topright)
            time.sleep(2)
            logout = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(((By.ID, "ctl00_lblogout"))))
            logout.click()

    @classmethod
    def tearDownClass(cls): # After All Test Cases
        cls.driver.close()
        cls.driver.quit()


# # driver.find_element(By.ID,"txtLogin_cs").send_keys("102551")
# # driver.find_element(By.ID,"txtPassword_m6cs").send_keys("123456789")
# # driver.find_element(By.ID,"btnlgn").click()
# time.sleep(2)
#  # driver.find_element(By.ID,"ctl00_lblUser")
# topright =WebDriverWait(driver, 10).until(EC.visibility_of_element_located(((By.ID, "ctl00_lblUser"))))
# driver.execute_script("arguments[0].click();",topright)
# time.sleep(2)
# logout = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(((By.ID, "ctl00_lblogout"))))
# logout.click()
# driver.find_element(By.ID,"txtLogin_cs").send_keys("10255")
# driver.find_element(By.ID,"txtPassword_m6cs").send_keys("12345678")
# driver.find_element(By.ID,"btnlgn").click()
# time.sleep(2)
# assert "Wrong Username or Password" in driver.page_source
