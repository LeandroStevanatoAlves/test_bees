import time
from random import randrange
from behave import *


@given(u'the user is on the Inventories page')
def step_impl(context):
    context.login_page.open_page(context.site_url)
    context.login_page.enter_email('leandro.stevanato@gmail.com')
    context.login_page.enter_password('JKE9At9iQEHZ7at')
    context.login_page.click_submit_button()
    context.home_page.click_inventories_menu()


@given(u'clicks on New Inventory')
def step_impl(context):
    context.inventories_page.click_new_inventory_link()
    time.sleep(2)


@given(u'fill all fields of New Inventory form with valid information')
def step_impl(context):
    context.inventory_new_page.select_option_item_id('aaa')
    context.inventory_new_page.select_option_deposit_id('ABC')
    context.inventory_new_page.enter_item_count(str(randrange(1, 15)))
    time.sleep(2)


@when(u'clicks on Create Inventory button')
def step_impl(context):
    context.inventory_new_page.click_create_inventory_button()
    time.sleep(2)


@then(u'the user should see the "Inventory was successfully created." message')
def step_impl(context):
    assert context.inventory_show_page.inventory_created_message_text() == 'Inventory was successfully created.'
    # Destroys the created deposit, to keep the database clean
    context.inventory_show_page.click_destroy_inventory_button()
