import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime


@pytest.fixture(scope="function")
def driver():

    options = webdriver.ChromeOptions()

    #Open in Incognito
    options.add_argument("--incognito")

    #Disable password save popup
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    #Disable notifications
    options.add_argument("--disable-notifications")

    #Start maximized
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:

        driver = item.funcargs.get("driver")

        if driver:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            screenshot_dir = os.path.join(base_dir, "screenshots")

            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(file_path)