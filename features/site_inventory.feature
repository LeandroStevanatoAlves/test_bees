Feature: Inventories Page

  Scenario: Create a new inventory
    Given the user is on the Inventories page
    And clicks on New Inventory
    And fill all fields of New Inventory form with valid information
    When clicks on Create Inventory button
    Then the user should see the "Inventory was successfully created." message
