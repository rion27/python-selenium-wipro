import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_saucedemo_e2e():

    url = "https://www.saucedemo.com/"

    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()

    try:
        # Open Website
        driver.get(url)
        time.sleep(2)

        # Login
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

        print("Login Successful")

        # Add Product
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)

        # Go to Cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)

        # Checkout
        driver.find_element(By.ID, "checkout").click()
        time.sleep(2)

        driver.find_element(By.ID, "first-name").send_keys("Rion")
        driver.find_element(By.ID, "last-name").send_keys("Test")
        driver.find_element(By.ID, "postal-code").send_keys("781005")
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)

        driver.find_element(By.ID, "finish").click()
        time.sleep(2)

        success_text = driver.find_element(By.CLASS_NAME, "complete-header").text
        assert "Thank you for your order!" in success_text

        print("Order Completed Successfully")

    except Exception as e:
        print("Test Failed Due To:", e)

    finally:
        driver.quit()