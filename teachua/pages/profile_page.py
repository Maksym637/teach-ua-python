from teachua.base.base_page import BasePage
from teachua.locators.page_locators import ProfilePageLocators
from teachua.components.edit_profile_component import EditProfileComponent
from teachua.components.club_component import ClubComponent
from teachua.components.centre_component import CentreComponent


class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ProfilePageLocators
    
    def get_profile_content(self):
        fields = self.wait_different_elements_to_appear([
            self.locator.MENU_TITLE, self.locator.PROFILE_TITLE, self.locator.USER_NAME_FIELD, 
            self.locator.USER_ROLE_FIELD, self.locator.USER_PHONE_FIELD, self.locator.USER_EMAIL_FIELD
        ])
        return [field.text for field in fields]
    
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
