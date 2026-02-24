from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from trio import sleep


def test():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    clickhere=driver.find_element(By.XPATH,"//a[normalize-space()='Click Here']")
    clickhere.click()
    #fetch the window handles of both tabs
    windows=driver.window_handles
    print(windows)
    #move the control to the child window
    driver.switch_to.window(windows[1])
    text=driver.find_element(By.XPATH,"//h3[contains(text(),'New Window')]")
    print(text)
    driver.close()
    #get back to parent window
    driver.switch_to.window(windows[0])
    clickhere.is_displayed()
    driver.close()