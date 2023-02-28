from tests.base_test import BaseTest
from teachua.pages.home_page import HomePage
from teachua.components.register_component import RegistrationComponent
from parameterized import parameterized


class TestHomePage(BaseTest):

    """Implementation of TUA-454
    """
    @parameterized.expand([
        ("firstUser", "firstUser", "0121212121", "user1@gmail.com", "User_111", "User_111",
         {"last_name": "firstUser", "first_name": "firstUser", "phone": "0121212121", 
          "email": "user1@gmail.com", "password": "User_111", "confirmation": "User_111"}),
    ])
    def test_registration_form(self, last_name, first_name, phone, 
                               email, password, confirmation, expected_data):
        home_page = HomePage(self.driver)
        register_form = RegistrationComponent(self.driver)

        home_page.header \
            .move_to_guest_menu() \
            .click_register_button() \
            .enter_last_name(last_name) \
            .enter_first_name(first_name) \
            .enter_phone(phone) \
            .enter_email(email) \
            .enter_password(password) \
            .confirm_password(confirmation) \
            .click_close_button()
        
        home_page.header \
            .move_to_guest_menu() \
            .click_register_button()
        
        actual_data = {
            "last_name": register_form.get_last_name_value(),
            "first_name": register_form.get_first_name_value(),
            "phone": register_form.get_phone_value(),
            "email": register_form.get_email_value(),
            "password": register_form.get_password_value(),
            "confirmation": register_form.get_confirm_password_field()
        }
        
        self.assertDictEqual(actual_data, expected_data)
