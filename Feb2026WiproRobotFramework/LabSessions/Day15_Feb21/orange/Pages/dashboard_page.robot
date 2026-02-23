*** Settings ***
Library     SeleniumLibrary
*** Keywords ***
Verify Dashboard Is Visible
        Element Text Should Be    xpath://h6[.='Dashboard']    Dashboard
