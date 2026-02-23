*** Settings ***
Resource        ./../Resources/Resource.robot
Library     SeleniumLibrary

*** Test Cases ***
#name of the testcase
Verify login with valid credentials
        Login
Verify Add to cart functionality
        Login
    Log    User selects the product
    Log    user adds the product to the cart
    Log    user verifies that the product with details is added to the cart
