from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.deposits_page import DepositsPage
from pages.new_deposit_page import NewDepositPage
from pages.show_deposit_page import ShowDepositPage


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    context.wait = WebDriverWait(context.driver, 10)

    context.site_url = 'https://test-bees.herokuapp.com/'

    context.login_page = LoginPage(context.driver)
    context.home_page = HomePage(context.driver, context.wait)
    context.deposits_page = DepositsPage(context.driver, context.wait)
    context.new_deposits_page = NewDepositPage(context.driver, context.wait)
    context.show_deposit_page = ShowDepositPage(context.driver, context.wait)


def after_scenario(context, scenario):
    context.driver.close()
