import configparser
from tests.base_test import BaseTest
from teachua.pages.home_page import HomePage
from utils.constants import Paths
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

config = configparser.ConfigParser()
config.read(Paths.CREDENTIALS_PATH.value)
config.sections()

USER = {
    "email": config["Admin"]["email"],
    "password": config["Admin"]["password"]
}

DB = {
    "username": config["Database"]["db_username"],
    "password": config["Database"]["db_password"],
    "hostname": config["Database"]["db_hostname"],
    "name": config["Database"]["db_name"]
}

engine = create_engine(f"postgresql://{DB['username']}:{DB['password']}@{DB['hostname']}/{DB['name']}")
Session = sessionmaker(bind=engine)


class LoginRunner(BaseTest):

    def setUp(self):
        self.home_page = HomePage(self.driver)

        self.home_page.header \
            .move_to_guest_menu() \
            .click_login_button() \
            .enter_email(USER["email"]) \
            .enter_password(USER["password"]) \
            .click_sign_in() \
            .get_success_message()
    
    def tearDown(self):
        self.home_page.open()

        self.home_page.header \
            .move_to_user_menu() \
            .click_log_out()


class LoginSessionRunner(BaseTest):

    def setUp(self):
        self.session = Session()
        self.home_page = HomePage(self.driver)

        self.home_page.header \
            .move_to_guest_menu() \
            .click_login_button() \
            .enter_email(USER["email"]) \
            .enter_password(USER["password"]) \
            .click_sign_in() \
            .get_success_message()
    
    def tearDown(self):
        self.home_page.open()

        self.home_page.header \
            .move_to_user_menu() \
            .click_log_out()
        
        self.session.close()
