from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class DepositShowPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.deposit_created_message = (By.XPATH, '/html/body/div/p')
        self.edit_deposit_link = (By.LINK_TEXT, 'Edit this deposit')
        self.back_to_deposits_link = (By.LINK_TEXT, 'Back to deposits')
        self.destroy_deposit_button = (By.CSS_SELECTOR, "button[type='submit']")

    def deposit_created_message_text(self) -> str:
        return self.wait.until(ec.visibility_of_element_located(self.deposit_created_message)).text

    def click_edit_deposit_link(self):
        self.wait.until(ec.element_to_be_clickable(self.edit_deposit_link)).click()

    def click_back_to_deposits_link(self):
        self.wait.until(ec.element_to_be_clickable(self.back_to_deposits_link)).click()

    def click_destroy_deposit_button(self):
        self.wait.until(ec.element_to_be_clickable(self.destroy_deposit_button)).click()
