import pytest

from pages.home_page import HomePage


def test_temperature_conversion(driver):
    home_page = HomePage(driver)
    home_page.click_button(home_page.accept_cookies_button)
    home_page.click_button(home_page.temperature_button)
    home_page.close_add()
    # home_page.click_button(home_page.dismiss_add_button)
    home_page.select_from_dropdown("unitFrom", "Celsius")

    home_page.click_button(home_page.temperature_button)
    # login_page.execute_login(get_data["username"], get_data["password"])
    # assert login_page.actual_error() == "Invalid credentials", "Error message does not match expected value"


# def test_login_negative(driver, get_data):
#     login_page = LoginPage(driver)
#     login_page.execute_login(get_data["username"], get_data["password"])
#     assert login_page.actual_error() == "Invalid credentials", "Error message does not match expected value"

#
#
# @pytest.fixture(params=[{"username": "admin", "password": "admin$$"},
#                         {"username": "Admin123", "password": "123"}])
# def get_data(request):
#     return request.param
