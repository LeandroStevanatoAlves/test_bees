from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as ec


class InventoryNewPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.item_id_select = (By.ID, 'inventory_item_id')
        self.deposit_id_select = (By.ID, 'inventory_deposit_id')
        self.item_count_field = (By.ID, 'inventory_item_count')
        self.create_inventory_button = (By.NAME, 'commit')
        self.back_to_inventories_link = (By.LINK_TEXT, 'Back to inventories')


    def select_option_item_id(self, text):
        Select(self.wait.until(ec.element_to_be_clickable(self.item_id_select))).select_by_visible_text(text)
        #select_element = driver.find_element(By.NAME, 'selectomatic')
        #select = Select(select_element)
        #select.select_by_visible_text('Four')
        # select.select_by_visible_text('Four')

    def select_option_deposit_id(self, text):
        Select(self.wait.until(ec.element_to_be_clickable(self.deposit_id_select))).select_by_visible_text(text)

    def enter_item_count(self, item_count):
        self.wait.until(ec.element_to_be_clickable(self.item_count_field)).send_keys(item_count)

    def click_create_inventory_button(self):
        self.wait.until(ec.element_to_be_clickable(self.create_inventory_button)).click()

    def click_back_to_inventories_link(self):
        self.wait.until(ec.element_to_be_clickable(self.back_to_inventories_link)).click()
