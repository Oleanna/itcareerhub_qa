import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from Lesson6s.pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    yield driver
    driver.quit()

def test_successful_login(driver):
   login_page = LoginPage(driver)
   login_page.enter_username("standard_user")
   login_page.enter_password("secret_sauce")
   login_page.click_on_login_button()
   assert "inventory.html" in driver.current_url, "Не удалось войти в систему."

def test_invalid_password(driver):
   login_page = LoginPage(driver)
   login_page.enter_username("standard_user")
   login_page.enter_password("wrong_password")
   login_page.click_on_login_button()
   assert "Username and password do not match" in login_page.error_message().text, "Неверное сообщение об ошибке."

def test_locked_out_user(driver):
   login_page = LoginPage(driver)
   login_page.enter_username("locked_out_user")
   login_page.enter_password("secret_sauce")
   login_page.click_on_login_button()
   assert "Sorry, this user has been locked out." in login_page.error_message().text, "Неверное сообщение об ошибке."

def test_empty_username(driver):
   login_page = LoginPage(driver)
   login_page.enter_password("secret_sauce")
   login_page.click_on_login_button()
   assert "Username is required" in login_page.error_message().text, "Неверное сообщение об ошибке."

def test_empty_password(driver):
   login_page = LoginPage(driver)
   login_page.enter_username("standard_user")
   login_page.click_on_login_button()
   assert "Password is required" in login_page.error_message().text, "Неверное сообщение об ошибке."
