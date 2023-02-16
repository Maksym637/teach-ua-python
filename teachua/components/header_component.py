from teachua.base.base_page import BaseComponent
from utils.component_locators import HeaderComponentLocators
from teachua.components.menu_component import GuestMenuComponent, UserMenuComponent


class HeaderComponent(BaseComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HeaderComponentLocators
    
    def is_logged(self):
        return self.driver.execute_script("localStorage.getItem('role')") != None

    def get_user_icon(self):
        if self.is_logged():
            return self.wait_element_to_be_clickable(self.locator.USER_ICON_LOGIN)
        return self.wait_element_to_be_clickable(self.locator.USER_ICON_NOT_LOGIN)
    
    def click_user_icon(self):
        if self.is_logged():
            self.get_user_icon().click()
            return UserMenuComponent(self.driver)
        self.get_user_icon().click()
        return GuestMenuComponent(self.driver)
