import time
from random import randrange
from behave import *


@given(u'the user is on the Items page')
def step_impl(context):
    context.login_page.open_page(context.site_url)
    context.login_page.enter_email('leandro.stevanato@gmail.com')
    context.login_page.enter_password('JKE9At9iQEHZ7at')
    context.login_page.click_submit_button()
    context.home_page.click_items_menu()


@given(u'clicks on New Item')
def step_impl(context):
    context.items_page.click_new_item_link()


@given(u'fill all fields of New Item form with valid information')
def step_impl(context):
    context.item_new_page.enter_name("Item " + str(randrange(1, 20)))
    context.item_new_page.enter_height(str(randrange(1, 15)))
    context.item_new_page.enter_width(str(randrange(1, 15)))
    context.item_new_page.enter_weight(str(randrange(1, 15)))
    time.sleep(2)


@when(u'clicks on Create Item button')
def step_impl(context):
    context.item_new_page.click_create_item_button()


@then(u'the user should see the "Item was successfully created." message')
def step_impl(context):
    assert context.item_show_page.item_created_message_text() == 'Item was successfully created.'
    # Destroys the created deposit, to keep the database clean
    context.item_show_page.click_destroy_item_button()
