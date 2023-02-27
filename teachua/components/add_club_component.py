from teachua.base.base_page import BasePage
from teachua.locators.component_locators import (
    StepLocators,
    ClubMainInfoComponentLocators,
    ClubContactsComponentLocators,
    ClubDescriptionComponentLocators
)


class ClubStep(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.step_locator = StepLocators
    
    def get_previous_step(self):
        return self.wait_element_to_be_clickable(self.step_locator.PREVIOUS_STEP)
    
    def get_next_step(self):
        return self.wait_element_to_be_clickable(self.step_locator.NEXT_STEP)


class ClubMainInfoComponent(ClubStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ClubMainInfoComponentLocators
    
    def enter_club_name(self, name):
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).send_keys(name)
        return self
    
    def choose_category(self, number):
        self.wait_elements_to_appear(self.locator.CATEGORIES_BOXES)[number].click()
        return self
    
    def enter_age_from(self, age_from):
        self.wait_element_to_be_clickable(self.locator.AGE_FROM).click()
        self.wait_element_to_be_clickable(self.locator.AGE_FROM).send_keys(age_from)
        return self
    
    def enter_age_to(self, age_to):
        self.wait_element_to_be_clickable(self.locator.AGE_TO).click()
        self.wait_element_to_be_clickable(self.locator.AGE_TO).send_keys(age_to)
        return self
    
    def click_next_step(self):
        self.get_next_step().click()
        return ClubContactsComponent(self.driver)


class ClubContactsComponent(ClubStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ClubContactsComponentLocators
    
    def enter_phone(self, phone):
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).send_keys(phone)
        return self
    
    def click_previous_step(self):
        self.get_previous_step().click()
        return ClubMainInfoComponent(self.driver)
    
    def click_next_step(self):
        self.get_next_step().click()
        return ClubDescriptionComponent(self.driver)


class ClubDescriptionComponent(ClubStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ClubDescriptionComponentLocators

    def enter_description(self, description):
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).send_keys(description)
        return self
    
    def get_description_success(self):
        return self.wait_element_to_appear(self.locator.DESCRIPTION_SUCESS).is_displayed()

    def get_description_error_msg(self):
        return self.wait_element_to_appear(self.locator.DESCRIPTION_ERROR_MSG).text
    
    def click_previous_step(self):
        self.get_previous_step().click()
        return ClubContactsComponent(self.driver)
    
    def click_finish_button(self):
        self.wait_element_to_be_clickable(self.locator.FINISH_BUTTON).click
        return self
