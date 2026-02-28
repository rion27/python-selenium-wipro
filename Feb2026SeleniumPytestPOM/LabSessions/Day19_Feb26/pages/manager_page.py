from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class ManagerPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    add_customer_tab = (By.XPATH, "//button[@ng-click='addCust()']")
    first_name_input = (By.XPATH, "//input[@placeholder='First Name']")
    last_name_input = (By.XPATH, "//input[@placeholder='Last Name']")
    post_code_input = (By.XPATH, "//input[@placeholder='Post Code']")
    add_customer_btn = (By.XPATH, "//button[text()='Add Customer']")

    open_account_tab = (By.XPATH, "//button[@ng-click='openAccount()']")
    customer_dropdown = (By.ID, "userSelect")
    currency_dropdown = (By.ID, "currency")
    process_btn = (By.XPATH, "//button[text()='Process']")

    customers_tab = (By.XPATH, "//button[@ng-click='showCust()']")
    customers_table_rows = (By.XPATH, "//table/tbody/tr")

    # ========== METHODS ==========

    def click_add_customer_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.add_customer_tab)).click()

    def add_customer(self, fname, lname, postcode):
        self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(fname)
        self.driver.find_element(*self.last_name_input).send_keys(lname)
        self.driver.find_element(*self.post_code_input).send_keys(postcode)
        time.sleep(2)
        self.driver.find_element(*self.add_customer_btn).click()

    def handle_alert_and_get_text(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        time.sleep(2)
        alert.accept()
        return alert_text

    def click_open_account_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.open_account_tab)).click()

    def open_account(self, customer_name, currency):
        customer_name = customer_name.strip()
        customer_dd = self.wait.until(EC.presence_of_element_located(self.customer_dropdown))
        time.sleep(2)
        Select(customer_dd).select_by_visible_text(customer_name)

        currency_dd = self.driver.find_element(*self.currency_dropdown)
        Select(currency_dd).select_by_visible_text(currency)

        self.driver.find_element(*self.process_btn).click()

    def click_customers_tab(self):
        self.wait.until(EC.element_to_be_clickable(self.customers_tab)).click()

    def verify_customer_in_table(self, fname, lname):
        customer_row = (
            By.XPATH,
            f"//table//tr[td[text()='{fname}'] and td[text()='{lname}']]"
        )

        row = self.wait.until(
            EC.presence_of_element_located(customer_row)
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", row
        )
        time.sleep(2)

        return row.is_displayed()