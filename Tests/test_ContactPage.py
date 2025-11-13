import pytest
from Pages.HomePage import HomePage
from Pages.ContactPage import ContactPage

def test_reviews_message_displayed(driver):
    homepage = HomePage(driver)
    homepage.open(HomePage.URL)
    homepage.click(HomePage.LINK_CONTACTS)
    driver.switch_to.window(driver.window_handles[-1])
    contact = ContactPage(driver)
    contact.click(ContactPage.ICON_PHONE)
    #contact.click(ContactPage.MODAL_WINDOW)
    expected_text = ContactPage.CONTACT_MODAL_TEXT
    actual_text = contact.get_text(ContactPage.MODAL_TEXT)

    assert actual_text == expected_text