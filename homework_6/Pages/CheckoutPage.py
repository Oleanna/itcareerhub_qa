from selenium.webdriver.common.by import By
from homework_6.Pages.BasePage import BasePage


class CheckoutPage(BasePage):
    URL = "https://www.saucedemo.com/checkout-step-one.html"

    INPUT_FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    INPUT_LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    INPUT_POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    BUTTON_CONTINUE = (By.CSS_SELECTOR, "#continue")

    TEXT_TOTAL = (By.CSS_SELECTOR, '[data-test="total-label"]')

    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        self.input_text(self.INPUT_FIRST_NAME, first_name)
        self.input_text(self.INPUT_LAST_NAME, last_name)
        self.input_text(self.INPUT_POSTAL_CODE, postal_code)

    def get_total_amount(self):
        return self.find(self.TEXT_TOTAL).text.replace('Total: ', '')


