from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class HomePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.deposits_menu = (By.LINK_TEXT, 'Deposits')
        self.items_menu = (By.LINK_TEXT, 'Items')
        self.inventories_menu = (By.LINK_TEXT, 'Inventory')
        self.logout_button = (By.CSS_SELECTOR, 'btn-danger')
        self.signed_in_message = (By.TAG_NAME, 'p')
        self.welcome_message = (By.TAG_NAME, 'h1')

    def click_deposits_menu(self):
        self.wait.until(ec.element_to_be_clickable(self.deposits_menu)).click()

    def click_items_menu(self):
        self.wait.until(ec.element_to_be_clickable(self.items_menu)).click()

    def click_inventories_menu(self):
        self.wait.until(ec.element_to_be_clickable(self.inventories_menu)).click()

    def click_logout_button(self):
        self.wait.until(ec.element_to_be_clickable(self.logout_button)).click()

    def welcome_message_text(self) -> str:
        return self.wait.until(ec.visibility_of_element_located(self.welcome_message)).text
