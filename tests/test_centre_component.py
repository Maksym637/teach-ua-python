from tests.precondition_test import LoginRunner
from teachua.pages.home_page import HomePage
from teachua.components.add_centre_component import CentreMainInfoComponent
from parameterized import parameterized
from utils.constants import Urls
import allure


class TestCentreComponent(LoginRunner):

    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-252", "TUA-252")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_centre_step(self):
        home_page = HomePage(self.driver)

        actual_alert_msg = home_page.header \
            .move_to_user_menu() \
            .click_add_centre() \
            .click_next_step_error() \
            .get_alert_centre_name()
        
        self.assertEqual(actual_alert_msg, "Некоректна назва центру")

    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-158", "TUA-158")
    @allure.severity(allure.severity_level.CRITICAL)
    @parameterized.expand([
        ("location-1.1", 0, 0, "street 1.1", "50.4485253, 30.4735083", "1212121212", "location-1.1"),
        ("location-2.2", 2, 2, "street 2.2", "30.4485253, 50.4735083", "2424242424", "location-2.2"),
        ("test-location", 4, 4, "test 12, 12", "25.4485253, 25.4735083", "0681245611", "test-location")
    ])
    def test_add_location_valid(self, location_name, city_number, region_number, 
                          address, coordinates, phone, expected_new_location):
        home_page = HomePage(self.driver)
        centre_main_info = CentreMainInfoComponent(self.driver)

        home_page.header \
            .move_to_user_menu() \
            .click_add_centre() \
            .click_add_location() \
            .enter_location_name(location_name) \
            .choose_city(city_number) \
            .choose_region(region_number) \
            .enter_address(address) \
            .enter_coordinates(coordinates) \
            .enter_phone(phone) \
            .click_add_button()
        
        actual_new_location = centre_main_info.get_name_new_location()

        self.assertEqual(actual_new_location, expected_new_location)

    @allure.issue(f"{Urls.TEST_CASES.value}/TUA-160", "TUA-160")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_location_invalid(self):
        home_page = HomePage(self.driver)

        actual_error_msg = home_page.header \
            .move_to_user_menu() \
            .click_add_centre() \
            .click_add_location() \
            .click_add_button() \
            .get_error_messages()
        
        self.assertListEqual(
            actual_error_msg, ["Некоректна назва локації", "Це поле є обов'язковим",
                               "Це поле є обов'язковим", "Некоректна адреса",
                               "Некоректні координати", "Це поле є обов'язковим"]
        )
