from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class ItemNewPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.name_field = (By.ID, 'item_name')
        self.height_field = (By.ID, 'item_height')
        self.width_field = (By.ID, 'item_width')
        self.weight_field = (By.ID, 'item_weight')
        self.create_item_button = (By.NAME, 'commit')
        self.back_to_items_link = (By.LINK_TEXT, 'Back to items')

    def enter_name(self, name):
        self.wait.until(ec.element_to_be_clickable(self.name_field)).send_keys(name)

    def enter_height(self, height):
        self.wait.until(ec.element_to_be_clickable(self.height_field)).send_keys(height)

    def enter_width(self, width):
        self.wait.until(ec.element_to_be_clickable(self.width_field)).send_keys(width)

    def enter_weight(self, weight):
        self.wait.until(ec.element_to_be_clickable(self.weight_field)).send_keys(weight)

    def click_create_item_button(self):
        self.wait.until(ec.element_to_be_clickable(self.create_item_button)).click()

    def click_back_to_items_link(self):
        self.wait.until(ec.element_to_be_clickable(self.back_to_items_link)).click()
