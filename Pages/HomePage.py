from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):
    URL = "https://itcareerhub.de/ru"

    LOGO = (By.CSS_SELECTOR, "[alt='IT Career Hub']")
    LINK_PROGRAMS = (By.LINK_TEXT, "Программы")
    LINK_PAYMENT = (By.LINK_TEXT, "Способы оплаты")
    LINK_NEWS = (By.LINK_TEXT, "Новости")
    LINK_ABOUT = (By.LINK_TEXT, "О нас")
    LINK_REVIEWS = (By.LINK_TEXT, "Отзывы")
    LINK_CONTACTS = (By.LINK_TEXT, "Контакты")
    BUTTON_RU = (By.LINK_TEXT, "ru")
    BUTTON_DE = (By.LINK_TEXT, "de")
    LINK_PROGRAMS_DE = (By.LINK_TEXT, "Programme")




