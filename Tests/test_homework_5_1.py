from time import sleep

import pytest
from Pages.HandsOn import HandOn

text = "semper posuere integer et senectus justo curabitur"

def test_check_text(driver):
    handonpage = HandOn(driver)
    handonpage.open(HandOn.URL)
    handonpage.switch_to_frame(HandOn.IFRAME)
    paragraphs = handonpage.find_all(HandOn.TEXT)
    assert any(
        text in p.text for p in paragraphs
    )
