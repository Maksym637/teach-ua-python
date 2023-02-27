import configparser
from tests.base_test import BaseTest
from teachua.pages.home_page import HomePage
from utils.constants import Paths


config = configparser.ConfigParser()
config.read(Paths.CREDENTIALS_PATH.value)
config.sections()


class LoginRunner(BaseTest):

    def setUp(self):
        home_page = HomePage(self.driver)

        home_page.header \
            .move_to_guest_menu() \
            .click_login_button() \
            .enter_email(config["Admin"]["email"]) \
            .enter_password(config["Admin"]["password"]) \
            .click_sign_in() \
            .get_success_message()
    
    def tearDown(self):
        home_page = HomePage(self.driver)

        home_page.open()

        home_page.header \
            .move_to_user_menu() \
            .click_log_out()
