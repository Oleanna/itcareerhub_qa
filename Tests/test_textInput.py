import pytest
from Pages.TextInput import TextInput

text = "ITCH"

@pytest.fixture
def textinput(driver):
    textinput = TextInput(driver)
    textinput.open(TextInput.URL)
    return textinput

def test_button_text_changes(textinput):
    textinput.input_text(TextInput.INPUT, text)
    textinput.click(TextInput.BUTTON)
    expected_text = text
    actual_text = textinput.get_text(TextInput.BUTTON)

    assert actual_text == expected_text

