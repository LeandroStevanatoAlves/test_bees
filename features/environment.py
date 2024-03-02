from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.home_page import HomePage


def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    context.site_url = 'https://test-bees.herokuapp.com/'

    context.login_page = LoginPage(context.driver)
    context.home_page = HomePage(context.driver)


def after_scenario(context, scenario):
    context.driver.close()
