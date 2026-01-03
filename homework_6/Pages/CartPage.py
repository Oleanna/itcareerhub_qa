from selenium.webdriver.common.by import By
from homework_6.Pages.BasePage import BasePage


class CartPage(BasePage):
    URL = "https://www.saucedemo.com/cart.html"

    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "#checkout")
