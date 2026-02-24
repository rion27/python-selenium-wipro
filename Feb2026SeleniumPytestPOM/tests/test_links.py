import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
download_dir= 'C:/Users/rionb/Downloads'
class Test_Links:
    def test_link(self):
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        links=driver.find_elements(By.TAG_NAME,"a")
        count=len(links)
        print(count)

        for link in links:
            print(link.text)

        time.sleep(3)
        driver.close()