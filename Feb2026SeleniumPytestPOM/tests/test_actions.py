import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Test_Actions:

    def test_actions(self):
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()

        driver.get("https://www.amazon.in/")
        time.sleep(2)

        actions=ActionChains(driver)
        bestsellers=driver.find_element(By.XPATH,"//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']")

        #double click using actions class
        actions.double_click(bestsellers).perform()    #double click
        time.sleep(2)
        driver.back()
        time.sleep(2)

        mobiles=driver.find_element(By.XPATH,"//a[normalize-space()='Mobiles']")
        #mobiles = driver.find_element(By.CSS_SELECTOR, ".nav-a[href='/mobile-phones/b/?ie=UTF8&node=1389401031&ref_=nav_cs_mobiles']")
        actions.context_click(mobiles).perform() #right click
        time.sleep(2)
        #driver.back()
        #driver.close()

        #move to element
        prime=driver.find_element(By.XPATH,"//span[normalize-space()='Prime']")
        actions.move_to_element(prime).perform()

        #click and hold
        fresh=driver.find_element(By.XPATH,"//span[normalize-space()='Fresh']")
        actions.click_and_hold(fresh).perform()
