Feature: Endpoint /deposits

  @api
  Scenario: List Deposits
    When a GET request is sent to "/deposits.json"
    Then the response status code should be 200
    And the response should contain a list of deposits

  @api
  Scenario: Create a Deposit
    Given the payload with necessary deposit data is prepared
    When a POST request is sent to "/deposits.json" with the deposit data
    Then the response status code should be 201
    And the response should contain the created deposit details

  @api
  Scenario: Show Deposit Details
    Given there is an existing deposit
    When a GET request is sent to "/deposits/id.json"
    Then the response status code should be 200
    And the response should contain deposit details

  @api
  Scenario: Error When Try to Show Details of a Deposit That doesn't exist
    Given there is an nonexistent deposit
    When a GET request is sent to "/deposits/id.json"
    Then the response status code should be 404
    And the response should contain details of the error 404

  @api
  Scenario: Update Deposit (Using PUT)
    Given there is an existing deposit
    And have a updated deposit data
    When a PUT request is sent to "/deposits/id.json" with the updated data
    Then the response status code should be 200
    And the response should contain the updated deposit details

  @api
  Scenario: Update Deposit (Using PATCH)
    Given there is an existing deposit
    And have a updated deposit data
    When a PATCH request is sent to "/deposits/id.json" with the updated data
    Then the response status code should be 200
    And the response should contain the updated deposit details

  @api
  Scenario: Delete Deposit
    Given there is an existing deposit
    When a DELETE request is sent to "/deposits/id.json"
    Then the response status code should be 204
    And the deposit should be successfully deleted
