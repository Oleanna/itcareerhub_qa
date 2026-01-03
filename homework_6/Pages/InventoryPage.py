from selenium.webdriver.common.by import By
from homework_6.Pages.BasePage import BasePage


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"

    SAUCE_LABS_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    SAUCE_LABS_BOLT_T_SHIRT = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    SAUCE_LABS_ONESIE = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")

    CART = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')

    def add_to_cart(self):
        self.click(self.SAUCE_LABS_BACKPACK)
        self.click(self.SAUCE_LABS_BOLT_T_SHIRT)
        self.click(self.SAUCE_LABS_ONESIE)

    def go_to_cart(self):
        self.click(self.CART)
