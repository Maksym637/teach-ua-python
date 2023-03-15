from teachua.base.base_page import BasePage
from teachua.locators.component_locators import (
    StepLocators,
    CentreMainInfoComponentLocators, 
    CentreContactsComponentLocators,
    CentreDescriptionComponentLocators,
    CentreClubsComponentLocators
)
from teachua.components.location_component import AddLocationComponent
import allure


class CentreStep(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.step_locator = StepLocators
    
    def get_previous_step(self):
        return self.wait_element_to_be_clickable(self.step_locator.PREVIOUS_STEP)
    
    def get_next_step(self):
        return self.wait_element_to_be_clickable(self.step_locator.NEXT_STEP)


class CentreMainInfoComponent(CentreStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CentreMainInfoComponentLocators

    @allure.step("Enter centre name : {name}")
    def enter_centre_name(self, name):
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).send_keys(name)
        return self
    
    def get_alert_centre_name(self):
        return self.wait_element_to_appear(self.locator.ALERT_MSG_NAME_FIELD).text
    
    @allure.step("Click add location")
    def click_add_location(self):
        self.wait_element_to_be_clickable(self.locator.ADD_LOCATION_BUTTON).click()
        return AddLocationComponent(self.driver)
    
    @allure.step("Choose location : location number in list is {number}")
    def choose_location(self, number):
        self.wait_elements_to_appear(self.locator.LOCATIONS_CHOICE)[number].click()
        return self
    
    def get_name_new_location(self):
        self.scroll_until_element_in_view(
            self.wait_element_to_appear(self.locator.LOCATIONS_LIST)
        )
        return self.wait_elements_to_appear(self.locator.LOCATIONS_CHOICE)[-1].text  
    
    def get_location_title(self, number):
        return self.wait_elements_to_appear(self.locator.LOCATIONS_CHOICE)[number].text
    
    @allure.step("Click on the next step")
    def click_next_step(self):
        self.get_next_step().click()
        return CentreContactsComponent(self.driver)
    
    @allure.step("Click on the next step")
    def click_next_step_error(self):
        self.get_next_step().click()
        return self


class CentreContactsComponent(CentreStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CentreContactsComponentLocators

    @allure.step("Enter phone number : {phone}")
    def enter_phone(self, phone):
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).send_keys(phone)
        return self
    
    @allure.step("Click on the previous step")
    def click_previous_step(self):
        self.get_previous_step().click()
        return CentreMainInfoComponent(self.driver)

    @allure.step("Click on the next step") 
    def click_next_step(self):
        self.get_next_step().click()
        return CentreDescriptionComponent(self.driver)


class CentreDescriptionComponent(CentreStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CentreDescriptionComponentLocators

    @allure.step("Enter description : {description}")
    def enter_description(self, description):
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).send_keys(description)
        return self
    
    @allure.step("Click on the previous step")
    def click_previous_step(self):
        self.get_previous_step().click()
        return CentreContactsComponent(self.driver)
    
    @allure.step("Click on the next step") 
    def click_next_step(self):
        self.get_next_step().click()
        return CentreClubsComponent(self.driver)


class CentreClubsComponent(CentreStep):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CentreClubsComponentLocators

    @allure.step("Choose club : club number in list is {number}")
    def choose_club(self, number):
        self.wait_elements_to_appear(self.locator.CLUBS_CHOICE)[number].click()
        return self
    
    @allure.step("Click on the previous step")
    def click_previous_step(self):
        self.get_previous_step().click()
        return CentreDescriptionComponent(self.driver)
    
    @allure.step("Click on the finish button")
    def click_finish_button(self):
        self.wait_element_to_be_clickable(self.locator.FINISH_BUTTON).click()
        return self
