from tests.precondition_test import LoginRunner
from teachua.pages.home_page import HomePage
from parameterized import parameterized
from utils.constants import Urls
import allure


error_messages = [
    "Опис гуртка задовгий",
    "Опис гуртка не може містити російські літери",
    "Некоректний опис гуртка\nОпис гуртка не може містити російські літери"
]


class TestClubComponent(LoginRunner):

    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-177", "TUA-177")
    @allure.severity(allure.severity_level.NORMAL)
    @parameterized.expand([
        ("club1.1", 0, "10", "15", "1212121212", ("some data;" * 150)),
        ("club1.2", 6, "9", "14", "1313131313", ("text;" * 300)),
        ("club1.3", 12, "15", "18", "2323232323", ("new test data ;" * 100)),
        ("club1.4", 3, "11", "18", "2525252525", ("some text;" * 5)),
        ("club1.5", 9, "8", "13", "1717171717", ("club description;" * 3))
    ])
    def test_description_field_valid(self, name, number, age_from, 
                                     age_to, phone, description):
        home_page = HomePage(self.driver)

        is_input_success = home_page.header \
            .move_to_user_menu() \
            .click_add_club() \
            .enter_club_name(name) \
            .choose_category(number) \
            .enter_age_from(age_from) \
            .enter_age_to(age_to) \
            .click_next_step() \
            .enter_phone(phone) \
            .click_next_step() \
            .enter_description(description) \
            .get_description_success()
        
        self.assertTrue(is_input_success)

    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-177", "TUA-177")
    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-178", "TUA-178")
    @allure.severity(allure.severity_level.NORMAL)
    @parameterized.expand([
        ("club2.1", 1, "12", "16", "1212121212", ("text;" * 300 + "!"), error_messages[0]),
        ("club2.2", 7, "10", "16", "1313131313", ("new test data ;" * 120), error_messages[0]),
        ("club2.3", 9, "15", "18", "2323232323", ("запрещенные слова;" * 3), error_messages[1]),
        ("club2.4", 2, "11", "18", "2525252525", ("эъüöäЫэъüöä" * 5), error_messages[2]),
        ("club2.5", 10, "8", "15", "1717171717", ("Aussätzige|Прокаженные" * 2), error_messages[2])
    ])
    def test_description_field_invalid(self, name, number, age_from,
                                       age_to, phone, description, expected_error_msg):
        home_page = HomePage(self.driver)

        actual_error_msg = home_page.header \
            .move_to_user_menu() \
            .click_add_club() \
            .enter_club_name(name) \
            .choose_category(number) \
            .enter_age_from(age_from) \
            .enter_age_to(age_to) \
            .click_next_step() \
            .enter_phone(phone) \
            .click_next_step() \
            .enter_description(description) \
            .get_description_error_msg()
        
        self.assertEqual(actual_error_msg, expected_error_msg)
