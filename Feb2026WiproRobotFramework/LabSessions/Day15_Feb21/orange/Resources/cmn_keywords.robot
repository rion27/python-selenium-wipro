*** Settings ***
Library     SeleniumLibrary
Resource        variables.robot

*** Keywords ***
Open Application

        Open Browser    ${url}      ${browser}
        Maximize Browser Window
        Set Selenium Implicit Wait    5s

Close Application

        Close Browser