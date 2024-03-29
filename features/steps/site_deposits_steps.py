from behave import *
from faker import Faker
from selenium.webdriver import ActionChains, Keys


@given(u'the user is on the deposits page')
def step_impl(context):
    context.login_page.open_page(context.site_url)
    context.login_page.enter_email('leandro.stevanato@gmail.com')
    context.login_page.enter_password('JKE9At9iQEHZ7at')
    context.login_page.click_submit_button()
    context.home_page.click_deposits_menu()


@given(u'clicks on New Deposit')
def step_impl(context):
    ActionChains(context.driver).key_down(Keys.END).perform()
    context.deposits_page.click_new_deposit_link()


@given(u'fill all fields with valid information')
def step_impl(context):
    fake = Faker('pt_BR')
    context.deposit_new_page.enter_name(fake.name())
    context.deposit_new_page.enter_address(fake.street_address())
    context.deposit_new_page.enter_city(fake.city())
    context.deposit_new_page.enter_state(fake.estado_sigla())
    context.deposit_new_page.enter_zipcode(fake.postcode())


@when(u'clicks on create deposit button')
def step_impl(context):
    context.deposit_new_page.click_create_deposit_button()


@then(u'the user should see the "Deposit was successfully created." message')
def step_impl(context):
    assert context.deposit_show_page.deposit_created_message_text() == 'Deposit was successfully created.'
    # Destroys the created deposit, to keep the database clean
    context.deposit_show_page.click_destroy_deposit_button()
