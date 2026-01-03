from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class ContactPage(BasePage):
    URL = "https://bonigarcia.dev/selenium-webdriver-java/iframes.html"

    IFRAME = (By.CSS_SELECTOR, "#my-iframe")

    PHONE_TEXT = (By.LINK_TEXT, "#content > p:nth-child(2)")

