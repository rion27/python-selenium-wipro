import pytest
import time

from pages.login_page import LoginPage
from pages.manager_page import ManagerPage
from pages.customer_page import CustomerPage
from utilities.excel_utils import ExcelUtils
from utilities.logger import LogGen


logger = LogGen.loggen()
excel = ExcelUtils()
test_data = excel.get_test_data()


@pytest.mark.parametrize("data", test_data)
def test_xyz_bank_e2e(driver, data):

    fname = data["first_name"].strip()
    lname = data["last_name"].strip()
    postcode = str(data["postcode"]).strip()
    deposit_amt = str(data["deposit"]).strip()
    withdraw_amt = str(data["withdraw"]).strip()

    full_name = f"{fname} {lname}"

    logger.info(f"Starting flow for customer: {full_name}")

    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    driver.get(url)

    login_page = LoginPage(driver)
    manager_page = ManagerPage(driver)
    customer_page = CustomerPage(driver)

    # Manager Flow
    login_page.click_bank_manager_login()
    manager_page.click_add_customer_tab()
    manager_page.add_customer(fname, lname, postcode)

    alert_text = manager_page.handle_alert_and_get_text()
    assert "Customer added successfully" in alert_text

    manager_page.click_open_account_tab()
    manager_page.open_account(full_name, "Dollar")

    alert_text = manager_page.handle_alert_and_get_text()
    assert "Account created successfully" in alert_text

    manager_page.click_customers_tab()
    assert manager_page.verify_customer_in_table(fname, lname)

    login_page.click_home()

    # Customer Flow
    login_page.click_customer_login()
    login_page.select_customer(full_name)
    login_page.click_login()

    assert full_name in login_page.get_welcome_text()

    customer_page.click_deposit_tab()
    customer_page.deposit_amount(deposit_amt)

    assert customer_page.get_balance() == deposit_amt

    customer_page.click_withdraw_tab()
    customer_page.withdraw_amount(withdraw_amt)

    expected_balance = str(int(deposit_amt) - int(withdraw_amt))
    assert customer_page.get_balance() == expected_balance