from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from trio import sleep

class Test_frames:
    def test_frames(self):
        driver = webdriver.Chrome()
        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()

        time.sleep(2)
        driver.implicitly_wait(10)
        #frame=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
        driver.switch_to.frame(0)

        datepicker=driver.find_element(By.XPATH,"//input[@id='datepicker']")
        datepicker.click()
        driver.close()
        