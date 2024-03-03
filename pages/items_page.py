from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class ItemsPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.new_item_link = (By.LINK_TEXT, 'New item')

    def click_new_item_link(self):
        self.wait.until(ec.element_to_be_clickable(self.new_item_link)).click()
