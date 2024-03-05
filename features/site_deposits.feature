Feature: Deposits Page

  @selenium
  Scenario: Create a new deposit
    Given the user is on the deposits page
    And clicks on New Deposit
    And fill all fields with valid information
    When clicks on create deposit button
    Then the user should see the "Deposit was successfully created." message
