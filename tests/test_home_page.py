from tests.base_test import configure_browser
from teachua.pages.home_page import HomePage
from tests.test_data.data_home_page import data_login_invalid
import pytest


def test_login_valid(configure_browser):
    home_page = HomePage(configure_browser)

    expected_message = "Ви успішно залогувалися!"
    actual_message = home_page \
        .move_to_header() \
        .click_user_icon() \
        .click_login_button() \
        .enter_email("admin@gmail.com") \
        .enter_password("admin") \
        .click_sign_in() \
        .get_success_message()

    assert actual_message == expected_message


@pytest.mark.parametrize("email,password,expected_message", data_login_invalid)
def test_login_invalid(configure_browser, email, password, expected_message):
    home_page = HomePage(configure_browser)

    actual_message = home_page \
        .move_to_header() \
        .click_user_icon() \
        .click_login_button() \
        .enter_email(email) \
        .enter_password(password) \
        .click_sign_in() \
        .get_error_message()
    
    assert actual_message == expected_message
