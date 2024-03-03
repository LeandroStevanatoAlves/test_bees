Feature: Deposits Page

  Scenario: Login with valid user
    Given the user is on the deposits page
    And clicks on New Deposit
    And fill all fields with valid information
    When clicks on create deposit button
    Then the user should see the "Deposit was successfully created." message

    #Show
    #Delete