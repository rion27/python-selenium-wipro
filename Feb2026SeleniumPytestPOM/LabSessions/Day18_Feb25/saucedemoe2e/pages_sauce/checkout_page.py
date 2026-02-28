from selenium.webdriver.common.by import By

class CheckoutPage:

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def enter_details(self, fname, lname, zip):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip)
        self.driver.find_element(*self.continue_button).click()