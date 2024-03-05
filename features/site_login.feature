Feature: User Login

  @selenium
  Scenario: Login with valid user
    Given the user is on the login page
    And enters valid credentials
    When clicks on the login button
    Then the user should see the "Welcome to your storage" message

  @selenium
  Scenario: Login with valid user
    Given the user is on the login page
    And enters invalid email
    When clicks on the login button
    Then the user should stay on login page

  @selenium
  Scenario: Login with valid user
    Given the user is on the login page
    And enters invalid password
    When clicks on the login button
    Then the user should stay on login page