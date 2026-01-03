from homework_6.Pages.LoginPage import LoginPage
from homework_6.Pages.CartPage import CartPage
from homework_6.Pages.CheckoutPage import CheckoutPage
from homework_6.Pages.InventoryPage import InventoryPage

username = "standard_user"
password = "secret_sauce"
first_name = "alex"
last_name = "alex"
postal_code = "11111"
expected_amount = "$58.29"

def test_check_total_amount(driver):
    login_page = LoginPage(driver)
    login_page.open(LoginPage.URL)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click(CartPage.BUTTON_CHECKOUT)

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form(first_name=first_name, last_name=last_name, postal_code=postal_code)
    checkout_page.click(CheckoutPage.BUTTON_CONTINUE)

    actual_amount = checkout_page.get_total_amount()
    assert actual_amount == expected_amount
