import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_dropdown():

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.get('https://trytestingthis.netlify.app/')

        time.sleep(3)

        # -------- Single Select Dropdown --------
        dropdown = driver.find_element(By.ID, "option")
        sel = Select(dropdown)

        sel.select_by_visible_text("Option 2")
        time.sleep(2)

        # Check which option is selected
        for option in sel.options:
            if option.is_selected():
                print("Single Dropdown Selected:", option.text)

        # -------- Multi Select Dropdown --------
        dropdown_multiple = driver.find_element(By.ID, "owc")
        sel_multi = Select(dropdown_multiple)

        sel_multi.select_by_visible_text("Option 1")
        sel_multi.select_by_visible_text("Option 2")
        sel_multi.select_by_visible_text("Option 3")

        time.sleep(2)

        # Check selected options
        print("Multi Dropdown Selected Options:")
        for option in sel_multi.options:
            if option.is_selected():
                print(option.text)

        time.sleep(3)
        driver.quit()