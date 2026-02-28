import pytest
from pages_sauce.login_page import LoginPage
from pages_sauce.products_page import InventoryPage
from pages_sauce.cart_page import CartPage
from pages_sauce.checkout_page import CheckoutPage
from pages_sauce.order_confirm_page import ConfirmationPage
from utilities.excel_utils import get_excel_data

# Read login data
login_data = get_excel_data("C:/Users/rionb/PycharmProjects/Automation-Frameworks-2026/python-selenium-wipro/Feb2026SeleniumPytestPOM/LabSessions/Day18_Feb25/saucedemoe2e/testdata/login_data.xlsx", "Sheet1")
# Read checkout data
checkout_data = get_excel_data("C:/Users/rionb/PycharmProjects/Automation-Frameworks-2026/python-selenium-wipro/Feb2026SeleniumPytestPOM/LabSessions/Day18_Feb25/saucedemoe2e/testdata/checkout_data.xlsx", "Sheet1")

@pytest.mark.parametrize("username,password", login_data)
@pytest.mark.parametrize("first_name,last_name,postal_code", checkout_data)
def test_complete_purchase(driver, username, password, first_name, last_name, postal_code):
    # Step 1: Login
    lp = LoginPage(driver)
    lp.login(username, password)

    # Step 2: Add first product to cart
    inv = InventoryPage(driver)
    inv.add_first_product()
    inv.go_to_cart()

    # Step 3: Go to cart and checkout
    cart = CartPage(driver)
    cart.click_checkout()

    # Step 4: Enter checkout details from Excel
    checkout = CheckoutPage(driver)
    checkout.enter_details(first_name, last_name, postal_code)

    # Step 5: Confirm order
    confirm = ConfirmationPage(driver)
    confirm.finish_order()

    assert "Thank you for your order!" in confirm.get_confirmation()