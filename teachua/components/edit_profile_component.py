from selenium.webdriver.common.keys import Keys
from teachua.base.base_page import BasePage
from teachua.locators.component_locators import EditProfileComponentLocators
from utils.functions import wait
import allure


class EditProfileComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = EditProfileComponentLocators
    
    def get_edit_profile_title(self):
        return self.wait_element_to_appear(self.locator.EDIT_PROFILE_TITLE).text
    
    @allure.step("Enter new last name : {last_name}")
    def enter_new_last_name(self, last_name):
        self.wait_element_to_be_clickable(self.locator.EDIT_LAST_NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.EDIT_LAST_NAME_FIELD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.EDIT_LAST_NAME_FIELD).send_keys(last_name)
        return self
    
    @wait(before=0.5)
    def get_alert_last_name(self):
        return self.wait_element_to_appear(self.locator.ALERT_MSG_LAST_NAME).text
    
    @allure.step("Enter new first name : {first_name}")
    def enter_new_first_name(self, first_name):
        self.wait_element_to_be_clickable(self.locator.EDIT_FIRST_NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.EDIT_FIRST_NAME_FIELD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.EDIT_FIRST_NAME_FIELD).send_keys(first_name)
        return self
    
    @wait(before=0.5)
    def get_alert_first_name(self):
        return self.wait_element_to_appear(self.locator.ALERT_MSG_FIRST_NAME).text
    
    @allure.step("Enter new phone number : {phone}")
    def enter_new_phone(self, phone):
        self.wait_element_to_be_clickable(self.locator.EDIT_PHONE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.EDIT_PHONE_FIELD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.EDIT_PHONE_FIELD).send_keys(phone)
        return self
    
    @wait(before=0.5)
    def get_alert_phone(self):
        return self.wait_element_to_appear(self.locator.ALERT_MSG_PHONE).text
    
    @allure.step("Click change password")
    def click_change_password(self):
        self.wait_element_to_be_clickable(self.locator.CHANGE_PASSWORD_SECTION).click()
        return self
    
    @allure.step("Enter current password : {password}")
    def enter_current_password(self, password):
        self.wait_element_to_be_clickable(self.locator.EDIT_CURRENT_PASSWORD).click()
        self.wait_element_to_be_clickable(self.locator.EDIT_CURRENT_PASSWORD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.EDIT_CURRENT_PASSWORD).send_keys(password)
        return self
    
    @wait(before=0.5)
    def get_alert_current_password(self):
        return self.wait_element_to_appear(self.locator.ALERT_MSG_CURRENT_PASSWORD).text
    
    @allure.step("Enter new password : {password}")
    def enter_new_password(self, password):
        self.wait_element_to_be_clickable(self.locator.NEW_PASSWORD_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.NEW_PASSWORD_FIELD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.NEW_PASSWORD_FIELD).send_keys(password)
        return self
    
    @wait(before=0.5)
    def get_alert_new_password(self):
        return self.wait_element_to_appear(self.locator.ALERT_MSG_NEW_PASSWORD).text
    
    @allure.step("Confirm new password : {password}")
    def confirm_new_password(self, password):
        self.wait_element_to_be_clickable(self.locator.CONFIRM_NEW_PASSWORD).click()
        self.wait_element_to_be_clickable(self.locator.CONFIRM_NEW_PASSWORD).send_keys(
            Keys.CONTROL, "a", Keys.DELETE
        )
        self.wait_element_to_be_clickable(self.locator.CONFIRM_NEW_PASSWORD).send_keys(password)
        return self
    
    @wait(before=0.5)
    def get_alert_confirm_password(self):
        return self.wait_element_to_appear(self.locator.ALERT_MSG_CONFIRM_PASSWORD).text
    
    @allure.step("Click save changes")
    def click_save_changes_button(self):
        self.wait_element_to_be_clickable(self.locator.SAVE_CHANGES_BUTTON).click()
        return self
    
    def is_save_changes_enabled(self):
        return self.wait_element_to_appear(self.locator.SAVE_CHANGES_BUTTON).is_enabled()
    
    @allure.step("Click close button")
    def click_close_button(self):
        self.wait_element_to_be_clickable(self.locator.CLOSE_BUTTON).click()
        return self
