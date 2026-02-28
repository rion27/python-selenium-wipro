from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    bank_manager_btn = (By.XPATH, "//button[text()='Bank Manager Login']")
    customer_login_btn = (By.XPATH, "//button[text()='Customer Login']")
    home_btn = (By.XPATH, "//button[text()='Home']")
    user_dropdown = (By.ID, "userSelect")
    login_btn = (By.XPATH, "//button[text()='Login']")
    welcome_text = (By.XPATH, "//strong[contains(text(),'Welcome')]")

    # Methods
    def click_bank_manager_login(self):
        time.sleep(2)
        element = self.wait.until(EC.element_to_be_clickable(self.bank_manager_btn))
        element.click()


    def click_customer_login(self):
        element = self.wait.until(EC.element_to_be_clickable(self.customer_login_btn))
        time.sleep(2)
        element.click()


    def click_home(self):
        element = self.wait.until(EC.element_to_be_clickable(self.home_btn))
        time.sleep(2)
        element.click()


    def select_customer(self, name):
        dropdown = self.wait.until(EC.presence_of_element_located(self.user_dropdown))
        time.sleep(2)
        Select(dropdown).select_by_visible_text(name)


    def click_login(self):
        element = self.wait.until(EC.element_to_be_clickable(self.login_btn))
        time.sleep(2)
        element.click()


    def get_welcome_text(self):
        time.sleep(2)
        return self.wait.until(EC.visibility_of_element_located(self.welcome_text)).text