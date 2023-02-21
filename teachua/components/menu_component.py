from teachua.base.base_page import BasePage
from teachua.locators.component_locators import GuestMenuComponentLocators
from teachua.components.login_component import LoginComponent


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
    pass


class AdminMenuComponent(BasePage):
    pass
