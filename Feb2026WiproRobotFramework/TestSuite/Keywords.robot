*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***

Verify login with valid credentials
        Login
Verify Add to cart functionality
        Login
    Log    User selects the product
    Log    User adds the product to the cart
    Log    User verifies the product with details
*** Keywords ***
Login

    Log     Enter usernamr
    Log     Enter password
    Log     click on login button
    Log     user is on th home page