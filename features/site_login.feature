Feature: User Login

  Scenario: Login with valid user
    Given the user is on the login page
    And enters valid credentials
    When clicks the login button
    Then the user should see the "Welcome to your storage" message

  Scenario: Login with valid user
    Given the user is on the login page
    And enters invalid email
    When clicks the login button
    Then the user should stay on login page

  Scenario: Login with valid user
    Given the user is on the login page
    And enters invalid password
    When clicks the login button
    Then the user should stay on login page