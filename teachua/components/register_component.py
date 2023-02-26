from teachua.base.base_page import BasePage
from teachua.locators.component_locators import RegistrationComponentLocators


class RegistrationComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = RegistrationComponentLocators
    
    def enter_last_name(self, last_name):
        self.wait_element_to_be_clickable(self.locator.LAST_NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.LAST_NAME_FIELD).send_keys(last_name)
        return self
    
    def get_last_name_value(self):
        return self.wait_element_to_appear(self.locator.LAST_NAME_FIELD).get_attribute("value")
    
    def enter_first_name(self, first_name):
        self.wait_element_to_be_clickable(self.locator.FIRST_NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.FIRST_NAME_FIELD).send_keys(first_name)
        return self
    
    def get_first_name_value(self):
        return self.wait_element_to_appear(self.locator.FIRST_NAME_FIELD).get_attribute("value")
    
    def enter_phone(self, phone):
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).send_keys(phone)
        return self
    
    def get_phone_value(self):
        return self.wait_element_to_appear(self.locator.PHONE_FIELD).get_attribute("value")
    
    def enter_email(self, email):
        self.wait_element_to_be_clickable(self.locator.EMAIL_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.EMAIL_FIELD).send_keys(email)
        return self
    
    def get_email_value(self):
        return self.wait_element_to_appear(self.locator.EMAIL_FIELD).get_attribute("value")
    
    def enter_password(self, password):
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PASSWORD_FIELD).send_keys(password)
        return self
    
    def get_password_value(self):
        return self.wait_element_to_appear(self.locator.PASSWORD_FIELD).get_attribute("value")
    
    def confirm_password(self, password):
        self.wait_element_to_be_clickable(self.locator.CONFIRM_PASSWORD_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.CONFIRM_PASSWORD_FIELD).send_keys(password)
        return self
    
    def get_confirm_password_field(self):
        return self.wait_element_to_appear(self.locator.CONFIRM_PASSWORD_FIELD).get_attribute("value")
    
    def click_register_button(self):
        self.wait_element_to_be_clickable(self.locator.REGISTER_BUTTON).click()
        return self
    
    def click_close_button(self):
        self.wait_element_to_be_clickable(self.locator.CLOSE_BUTTON).click()
        return self
