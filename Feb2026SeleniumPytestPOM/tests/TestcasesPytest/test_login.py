import time
import pytest
from pages.Login_page import LoginPage
from utilities.excel_utils import get_excel_data
from utilities.logger import get_logger

logger=get_logger()
test_data=get_excel_data("C:/Users/rionb/PycharmProjects/Automation-Frameworks-2026/python-selenium-wipro/Feb2026SeleniumPytestPOM/testdata/login_data.xlsx","Sheet1")

class TestLogin:
    def test_valid_login(self,driver):
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        #create the object of login_page
        lp=LoginPage(driver)
        logger.info("Entering the credentials")
        lp.login("Admin","admin123")
        time.sleep(2)

        assert "OrangeHRM" in driver.title
    def test_invalid_login(self,driver):
        logger.info("Opening application")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        #create the obj of login page
        lp=LoginPage(driver)
        lp.login("Admin","wrongpass")

        time.sleep(2)
        assert "Invalid credentials" in lp.get_error_message()

    # test data stored in excel sheet
    @pytest.mark.parametrize("username, password", test_data)
    def test_login_excel(self, driver, username, password):
        logger.info("Opening application")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        # create the object of login_page
        lp = LoginPage(driver)
        lp.login(username, password)

        if password == "admin123":
            assert "OrangeHRM" in driver.title
        else:
            assert "Invalid credentials" in lp.get_error_message()
