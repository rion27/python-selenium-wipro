#create a fixture for invoking chrome browser
# and close the chrome browser

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def setup(request):
    service=Service(ChromeDriverManager().install())
    #driver instance is created to use webdriver globally
    #in the test script
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://opensource-demo.orangehrmlive.com/")
    #driver set locally is passed to request at class level
    #so that driver is available for other testcases in the tests folder
    request.cls.driver = driver
    yield
    driver.quit()