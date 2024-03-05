Feature: Endpoint /inventories

  @api
  Scenario: List Inventories
    When a GET request is sent to "/inventories.json"
    Then the response status code should be 200
    And the response should contain a list of inventories

  @api
  Scenario: Create a Inventory
    Given the payload with necessary inventory data is prepared
    When a POST request is sent to "/inventories.json" with the inventory data
    Then the response status code should be 201
    And the response should contain the created inventory details

  @api
  Scenario: Show Inventory Details
    Given there is an existing inventory
    When a GET request is sent to "/inventories/id.json"
    Then the response status code should be 200
    And the response should contain inventory details

  @api
  Scenario: Error When Try to Show Details of a Inventory That doesn't exist
    Given there is an nonexistent inventory
    When a GET request is sent to "/inventories/id.json"
    Then the response status code should be 404
    And the response should contain details of the error 404

  @api
  Scenario: Update Inventory (Using PUT)
    Given there is an existing inventory
    And have a updated inventory data
    When a PUT request is sent to "/inventories/id.json" with the updated data
    Then the response status code should be 200
    And the response should contain the updated inventory details

  @api
  Scenario: Update Inventory (Using PATCH)
    Given there is an existing inventory
    And have a updated inventory data
    When a PATCH request is sent to "/inventories/id.json" with the updated data
    Then the response status code should be 200
    And the response should contain the updated inventory details

  @api
  Scenario: Delete Inventory
    Given there is an existing inventory
    When a DELETE request is sent to "/inventories/id.json"
    Then the response status code should be 204
    And the inventory should be successfully deleted
