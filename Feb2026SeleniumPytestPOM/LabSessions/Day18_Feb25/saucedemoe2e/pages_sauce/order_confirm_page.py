from selenium.webdriver.common.by import By

class ConfirmationPage:

    finish_button = (By.ID, "finish")
    confirmation_text = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def finish_order(self):
        self.driver.find_element(*self.finish_button).click()

    def get_confirmation(self):
        return self.driver.find_element(*self.confirmation_text).text