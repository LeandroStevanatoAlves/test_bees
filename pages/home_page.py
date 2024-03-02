from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.deposits_menu = (By.LINK_TEXT, 'Deposits')
        self.items_menu = (By.LINK_TEXT, 'Items')
        self.inventories_menu = (By.LINK_TEXT, 'Inventory')
        self.logout_button = (By.CSS_SELECTOR, 'btn-danger')
        self.signed_in_message = (By.TAG_NAME, 'p')
        self.welcome_message = (By.TAG_NAME, 'h1')


    def click_deposits_menu(self):
        self.driver.find_element(*self.deposits_menu).click()

    def click_items_menu(self):
        self.driver.find_element(*self.items_menu).click()

    def click_inventories_menu(self):
        self.driver.find_element(*self.inventories_menu).click()

    def click_logout_button(self):
        self.driver.find_element(*self.logout_button).click()

    def welcome_message_text(self) -> str:
        return self.driver.find_element(*self.welcome_message).text
