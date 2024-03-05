from random import randrange

import requests
from behave import *
from utilities.api_deposits import deposits_payload_factory
from utilities.api_items import items_payload_factory


@given(u'the user is on the Inventories page')
def step_impl(context):
    # Create a new item
    payload = items_payload_factory()
    response = requests.post(context.site_url + 'items.json', json=payload)
    response_data = response.json()
    # Get the new deposit ID
    context.item_id = response_data["id"]
    context.item_name = response_data["name"]

    # Create a new deposit
    payload = deposits_payload_factory()
    response = requests.post(context.site_url + 'deposits.json', json=payload)
    response_data = response.json()
    # Get the new deposit ID
    context.deposit_id = response_data["id"]
    context.deposit_name = response_data["name"]

    context.login_page.open_page(context.site_url)
    context.login_page.enter_email('leandro.stevanato@gmail.com')
    context.login_page.enter_password('JKE9At9iQEHZ7at')
    context.login_page.click_submit_button()
    context.home_page.click_inventories_menu()


@given(u'clicks on New Inventory')
def step_impl(context):
    context.inventories_page.click_new_inventory_link()


@given(u'fill all fields of New Inventory form with valid information')
def step_impl(context):
    context.inventory_new_page.select_option_item_id(context.item_name)
    context.inventory_new_page.select_option_deposit_id(context.deposit_name)
    context.inventory_new_page.enter_item_count(str(randrange(1, 15)))


@when(u'clicks on Create Inventory button')
def step_impl(context):
    context.inventory_new_page.click_create_inventory_button()


@then(u'the user should see the "Inventory was successfully created." message')
def step_impl(context):
    assert context.inventory_show_page.inventory_created_message_text() == 'Inventory was successfully created.'
    # Destroys the created deposit, to keep the database clean
    context.inventory_show_page.click_destroy_inventory_button()

    # delete data
    requests.delete(context.site_url + 'items/' + str(context.item_id) + '.json')
    requests.delete(context.site_url + 'deposits/' + str(context.deposit_id) + '.json')
