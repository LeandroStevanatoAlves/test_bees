from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class DepositsPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.new_deposit_link = (By.LINK_TEXT, 'New deposit')
        #<p style="color: green">Deposit was successfully destroyed.</p>
        #self.deposits_menu = (By.LINK_TEXT, 'Deposits')
        #self.items_menu = (By.LINK_TEXT, 'Items')
        #self.signed_in_message = (By.TAG_NAME, 'p')
        #self.welcome_message = (By.TAG_NAME, 'h1')

    def click_new_deposit_link(self):
        self.wait.until(ec.element_to_be_clickable(self.new_deposit_link)).click()
