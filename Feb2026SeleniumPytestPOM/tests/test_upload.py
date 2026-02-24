import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Test_Upload:
    def test_up(self):
        driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)

        browse=driver.find_element(By.XPATH,"//input[@id='file-upload']")
        browse.send_keys("C://Users/rionb/PycharmProjects/IMG_8075.jpg")
        time.sleep(2)
        upload=driver.find_element(By.XPATH,"//input[@id='file-submit']")

        upload.click()
        time.sleep(2)
        fileupload=driver.find_element(By.XPATH,"//h3[normalize-space()='File Uploaded!']")
        assert fileupload.text == "File Uploaded!"

        time.sleep(2)
        driver.close()