from selenium.webdriver.common.by import By
from homework_6.Pages.BasePage import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"

    INPUT_USERNAME = (By.CSS_SELECTOR, "#user-name")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "#login-button")


    def login(self, username, password):
        self.input_text(self.INPUT_USERNAME, username)
        self.input_text(self.INPUT_PASSWORD, password)
        self.click(self.BUTTON_LOGIN)