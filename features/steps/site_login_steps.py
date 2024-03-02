from behave import *


@given(u'the user is on the login page')
def step_impl(context):
    context.login_page.open_page(context.site_url)


@given(u'enters valid credentials')
def step_impl(context):
    context.login_page.enter_email('leandro.stevanato@gmail.com')
    context.login_page.enter_password('JKE9At9iQEHZ7at')


@given(u'enters invalid email')
def step_impl(context):
    context.login_page.enter_email('error@gmail.com')
    context.login_page.enter_password('JKE9At9iQEHZ7at')


@given(u'enters invalid password')
def step_impl(context):
    context.login_page.enter_email('leandro.stevanato@gmail.com')
    context.login_page.enter_password('123456')


@when(u'clicks the login button')
def step_impl(context):
    context.login_page.click_submit_button()


@then(u'the user should see the "Welcome to your storage" message')
def step_impl(context):
    assert context.home_page.welcome_message_text() == 'Welcome to your storage'


@then(u'the user should stay on login page')
def step_impl(context):
    assert context.driver.current_url == context.site_url + 'users/sign_in'
