from teachua.base.base_page import BasePage
from teachua.locators.component_locators import (
    GuestMenuComponentLocators, 
    UserMenuComponentLocators, 
    AdminMenuComponentLocators
    )
from teachua.components.login_component import LoginComponent
from teachua.components.club_component import ClubComponent
from teachua.components.centre_component import CentreComponent
from teachua.pages.profile_page import ProfilePage


class GuestMenuComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = GuestMenuComponentLocators
    
    def click_register_button(self):
        self.wait_element_to_be_clickable(self.locator.REGISTER_BUTTON).click()
        return self
    
    def click_login_button(self):
        self.wait_element_to_be_clickable(self.locator.LOGIN_BUTTON).click()
        return LoginComponent(self.driver)


class UserMenuComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = UserMenuComponentLocators
    
    def click_add_club(self):
        self.wait_element_to_be_clickable(self.locator.ADD_CLUB).click()
        return ClubComponent(self.driver)
    
    def click_add_centre(self):
        self.wait_element_to_be_clickable(self.locator.ADD_CENTRE).click()
        return CentreComponent(self.driver)
    
    def click_profile_account(self):
        self.wait_element_to_be_clickable(self.locator.PROFILE_ACCOUNT).click()
        return ProfilePage(self.driver)


class AdminMenuComponent(UserMenuComponent):
    pass
