from selenium.webdriver.support import  expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        #dismiss pass popup
        self.dismiss_password_popup()

    def get_error(self):
        return self.driver.find_element(*self.error_message).text

    def dismiss_password_popup(self):
        try:
            popup = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//button[text()='Never'] | //button[text()='OK']")
                )
            )
            popup.click()
            print("Password popup dismissed")
        except:
            print("Password popup did not appear")