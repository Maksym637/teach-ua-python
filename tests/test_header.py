from tests.base_test import configure_browser
from teachua.pages.home_page import HomePage


def test_header_example(configure_browser):
    home_page = HomePage(configure_browser)
    home_page.get_header().click_user_icon()
