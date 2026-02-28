import pytest
from pages_sauce.login_page import LoginPage
from utilities.excel_utils import get_excel_data

test_data = get_excel_data("C:/Users/rionb/PycharmProjects/Automation-Frameworks-2026/python-selenium-wipro/Feb2026SeleniumPytestPOM/LabSessions/Day18_Feb25/saucedemoe2e/testdata/login_data.xlsx", "Sheet1")

class TestLogin:

    @pytest.mark.parametrize("username,password", test_data)
    def test_login(self, driver, username, password):
        lp = LoginPage(driver)
        lp.login(username, password)

        if username == "standard_user" and password == "secret_sauce":
            assert "inventory" in driver.current_url
        else:
            assert "Epic sadface" in lp.get_error()