Feature: Endpoint /items

  @api
  Scenario: List Items
    When a GET request is sent to "/items.json"
    Then the response status code should be 200
    And the response should contain a list of items

  @api
  Scenario: Create a Item
    Given the payload with necessary item data is prepared
    When a POST request is sent to "/items.json" with the item data
    Then the response status code should be 201
    And the response should contain the created item details

  @api
  Scenario: Show Item Details
    Given there is an existing item
    When a GET request is sent to "/items/id.json"
    Then the response status code should be 200
    And the response should contain item details

  @api
  Scenario: Error When Try to Show Details of a Deposit That doesn't exist
    Given there is an nonexistent item
    When a GET request is sent to "/items/id.json"
    Then the response status code should be 404
    And the response should contain details of the error 404

  @api
  Scenario: Update Deposit (Using PUT)
    Given there is an existing item
    And have a updated item data
    When a PUT request is sent to "/items/id.json" with the updated data
    Then the response status code should be 200
    And the response should contain the updated item details

  @api
  Scenario: Update Deposit (Using PATCH)
    Given there is an existing item
    And have a updated item data
    When a PATCH request is sent to "/items/id.json" with the updated data
    Then the response status code should be 200
    And the response should contain the updated item details

  @api
  Scenario: Delete Deposit
    Given there is an existing item
    When a DELETE request is sent to "/items/id.json"
    Then the response status code should be 204
    And the item should be successfully deleted
