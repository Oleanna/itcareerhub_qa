from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HandOn(BasePage):
    URL = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"

    IFRAME = (By.CSS_SELECTOR, "#my-iframe")

    TEXT = (By.CSS_SELECTOR, "#content > p")

