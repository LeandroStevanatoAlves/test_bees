from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.deposits_page import DepositsPage
from pages.deposit_new_page import DepositNewPage
from pages.deposit_show_page import DepositShowPage
from pages.items_page import ItemsPage
from pages.item_new_page import ItemNewPage
from pages.item_show_page import ItemShowPage
from pages.inventories_page import InventoriesPage
from pages.inventory_new_page import InventoryNewPage
from pages.inventory_show_page import InventoryShowPage
from utilities.tools import is_on_github_actions
from utilities.tools import is_selenium


def before_scenario(context, scenario):
    if is_selenium(context):
        options = webdriver.ChromeOptions()
        if is_on_github_actions():
            options.add_argument("--window-size=1920,1080")
            options.add_argument('--headless')
        else:
            options.add_argument('--start-maximized')
        context.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

        context.wait = WebDriverWait(context.driver, 10)

        context.login_page = LoginPage(context.driver, context.wait)
        context.home_page = HomePage(context.driver, context.wait)
        context.deposits_page = DepositsPage(context.driver, context.wait)
        context.deposit_new_page = DepositNewPage(context.driver, context.wait)
        context.deposit_show_page = DepositShowPage(context.driver, context.wait)
        context.items_page = ItemsPage(context.driver, context.wait)
        context.item_new_page = ItemNewPage(context.driver, context.wait)
        context.item_show_page = ItemShowPage(context.driver, context.wait)
        context.inventories_page = InventoriesPage(context.driver, context.wait)
        context.inventory_new_page = InventoryNewPage(context.driver, context.wait)
        context.inventory_show_page = InventoryShowPage(context.driver, context.wait)

    context.site_url = 'https://test-bees.herokuapp.com/'


def after_scenario(context, scenario):
    if is_selenium(context):
        context.driver.close()
