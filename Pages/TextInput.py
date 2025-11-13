from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class TextInput(BasePage):
    URL = "http://uitestingplayground.com/textinput"

    INPUT = (By.CSS_SELECTOR, "#newButtonName")
    BUTTON = (By.CSS_SELECTOR, "#updatingButton")
