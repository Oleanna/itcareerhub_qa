from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pytest

URL = "https://itcareerhub.de/ru"
PAYMENT_LINK = (By.LINK_TEXT, "Способы оплаты")
CONSULT_BUTTON = (By.LINK_TEXT, "ПОЛУЧИТЬ КОНСУЛЬТАЦИЮ")
PAYMENT_BLOCK = (By.CSS_SELECTOR, "#rec1345258701 > div > div > div.t396__filter")
SCREENSHOT_DIR = Path("./screenshots")
SCREENSHOT_DIR.mkdir(exist_ok=True)

date_str = datetime.now().strftime("%d_%m_%y_%H_%M_%S")

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_payment_block(driver):
    driver.get(URL)
    driver.find_element(*PAYMENT_LINK).click()
    assert driver.find_element(*CONSULT_BUTTON).is_displayed()
    driver.find_element(*PAYMENT_BLOCK).screenshot(str(SCREENSHOT_DIR/f"payment_block_{date_str}.png"))
