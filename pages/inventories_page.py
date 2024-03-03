from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class InventoriesPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.new_inventory_link = (By.LINK_TEXT, 'New inventory')

    def click_new_inventory_link(self):
        self.wait.until(ec.element_to_be_clickable(self.new_inventory_link)).click()
