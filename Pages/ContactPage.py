from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class ContactPage(BasePage):
    URL = "https://itcareerhub.de/ru/contact-us"

    BUTTON_CALLBACK = (By.LINK_TEXT, "ОБРАТНЫЙ ЗВОНОК")
    ICON_PHONE = (By.CSS_SELECTOR, '[src="https://static.tildacdn.net/tild3933-3337-4237-a439-336463393463/Group_3800.svg"]')
    PHONE_TEXT = (By.LINK_TEXT, "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами")
    MODAL_WINDOW = (By.CSS_SELECTOR, "#rec1194983686")
    MODAL_TEXT = (By.CSS_SELECTOR, "#rec1194983686 > div > div > div.t396__elem.tn-elem.tn-elem__11949836861711363912027 > div")

    CONTACT_MODAL_TEXT = "Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"
