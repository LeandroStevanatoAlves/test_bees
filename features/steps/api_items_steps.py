import requests
from behave import *
from utilities.api_items import items_payload_factory
from utilities.api_items import items_updated_payload_factory


@when(u'a GET request is sent to "/items.json"')
def step_impl(context):
    context.response = requests.get(context.site_url + 'items.json')


@then(u'the response should contain a list of items')
def step_impl(context):
    # Check if the response is a list (array)
    assert isinstance(context.response.json(), list)


@given(u'the payload with necessary item data is prepared')
def step_impl(context):
    context.payload = items_payload_factory()


@when(u'a POST request is sent to "/items.json" with the item data')
def step_impl(context):
    context.response = requests.post(context.site_url + 'items.json', json=context.payload)


@then(u'the response should contain the created item details')
def step_impl(context):
    response_data = context.response.json()
    assert context.payload["name"] == response_data["name"]
    assert context.payload["height"] + ".0" == response_data["height"]
    assert context.payload["width"] + ".0" == response_data["width"]
    assert context.payload["weight"] + ".0" == response_data["weight"]


@given(u'there is an existing item')
def step_impl(context):
    # Create a new item
    payload = items_payload_factory()
    response = requests.post(context.site_url + 'items.json', json=payload)
    response_data = response.json()
    # Get the new item ID
    context.item_id = response_data["id"]


@when(u'a GET request is sent to "/items/id.json"')
def step_impl(context):
    context.response = requests.get(context.site_url + 'items/' + str(context.item_id) + '.json')


@then(u'the response should contain item details')
def step_impl(context):
    response_data = context.response.json()
    assert context.item_id == response_data["id"]

    # Delete the new item, to keep the database clean
    requests.delete(context.site_url + 'items/' + str(context.item_id) + '.json')


@given(u'there is an nonexistent item')
def step_impl(context):
    context.item_id = 999999


@given(u'have a updated item data')
def step_impl(context):
    # Create a updated item data
    context.updated_payload = items_updated_payload_factory(context.item_id)


@when(u'a PUT request is sent to "/items/id.json" with the updated data')
def step_impl(context):
    context.response = requests.put(
        context.site_url + 'items/' + str(context.item_id) + '.json',
        json=context.updated_payload
    )


@then(u'the response should contain the updated item details')
def step_impl(context):
    response_data = context.response.json()
    assert context.updated_payload["name"] == response_data["name"]
    assert context.updated_payload["height"] + ".0" == response_data["height"]
    assert context.updated_payload["width"] + ".0" == response_data["width"]
    assert context.updated_payload["weight"] + ".0" == response_data["weight"]

    # Delete the new item, to keep the database clean
    requests.delete(context.site_url + 'items/' + str(context.item_id) + '.json')


@when(u'a PATCH request is sent to "/items/id.json" with the updated data')
def step_impl(context):
    context.response = requests.patch(
        context.site_url + 'items/' + str(context.item_id) + '.json',
        json=context.updated_payload
    )


@when(u'a DELETE request is sent to "/items/id.json"')
def step_impl(context):
    context.response = requests.delete(context.site_url + 'items/' + str(context.item_id) + '.json')


@then(u'the item should be successfully deleted')
def step_impl(context):
    # Try to get the item and expect to receive an error 404
    response = requests.get(context.site_url + 'items/' + str(context.item_id) + '.json')
    assert response.status_code == 404
