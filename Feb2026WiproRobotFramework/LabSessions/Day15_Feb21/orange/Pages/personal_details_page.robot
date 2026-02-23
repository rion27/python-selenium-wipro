*** Settings ***
Library    SeleniumLibrary

*** Keywords ***

Update First Name
    [Arguments]    ${firstname}
    Clear Element Text    xpath://input[@name='firstName']
    Input Text    xpath://input[@name='firstName']    ${firstname}
    Click Button    xpath://div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']

Verify First Name Updated
    [Arguments]     ${expected_name}
    Textfield Value Should Be        xpath://input[@name='firstName']        ${expected_name}