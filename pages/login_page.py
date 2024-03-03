from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.email_field = (By.ID, 'user_email')
        self.password_field = (By.ID, 'user_password')
        self.submit_button = (By.NAME, 'commit')

    def open_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.wait.until(ec.element_to_be_clickable(self.email_field)).send_keys(email)

    def enter_password(self, password):
        self.wait.until(ec.element_to_be_clickable(self.password_field)).send_keys(password)

    def click_submit_button(self):
        self.wait.until(ec.element_to_be_clickable(self.submit_button)).click()
