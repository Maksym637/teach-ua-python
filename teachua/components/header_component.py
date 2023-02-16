from teachua.base.base_page import BaseComponent
from utils.component_locators import HeaderComponentLocators


class HeaderComponent(BaseComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HeaderComponentLocators
    
    def get_user_icon(self):
        return self.driver.find_element(*self.locator.USER_ICON)
    
    def click_user_icon(self):
        self.get_user_icon().click()
        return self
