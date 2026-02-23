*** Settings ***
Library     SeleniumLibrary
*** Keywords ***
Enter Username
        [Arguments]     ${username}
        Input Text    xpath://input[@name='username']       ${username}
Enter Password
        [Arguments]     ${password}
        Input Text    xpath://input[@name='password']    ${password}
Click Login Button
        Click Button    xpath://button[@type='submit']
Login With Credentials
        [Arguments]     ${username}     ${password}
        Enter Username    ${username}
        Enter Password    ${password}
        Click Login Button
Verify Login Error Message
        Element Text Should Be    xpath://p[.='Invalid credentials']        Invalid credentials