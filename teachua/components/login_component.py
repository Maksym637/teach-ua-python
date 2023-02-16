from teachua.base.base import Base
from teachua.locators.component_locators import LoginComponentLocators


class LoginComponent(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginComponentLocators
    
    def get_email(self):
        return self.wait_element_to_be_clickable(self.locator.EMAIL_INPUT)
    
    def enter_email(self, email):
        self.get_email().click()
        self.get_email().clear()
        self.get_email().send_keys(email)
        return self
    
    def get_password(self):
        return self.wait_element_to_be_clickable(self.locator.PASSWORD_INPUT)
    
    def enter_password(self, password):
        self.get_password().click()
        self.get_password().clear()
        self.get_password().send_keys(password)
        return self
    
    def get_sign_in(self):
        return self.wait_element_to_be_clickable(self.locator.SIGN_IN_BUTTON)
    
    def click_sign_in(self):
        self.get_sign_in().click()
        return self
    
    def get_success_message(self):
        return self.wait_element_to_appear(self.locator.SUCCESS_MESSAGE).text
    
    def get_error_message(self):
        return self.wait_element_to_appear(self.locator.ERROR_MESSAGE).text
