from tests.precondition_test import LoginRunner
from teachua.pages.home_page import HomePage
from teachua.components.edit_profile_component import EditProfileComponent
from parameterized import parameterized
from utils.constants import Urls
import allure

combined_error_msg = [
    " не може містити більше, ніж 25 символів",
    " не може містити спеціальні символи",
    " не може містити цифри",
    " повинно починатися і закінчуватися літерою",
    "Будь ласка введіть Ваше "
]


class TestProfilePage(LoginRunner):

    @parameterized.expand([
        (("firstName" * 5), "Ім'я" + combined_error_msg[0]),
        ("!@#$%^&,", "Ім'я" + combined_error_msg[1]),
        ("1234", "Ім'я" + combined_error_msg[2]),
        ("-firstName", "Ім'я" + combined_error_msg[3]),
        ("< firstName>", "Ім'я" + combined_error_msg[1]),
        ("'firstName", "Ім'я" + combined_error_msg[3]),
        ("firstName-", "Ім'я" + combined_error_msg[3]),
        ("<firstName >", "Ім'я" + combined_error_msg[1]),
        ("firstName'", "Ім'я" + combined_error_msg[3]),
        ("", combined_error_msg[4] + "ім'я")
    ])
    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-328", "TUA-328")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_first_name_invalid(self, first_name, expected_alert_msg):
        home_page = HomePage(self.driver)
        edit_profile = EditProfileComponent(self.driver)

        actual_alert_msg = home_page.header \
            .move_to_user_menu() \
            .click_profile_account() \
            .click_edit_profile_button() \
            .enter_new_first_name(first_name) \
            .get_alert_first_name()
        
        self.assertEqual(actual_alert_msg, expected_alert_msg)
        self.assertFalse(edit_profile.is_save_changes_enabled())

    @parameterized.expand([
        (("lastName" * 5), "Прізвище" + combined_error_msg[0]),
        ("!@#$%^&,", "Прізвище" + combined_error_msg[1]),
        ("1234", "Прізвище" + combined_error_msg[2]),
        ("-lastName", "Прізвище" + combined_error_msg[3]),
        ("< lasttName>", "Прізвище" + combined_error_msg[1]),
        ("'lastName", "Прізвище" + combined_error_msg[3]),
        ("lastName-", "Прізвище" + combined_error_msg[3]),
        ("<lastName >", "Прізвище" + combined_error_msg[1]),
        ("lastName'", "Прізвище" + combined_error_msg[3]),
        ("", combined_error_msg[4] + "прізвище")
    ])
    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-343", "TUA-343")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_last_name_invalid(self, last_name, expected_alert_msg):
        home_page = HomePage(self.driver)
        edit_profile = EditProfileComponent(self.driver)

        actual_alert_msg = home_page.header \
            .move_to_user_menu() \
            .click_profile_account() \
            .click_edit_profile_button() \
            .enter_new_last_name(last_name) \
            .get_alert_last_name()
        
        self.assertEqual(actual_alert_msg, expected_alert_msg)
        self.assertFalse(edit_profile.is_save_changes_enabled())

    @parameterized.expand([
        ("065987458", "Телефон не відповідає вказаному формату"),
        ("06598521475", "Телефон не відповідає вказаному формату"),
        ("jngeoлщшогнеп", "Телефон не може містити літери\n" + 
         "Телефон не відповідає вказаному формату"),
        ("!@#$%^&*(_+.:", "Телефон не відповідає вказаному формату\n" +
         "Телефон не може містити спеціальні символи"),
        ("", "Будь ласка введіть Ваш номер телефону")
    ])
    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-356", "TUA-356")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_edit_phone_invalid(self, phone, expected_alert_msg):
        home_page = HomePage(self.driver)
        edit_profile = EditProfileComponent(self.driver)

        actual_alert_msg = home_page.header \
            .move_to_user_menu() \
            .click_profile_account() \
            .click_edit_profile_button() \
            .enter_new_phone(phone) \
            .get_alert_phone()
        
        self.assertEqual(actual_alert_msg, expected_alert_msg)
        self.assertFalse(edit_profile.is_save_changes_enabled())
