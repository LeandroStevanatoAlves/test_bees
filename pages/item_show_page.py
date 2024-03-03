from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class ItemShowPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.item_created_message = (By.XPATH, '/html/body/div/p')
        self.edit_item_link = (By.LINK_TEXT, 'Edit this item')
        self.back_to_items_link = (By.LINK_TEXT, 'Back to items')
        self.destroy_item_button = (By.XPATH, '/html/body/div/div[2]/form/button')

    def item_created_message_text(self) -> str:
        return self.wait.until(ec.visibility_of_element_located(self.item_created_message)).text

    def click_edit_item_link(self):
        self.wait.until(ec.element_to_be_clickable(self.edit_item_link)).click()

    def click_back_to_items_link(self):
        self.wait.until(ec.element_to_be_clickable(self.back_to_items_link)).click()

    def click_destroy_item_button(self):
        self.wait.until(ec.element_to_be_clickable(self.destroy_item_button)).click()
