from teachua.base.base_component import BaseComponent
from utils.component_locators import GuestMenuComponentLocators
from teachua.components.login_component import LoginComponent


class GuestMenuComponent(BaseComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = GuestMenuComponentLocators
    
    def get_register_button(self):
        return self.wait_element_to_be_clickable(self.locator.REGISTER_BUTTON)
    
    def click_register_button(self):
        self.get_register_button().click()
        return self
    
    def get_login_button(self):
        return self.wait_element_to_be_clickable(self.locator.LOGIN_BUTTON)
    
    def click_login_button(self):
        self.get_login_button().click()
        return LoginComponent(self.driver)


class UserMenuComponent(BaseComponent):
    pass
