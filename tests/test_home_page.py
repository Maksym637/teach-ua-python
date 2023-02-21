from tests.base_test import BaseTest
from teachua.pages.home_page import HomePage


class TestHomePage(BaseTest):

    def test_login_valid(self):
        home_page = HomePage(self.driver)

        home_page.header \
            .move_to_guest_menu() \
            .click_login_button() \
            .enter_email("admin@gmail.com") \
            .enter_password("admin") \
            .click_sign_in()
