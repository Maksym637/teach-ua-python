from tests.base_test import BaseTest
from teachua.pages.home_page import HomePage


class TestHomePage(BaseTest):

    def test_login_valid(self):
        home_page = HomePage(self.driver)

        success_message = home_page.header \
            .click_user_icon() \
            .click_login_button() \
            .enter_email("admin@gmail.com") \
            .enter_password("admin") \
            .click_sign_in() \
            .get_success_message()
        
        self.assertEqual(success_message, "Ви успішно залогувалися!")
    
    def test_login_invalid(self):
        pass

