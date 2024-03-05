import requests
from behave import *
from utilities.api_deposits import deposits_payload_factory
from utilities.api_deposits import deposits_updated_payload_factory


@when(u'a GET request is sent to "/deposits.json"')
def step_impl(context):
    context.response = requests.get(context.site_url + 'deposits.json')


@then(u'the response status code should be {response_code}')
def step_impl(context, response_code):
    assert context.response.status_code == int(response_code)


@then(u'the response should contain a list of deposits')
def step_impl(context):
    # Check if the response is a list (array)
    assert isinstance(context.response.json(), list)


@given(u'the payload with necessary deposit data is prepared')
def step_impl(context):
    context.payload = deposits_payload_factory()


@when(u'a POST request is sent to "/deposits.json" with the deposit data')
def step_impl(context):
    context.response = requests.post(context.site_url + 'deposits.json', json=context.payload)


@then(u'the response should contain the created deposit details')
def step_impl(context):
    response_data = context.response.json()
    assert context.payload["name"] == response_data["name"]
    assert context.payload["address"] == response_data["address"]
    assert context.payload["city"] == response_data["city"]
    assert context.payload["state"] == response_data["state"]
    assert context.payload["zipcode"] == response_data["zipcode"]


@given(u'there is an existing deposit')
def step_impl(context):
    # Create a new deposit
    payload = deposits_payload_factory()
    response = requests.post(context.site_url + 'deposits.json', json=payload)
    response_data = response.json()
    # Get the new deposit ID
    context.deposit_id = response_data["id"]

@given(u'there is an nonexistent deposit')
def step_impl(context):
    context.deposit_id = 999999


@when(u'a GET request is sent to "/deposits/id.json"')
def step_impl(context):
    context.response = requests.get(context.site_url + 'deposits/' + str(context.deposit_id) + '.json')


@then(u'the response should contain deposit details')
def step_impl(context):
    response_data = context.response.json()
    assert context.deposit_id == response_data["id"]

    # Delete the new deposit, to keep the database clean
    requests.delete(context.site_url + 'deposits/' + str(context.deposit_id) + '.json')


@given(u'have a updated deposit data')
def step_impl(context):
    # Create a updated deposit data
    context.updated_payload = deposits_updated_payload_factory(context.deposit_id)


@when(u'a PUT request is sent to "/deposits/id.json" with the updated data')
def step_impl(context):
    context.response = requests.put(
        context.site_url + 'deposits/' + str(context.deposit_id) + '.json',
        json=context.updated_payload
    )


@when(u'a PATCH request is sent to "/deposits/id.json" with the updated data')
def step_impl(context):
    context.response = requests.patch(
        context.site_url + 'deposits/' + str(context.deposit_id) + '.json',
        json=context.updated_payload
    )


@then(u'the response should contain the updated deposit details')
def step_impl(context):
    response_data = context.response.json()
    assert context.updated_payload["name"] == response_data["name"]
    assert context.updated_payload["address"] == response_data["address"]
    assert context.updated_payload["city"] == response_data["city"]
    assert context.updated_payload["state"] == response_data["state"]
    assert context.updated_payload["zipcode"] == response_data["zipcode"]

    # Delete the new deposit, to keep the database clean
    requests.delete(context.site_url + 'deposits/' + str(context.deposit_id) + '.json')


@then(u'the response should contain details of the error 404')
def step_impl(context):
    response_data = context.response.json()
    assert response_data["status"] == 404
    assert response_data["error"] == "Not Found"


@when(u'a DELETE request is sent to "/deposits/id.json"')
def step_impl(context):
    context.response = requests.delete(context.site_url + 'deposits/' + str(context.deposit_id) + '.json')


@then(u'the deposit should be successfully deleted')
def step_impl(context):
    # Try to get the deposit and expect to receive an error 404
    response = requests.get(context.site_url + 'deposits/' + str(context.deposit_id) + '.json')
    assert response.status_code == 404
