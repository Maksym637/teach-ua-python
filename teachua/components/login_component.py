from teachua.base.base_page import BasePage
from teachua.locators.component_locators import LoginComponentLocators


class LoginComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginComponentLocators
    
    def enter_email(self, email):
        self.wait_element_to_be_clickable(self.locator.EMAIL_INPUT).click()
        self.wait_element_to_be_clickable(self.locator.EMAIL_INPUT).clear()
        self.wait_element_to_be_clickable(self.locator.EMAIL_INPUT).send_keys(email)
        return self
    
    def enter_password(self, password):
        self.wait_element_to_be_clickable(self.locator.PASSWORD_INPUT).click()
        self.wait_element_to_be_clickable(self.locator.PASSWORD_INPUT).clear()
        self.wait_element_to_be_clickable(self.locator.PASSWORD_INPUT).send_keys(password)
        return self
    
    def click_sign_in(self):
        self.wait_element_to_be_clickable(self.locator.SIGN_IN_BUTTON).click()
        return self
    
    def get_success_message(self):
        return self.wait_element_to_appear(self.locator.SUCCESS_MESSAGE).text
    
    def get_error_message(self):
        return self.wait_element_to_appear(self.locator.ERROR_MESSAGE).text
