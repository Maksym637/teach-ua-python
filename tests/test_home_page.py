from tests.base_test import BaseTest
from teachua.pages.home_page import HomePage


class TestHomePage(BaseTest):

    def test_login_valid(self):
        home_page = HomePage(self.driver)

        home_page.header \
            .move_to_guest_menu() \
            .click_register_button() \
            .enter_last_name("user") \
            .enter_first_name("user") \
            .enter_phone("0121212121") \
            .enter_email("user@gmail.com") \
            .enter_password("Auser_123") \
            .confirm_password("Auser_123") \
            .click_close_button()
        
        last_name_value = home_page.header \
            .move_to_guest_menu() \
            .click_register_button() \
            .get_last_name_value()
        
        print(last_name_value)
