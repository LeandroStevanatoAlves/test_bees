import requests
from behave import *
from utilities.api_items import items_payload_factory
from utilities.api_items import items_updated_payload_factory
from utilities.api_deposits import deposits_payload_factory
from utilities.api_deposits import deposits_updated_payload_factory
from utilities.api_inventory import inventory_payload_factory
from utilities.api_inventory import inventory_updated_payload_factory


@when(u'a GET request is sent to "/inventories.json"')
def step_impl(context):
    context.response = requests.get(context.site_url + 'inventories.json')


@then(u'the response should contain a list of inventories')
def step_impl(context):
    # Check if the response is a list (array)
    assert isinstance(context.response.json(), list)


@given(u'the payload with necessary inventory data is prepared')
def step_impl(context):
    # Create a new item
    payload = items_payload_factory()
    response = requests.post(context.site_url + 'items.json', json=payload)
    response_data = response.json()
    # Get the new deposit ID
    context.item_id = response_data["id"]

    # Create a new deposit
    payload = deposits_payload_factory()
    response = requests.post(context.site_url + 'deposits.json', json=payload)
    response_data = response.json()
    # Get the new deposit ID
    context.deposit_id = response_data["id"]

    context.payload = inventory_payload_factory(context.item_id, context.deposit_id)


@when(u'a POST request is sent to "/inventories.json" with the inventory data')
def step_impl(context):
    context.response = requests.post(context.site_url + 'inventories.json', json=context.payload)


@then(u'the response should contain the created inventory details')
def step_impl(context):
    response_data = context.response.json()
    assert context.payload["item_id"] == response_data["item_id"]
    assert context.payload["deposit_id"] == response_data["deposit_id"]
    assert context.payload["item_count"] == response_data["item_count"]


@given(u'there is an existing inventory')
def step_impl(context):
    # Create a new item
    payload = items_payload_factory()
    response = requests.post(context.site_url + 'items.json', json=payload)
    response_data = response.json()
    # Get the new deposit ID
    context.item_id = response_data["id"]

    # Create a new deposit
    payload = deposits_payload_factory()
    response = requests.post(context.site_url + 'deposits.json', json=payload)
    response_data = response.json()
    # Get the new deposit ID
    context.deposit_id = response_data["id"]

    # Create a new inventory
    payload = inventory_payload_factory(context.item_id, context.deposit_id)
    response = requests.post(context.site_url + 'inventories.json', json=payload)
    response_data = response.json()
    # Get the new item ID
    context.inventory_id = response_data["id"]


@when(u'a GET request is sent to "/inventories/id.json"')
def step_impl(context):
    context.response = requests.get(context.site_url + 'inventories/' + str(context.inventory_id) + '.json')


@then(u'the response should contain inventory details')
def step_impl(context):
    response_data = context.response.json()
    assert context.inventory_id == response_data["id"]

    # Delete the new item, to keep the database clean
    requests.delete(context.site_url + 'inventories/' + str(context.inventory_id) + '.json')


@given(u'there is an nonexistent inventory')
def step_impl(context):
    context.inventory_id = 999999


@given(u'have a updated inventory data')
def step_impl(context):
    # Create a updated inventory data
    context.updated_payload = inventory_updated_payload_factory(context.item_id, context.deposit_id, context.inventory_id)


@when(u'a PUT request is sent to "/inventories/id.json" with the updated data')
def step_impl(context):
    context.response = requests.put(
        context.site_url + 'inventories/' + str(context.inventory_id) + '.json',
        json=context.updated_payload
    )


@then(u'the response should contain the updated inventory details')
def step_impl(context):
    response_data = context.response.json()
    assert context.updated_payload["item_id"] == response_data["item_id"]
    assert context.updated_payload["deposit_id"] == response_data["deposit_id"]
    assert context.updated_payload["item_count"] == response_data["item_count"]

    # Delete the new item, to keep the database clean
    requests.delete(context.site_url + 'inventories/' + str(context.inventory_id) + '.json')


@when(u'a PATCH request is sent to "/inventories/id.json" with the updated data')
def step_impl(context):
    context.response = requests.patch(
        context.site_url + 'inventories/' + str(context.inventory_id) + '.json',
        json=context.updated_payload
    )


@when(u'a DELETE request is sent to "/inventories/id.json"')
def step_impl(context):
    context.response = requests.delete(context.site_url + 'inventories/' + str(context.inventory_id) + '.json')


@then(u'the inventory should be successfully deleted')
def step_impl(context):
    # Try to get the item and expect to receive an error 404
    response = requests.get(context.site_url + 'inventories/' + str(context.inventory_id) + '.json')
    assert response.status_code == 404


