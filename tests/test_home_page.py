from tests.base_test import configure_browser
from teachua.pages.home_page import HomePage


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
