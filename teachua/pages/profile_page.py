from teachua.base.base_page import BasePage
from teachua.locators.page_locators import ProfilePageLocators
from teachua.components.edit_profile_component import EditProfileComponent
from teachua.components.club_component import ClubComponent
from teachua.components.centre_component import CentreComponent


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ProfilePageLocators
    
    def get_menu_title(self):
        return self.wait_element_to_appear(self.locator.MENU_TITLE).text
    
    def get_profile_title(self):
        return self.wait_element_to_appear(self.locator.PROFILE_TITLE).text
    
    def get_user_name(self):
        return self.wait_element_to_appear(self.locator.USER_NAME_FIELD).text
    
    def get_user_role(self):
        return self.wait_element_to_appear(self.locator.USER_ROLE_FIELD).text
    
    def get_user_phone(self):
        return self.wait_element_to_appear(self.locator.USER_PHONE_FIELD).text
    
    def get_user_email(self):
        return self.wait_element_to_appear(self.locator.USER_EMAIL_FIELD).text
    
    def click_edit_profile_button(self):
        self.wait_element_to_be_clickable(self.locator.EDIT_PROFILE_BUTTON).click()
        return EditProfileComponent(self.driver)
    
    def click_add_button(self):
        self.wait_element_to_be_clickable(self.locator.ADD_BUTTON).click()
        return self
    
    def click_add_club_button(self):
        self.wait_element_to_be_clickable(self.locator.ADD_CLUB_BUTTON).click()
        return ClubComponent(self.driver)
    
    def click_add_centre_button(self):
        self.wait_element_to_be_clickable(self.locator.ADD_CENTRE_BUTTON).click()
        return CentreComponent(self.driver)
