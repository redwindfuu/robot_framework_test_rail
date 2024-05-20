*** Settings ***
Documentation     A test suite containing tests related to invalid login.
...
...               These tests are data-driven by their nature. They use a single
...               keyword, specified with Test Template setting, that is called
...               with different arguments to cover different scenarios.
...
...               This suite also demonstrates using setups and teardowns in
...               different levels.
Suite Setup       Open Browser To Login Page
Suite Teardown    Close Browser
Test Setup        Go To Login Page
Test Template     Login With Invalid Credentials Should Fail
Resource          resource.robot

*** Test Cases ***               USER NAME        PASSWORD       ID
Invalid Username                 invalid          ${VALID PASSWORD}   7
Invalid Password                 ${VALID USER}    invalid    6
Invalid Username And Password    invalid          whatever    5
Empty Username                   ${EMPTY}         ${VALID PASSWORD}    8
Empty Password                   ${VALID USER}    ${EMPTY}    4
Empty Username And Password      ${EMPTY}         ${EMPTY}    9
*** Keywords ***
Login With Invalid Credentials Should Fail
    [Arguments]    ${username}    ${password}    ${ID}
    Set Tags    id=${ID}
    ${id} =    Get Test Metadata    ID
    Input Username    ${username}
    Input Password    ${password}
    Submit Credentials
    Login Should Have Failed

Login Should Have Failed
    
    Location Should Be    ${ERROR URL}
    Title Should Be    Error Page