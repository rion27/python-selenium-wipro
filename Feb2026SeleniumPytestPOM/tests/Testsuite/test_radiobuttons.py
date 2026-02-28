import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_radio():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/AutomationPractice/")

    time.sleep(4)
    radio_btn = driver.find_element(By.XPATH, "(//input[@value='radio2'])[1]")
    radio_btn.click()
    time.sleep(2)
    check2_btn = driver.find_element(By.XPATH, "//input[@id='checkBoxOption2']")
    check2_btn.click()
    time.sleep(2)
    check3_btn = driver.find_element(By.XPATH, "//input[@id='checkBoxOption3']")
    check3_btn.click()
    driver.quit()


def test_radio_link2():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get("https://testautomationpractice.blogspot.com/")

    time.sleep(4)
    gender_btn = driver.find_element(By.XPATH, "//input[@id='male']")
    gender_btn.click()
    time.sleep(2)
    day1_btn = driver.find_element(By.XPATH, "//input[@id='sunday']")
    day1_btn.click()
    time.sleep(2)
    day2_btn = driver.find_element(By.XPATH, "//input[@id='saturday']")
    day2_btn.click()
    driver.quit()
