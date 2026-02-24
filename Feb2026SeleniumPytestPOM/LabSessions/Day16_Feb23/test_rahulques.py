import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_greenkart_e2e():

    # URL variable
    url = "https://rahulshettyacademy.com/seleniumPractise/#/"

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    try:
        #Open Website
        driver.get(url)
        time.sleep(2)

        #Search Product (Example: Cucumber)
        driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("Cucumber")
        time.sleep(2)

        #Add Product to Cart
        driver.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
        time.sleep(2)

        print("Product Added to Cart")

        #Click Cart Icon
        driver.find_element(By.CLASS_NAME, "cart-icon").click()
        time.sleep(2)

        #Click Proceed to Checkout
        driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
        time.sleep(3)

        #Apply Promo Code
        driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
        driver.find_element(By.CLASS_NAME, "promoBtn").click()
        time.sleep(3)

        #Validate Promo Applied Message
        promo_msg = driver.find_element(By.CLASS_NAME, "promoInfo").text
        print("Promo Message:", promo_msg)

        assert "Code applied" in promo_msg

        print("Promo Code Applied Successfully")

    except Exception as e:
        print("Test Failed Due To:", e)

    finally:
        time.sleep(3)
        driver.quit()