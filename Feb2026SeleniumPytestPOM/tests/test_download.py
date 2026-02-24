import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
download_dir= 'C:/Users/rionb/Downloads'
class Test_Download:
    def test_dw(self):
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        alert=driver.find_element(By.XPATH,"//a[normalize-space()='alert.jpeg']")
        alert.click()
        time.sleep(7)
        #verify file downloaded or not
        file_path=os.path.join(download_dir,"alert.jpeg")
        assert os.path.exists(file_path)

        time.sleep(2)
        driver.close()