import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CustomerPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    deposit_tab = (By.XPATH, "//button[@ng-click='deposit()']")
    withdraw_tab = (By.XPATH, "//button[@ng-click='withdrawl()']")
    amount_input = (By.XPATH, "//input[@placeholder='amount']")
    deposit_btn = (By.XPATH, "//button[text()='Deposit']")
    withdraw_btn = (By.XPATH, "//button[text()='Withdraw']")
    balance_text = (By.XPATH, "//strong[2]")
    transactions_tab = (By.XPATH, "//button[@ng-click='transactions()']")
    transaction_rows = (By.XPATH, "//table/tbody/tr")

    # ========== METHODS ==========

    def click_deposit_tab(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.deposit_tab)).click()

    def deposit_amount(self, amount):
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.amount_input)).send_keys(amount)
        self.driver.find_element(*self.deposit_btn).click()

    def click_withdraw_tab(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.withdraw_tab)).click()

    def withdraw_amount(self, amount):
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located(self.amount_input)).send_keys(amount)
        self.driver.find_element(*self.withdraw_btn).click()

    def get_balance(self):
        time.sleep(2)
        return self.wait.until(EC.visibility_of_element_located(self.balance_text)).text

    def click_transactions_tab(self):
        time.sleep(2)
        self.wait.until(EC.element_to_be_clickable(self.transactions_tab)).click()

    def get_transaction_data(self):
        rows = self.wait.until(EC.presence_of_all_elements_located(self.transaction_rows))
        transactions = []

        for row in rows:
            transactions.append(row.text)

        return transactions