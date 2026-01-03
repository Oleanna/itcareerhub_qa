from time import sleep

import pytest
from Pages.Globalsqa import GlobalsQa


def test_drag_and_drop(driver):
    global_page = GlobalsQa(driver)
    global_page.open(GlobalsQa.URL)
    global_page.click(GlobalsQa.CONSENT)
    global_page.switch_to_frame(GlobalsQa.IFRAME)
    first_image = global_page.find_all(GlobalsQa.IMAGES)[0]
    trash = global_page.find(GlobalsQa.TRASH)
    global_page.drag_and_drop(first_image, trash)

    trash_images = global_page.find_all(GlobalsQa.IMAGES_TRASH)
    gallery_images = global_page.find_all(GlobalsQa.IMAGES)
    assert len(trash_images) == 1 and len(gallery_images) == 3