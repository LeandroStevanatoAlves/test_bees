Feature: Items Page

  Scenario: Create a new item
    Given the user is on the Items page
    And clicks on New Item
    And fill all fields of New Item form with valid information
    When clicks on Create Item button
    Then the user should see the "Item was successfully created." message
