import pytest
from Pages.HomePage import HomePage

@pytest.fixture
def homepage(driver):
    homepage = HomePage(driver)
    homepage.open(HomePage.URL)
    return homepage

def test_logo_displayed(homepage):
    assert homepage.find(HomePage.LOGO)

def test_link_programs_displayed(homepage):
    assert homepage.is_displayed(HomePage.LINK_PROGRAMS)

def test_link_payment_displayed(homepage):
    assert homepage.is_displayed(HomePage.LINK_PAYMENT)

def test_link_about_displayed(homepage):
    assert homepage.is_displayed(HomePage.LINK_ABOUT)

def test_link_reviews_displayed(homepage):
    assert homepage.is_displayed(HomePage.LINK_REVIEWS)

def test_language_ru_buttons_displayed(homepage):
    assert homepage.is_displayed(HomePage.BUTTON_RU)

def test_language_de_buttons_displayed(homepage):
    assert homepage.is_displayed(HomePage.BUTTON_DE)

def test_language_switch_de(homepage):
    homepage.click(HomePage.BUTTON_DE)
    assert homepage.is_displayed(HomePage.LINK_PROGRAMS_DE)

def test_language_switch_ru(homepage):
    homepage.click(HomePage.BUTTON_DE)
    homepage.click(HomePage.BUTTON_RU)
    assert homepage.is_displayed(HomePage.LINK_PROGRAMS)