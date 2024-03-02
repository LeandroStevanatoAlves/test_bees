from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, 'user_email')
        self.password_field = (By.ID, 'user_password')
        self.submit_button = (By.NAME, 'commit')

    def open_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()
