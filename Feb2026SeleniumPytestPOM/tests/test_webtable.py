from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_table:
    def test_table(self):
        driver = webdriver.Chrome()
        driver.get("https://the-internet.herokuapp.com/tables")
        driver.maximize_window()

        rows=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr[1]/tr")
        for i in rows:
            print(i.text)

        time.sleep(2)
        #no of columns

        cols=driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr[1]/td")
        for i in cols:
            print(i.text)
        time.sleep(2)

        #fetch the cell data
        celldata=driver.find_element(By.XPATH,"//table[@id='table1']/tbody/tr[3]/td[4]")
        assert "$100.00" in celldata.text

        driver.quit()
