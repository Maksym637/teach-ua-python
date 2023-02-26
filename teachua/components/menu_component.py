from teachua.base.base_page import BasePage
from teachua.locators.component_locators import (
    GuestMenuComponentLocators, 
    UserMenuComponentLocators, 
    )
from teachua.components.register_component import RegistrationComponent
from teachua.components.login_component import LoginComponent
from teachua.components.add_club_component import ClubMainInfoComponent
from teachua.components.add_centre_component import CentreMainInfoComponent
from teachua.pages.profile_page import ProfilePage


class GuestMenuComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = GuestMenuComponentLocators
    
    def click_register_button(self):
        self.wait_element_to_be_clickable(self.locator.REGISTER_BUTTON).click()
        return RegistrationComponent(self.driver)
    
    def click_login_button(self):
        self.wait_element_to_be_clickable(self.locator.LOGIN_BUTTON).click()
        return LoginComponent(self.driver)


class UserMenuComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = UserMenuComponentLocators
    
    def click_add_club(self):
        self.wait_element_to_be_clickable(self.locator.ADD_CLUB).click()
        return ClubMainInfoComponent(self.driver)
    
    def click_add_centre(self):
        self.wait_element_to_be_clickable(self.locator.ADD_CENTRE).click()
        return CentreMainInfoComponent(self.driver)
    
    def click_profile_account(self):
        self.wait_element_to_be_clickable(self.locator.PROFILE_ACCOUNT).click()
        return ProfilePage(self.driver)
    
    def click_log_out(self):
        self.wait_element_to_be_clickable(self.locator.LOG_OUT).click()
        return self
