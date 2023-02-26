from teachua.base.base_page import BasePage
from teachua.locators.component_locators import (
    CentreStepLocators, 
    CentreMainInfoComponentLocators, 
    CentreContactsComponentLocators,
    CentreDescriptionComponentLocators,
    CentreClubsComponentLocators
    )
from teachua.components.location_component import AddLocationComponent


class CentreStep(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.step_locator = CentreStepLocators
    
    def get_previous_step(self):
        return self.wait_element_to_be_clickable(self.step_locator.PREVIOUS_STEP)
    
    def get_next_step(self):
        return self.wait_element_to_be_clickable(self.step_locator.NEXT_STEP)


class CentreMainInfoComponent(CentreStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CentreMainInfoComponentLocators

    def enter_centre_name(self, name):
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).send_keys(name)
        return self
    
    def click_add_location(self):
        self.wait_element_to_be_clickable(self.locator.ADD_LOCATION_BUTTON).click()
        return AddLocationComponent(self.driver)
    
    def choose_location(self, number):
        self.wait_elements_to_appear(self.locator.LOCATIONS_CHOICE)[number].click()
        return self
    
    def get_location_title(self, number):
        return self.wait_elements_to_appear(self.locator.LOCATIONS_CHOICE)[number].text
    
    def click_next_step(self):
        self.wait_element_to_be_clickable(self.get_next_step()).click()
        return CentreContactsComponent(self.driver)


class CentreContactsComponent(CentreStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CentreContactsComponentLocators
    
    def enter_phone(self, phone):
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).send_keys(phone)
        return self
    
    def click_previous_step(self):
        self.get_previous_step().click()
        return CentreMainInfoComponent(self.driver)
    
    def click_next_step(self):
        self.get_next_step().click()
        return CentreDescriptionComponent(self.driver)


class CentreDescriptionComponent(CentreStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CentreDescriptionComponentLocators

    def enter_description(self, description):
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).send_keys(description)
        return self
    
    def click_previous_step(self):
        self.get_previous_step().click()
        return CentreContactsComponent(self.driver)
    
    def click_next_step(self):
        self.get_next_step().click()
        return CentreClubsComponent(self.driver)


class CentreClubsComponent(CentreStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CentreClubsComponentLocators
    
    def choose_club(self, number):
        self.wait_elements_to_appear(self.locator.CLUBS_CHOICE)[number].click()
        return self
    
    def click_previous_step(self):
        self.get_previous_step().click()
        return CentreDescriptionComponent(self.driver)
    
    def click_finish_button(self):
        self.wait_element_to_be_clickable(self.locator.FINISH_BUTTON).click()
        return self
