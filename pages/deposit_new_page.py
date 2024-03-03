from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class DepositNewPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.name_field = (By.ID, 'deposit_name')
        self.address_field = (By.ID, 'deposit_address')
        self.city_field = (By.ID, 'deposit_city')
        self.state_field = (By.ID, 'deposit_state')
        self.zipcode_field = (By.ID, 'deposit_zipcode')
        self.create_deposit_button = (By.NAME, 'commit')
        self.back_to_deposits_link = (By.LINK_TEXT, 'Back to deposits')

    def enter_name(self, name):
        self.wait.until(ec.element_to_be_clickable(self.name_field)).send_keys(name)

    def enter_address(self, address):
        self.wait.until(ec.element_to_be_clickable(self.address_field)).send_keys(address)

    def enter_city(self, city):
        self.wait.until(ec.element_to_be_clickable(self.city_field)).send_keys(city)

    def enter_state(self, state):
        self.wait.until(ec.element_to_be_clickable(self.state_field)).send_keys(state)

    def enter_zipcode(self, zipcode):
        self.wait.until(ec.element_to_be_clickable(self.zipcode_field)).send_keys(zipcode)

    def click_create_deposit_button(self):
        self.wait.until(ec.element_to_be_clickable(self.create_deposit_button)).click()

    def click_back_to_deposits_link(self):
        self.wait.until(ec.element_to_be_clickable(self.back_to_deposits_link)).click()
