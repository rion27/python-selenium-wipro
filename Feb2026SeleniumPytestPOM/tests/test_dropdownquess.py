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

        time.sleep(4)

        # -------- Single Select Dropdown --------
        dropdown = driver.find_element(By.ID, "option")

        # Select class is used for drop downs
        sel = Select(dropdown)

        sel.select_by_value("option 2")
        time.sleep(2)

        # -------- Multi Select Dropdown --------
        dropdown_multiple = driver.find_element(By.ID, "owc")
        sel = Select(dropdown_multiple)

        # Check if multiple selection is allowed
        print("Is multiple:", sel.is_multiple)

        # Select multiple options
        sel.select_by_visible_text("Option 1")
        sel.select_by_visible_text("Option 2")
        sel.select_by_visible_text("Option 3")

        time.sleep(3)

        # Deselect one option
        sel.deselect_by_visible_text("Option 2")

        time.sleep(3)


        driver.quit()