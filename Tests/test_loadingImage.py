import pytest
from Pages.LoadingImage import LoadingImage

alt = "award"

@pytest.fixture
def loadingImg(driver):
    loadingImg = LoadingImage(driver)
    loadingImg.open(LoadingImage.URL)
    return loadingImg

def test_button_text_changes(loadingImg):
    loadingImg.is_displayed(LoadingImage.COMPASS)
    loadingImg.is_displayed(LoadingImage.CALENDAR)
    loadingImg.is_displayed(LoadingImage.AWARD)
    loadingImg.is_displayed(LoadingImage.LANDSCAPE)

    expected_text = alt
    actual_text = loadingImg.get_alt_attribute_by_index(LoadingImage.IMAGES, 3)
    assert actual_text == expected_text