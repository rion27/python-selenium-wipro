*** Settings ***
Resource        ./../Resources/Resource.robot
Library     SeleniumLibrary
Test Setup      Launch Browser
Task Teardown   Closing the Browser

*** Test Cases ***

Verify login with valid credentials
        Login
Verify Add to cart functionality
        Login
    Log    User selects the product
    Log    User adds the product to the cart
    Log    User verifies the product with details
