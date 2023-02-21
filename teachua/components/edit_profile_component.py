from selenium.webdriver.common.keys import Keys
from teachua.base.base_page import BasePage
from teachua.locators.component_locators import EditProfileComponentLocators


class EditProfileComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = EditProfileComponentLocators
    
    def get_edit_profile_title(self):
        return self.wait_element_to_appear(self.locator.EDIT_PROFILE_TITLE).text
    
    def enter_new_last_name(self, last_name):
        self.wait_element_to_be_clickable(self.locator.EDIT_LAST_NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.EDIT_LAST_NAME_FIELD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.EDIT_LAST_NAME_FIELD).send_keys(last_name)
        return self
    
    def enter_new_first_name(self, first_name):
        self.wait_element_to_be_clickable(self.locator.EDIT_FIRST_NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.EDIT_FIRST_NAME_FIELD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.EDIT_FIRST_NAME_FIELD).send_keys(first_name)
        return self
    
    def enter_new_phone(self, phone):
        self.wait_element_to_be_clickable(self.locator.EDIT_PHONE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.EDIT_PHONE_FIELD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.EDIT_PHONE_FIELD).send_keys(phone)
        return self
    
    def click_change_password(self):
        self.wait_element_to_be_clickable(self.locator.CHANGE_PASSWORD_SECTION).click()
        return self
    
    def enter_current_password(self, password):
        self.wait_element_to_be_clickable(self.locator.EDIT_CURRENT_PASSWORD).click()
        self.wait_element_to_be_clickable(self.locator.EDIT_CURRENT_PASSWORD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.EDIT_CURRENT_PASSWORD).send_keys(password)
        return self
    
    def enter_new_password(self, password):
        self.wait_element_to_be_clickable(self.locator.NEW_PASSWORD_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.NEW_PASSWORD_FIELD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.NEW_PASSWORD_FIELD).send_keys(password)
        return self
    
    def confirm_new_password(self, password):
        self.wait_element_to_be_clickable(self.locator.CONFIRM_NEW_PASSWORD).click()
        self.wait_element_to_be_clickable(self.locator.CONFIRM_NEW_PASSWORD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.CONFIRM_NEW_PASSWORD).send_keys(password)
        return self
    
    def get_error_messages(self):
        messages = self.wait_elements_to_appear(self.locator.ERROR_MESSAGES)
        return [msg.text for msg in messages]
    
    def click_save_changes_button(self):
        self.wait_element_to_be_clickable(self.locator.SAVE_CHANGES_BUTTON).click()
        return self
    
    def click_close_button(self):
        self.wait_element_to_be_clickable(self.locator.CLOSE_BUTTON).click()
        return self
