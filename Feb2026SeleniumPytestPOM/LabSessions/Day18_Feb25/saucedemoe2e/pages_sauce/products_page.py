from selenium.webdriver.common.by import By

class InventoryPage:

    add_to_cart_button = (By.XPATH, "(//button[text()='Add to cart'])[1]")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_first_product(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()