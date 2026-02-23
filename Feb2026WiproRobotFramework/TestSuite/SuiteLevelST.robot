*** Settings ***
Resource        ./../Resources/Resource.robot
Library     SeleniumLibrary
Suite Setup       Open DB
Suite Teardown   Close DB

*** Test Cases ***

Verify login with valid credentials
        Login
Verify Add to cart functionality
        Login
    Log    User selects the product
    Log    User adds the product to the cart
    Log    User verifies the product with details
