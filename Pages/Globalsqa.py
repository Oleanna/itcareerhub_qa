from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class GlobalsQa(BasePage):
    URL = "https://www.globalsqa.com/demo-site/draganddrop/"

    IFRAME = (By.CSS_SELECTOR, "iframe.demo-frame")
    IMAGES = (By.CSS_SELECTOR, "#gallery > li")
    TRASH = (By.CSS_SELECTOR, "#trash")
    IMAGES_TRASH = (By.CSS_SELECTOR, "#trash > ul > li")

    CONSENT = (By.CSS_SELECTOR, ".fc-cta-consent")

