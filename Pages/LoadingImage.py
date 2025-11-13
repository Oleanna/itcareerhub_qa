from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class LoadingImage(BasePage):
    URL = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"

    COMPASS = (By.CSS_SELECTOR, "#compass")
    CALENDAR = (By.CSS_SELECTOR, "#calendar")
    AWARD = (By.CSS_SELECTOR, "#award")
    LANDSCAPE = (By.CSS_SELECTOR, "#landscape")
    IMAGES = (By.TAG_NAME, "img")