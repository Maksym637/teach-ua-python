from teachua.base.base_page import BasePage
from teachua.locators.component_locators import AddLocationComponentLocators


class AddLocationComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = AddLocationComponentLocators
    
    def enter_location_name(self, name):
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).send_keys(name)
        return self
    
    def choose_city(self, number):
        self.wait_element_to_be_clickable(self.locator.CITY_FIELD).click()
        self.wait_elements_to_appear(self.locator.CITIES_LIST)[number].click()
        return self
    
    def choose_region(self, number):
        self.wait_element_to_be_clickable(self.locator.REGION_FIELD).click()
        self.wait_elements_to_appear(self.locator.REGIONS_LIST)[number].click()
        return self
    
    def enter_address(self, address):
        self.wait_element_to_be_clickable(self.locator.ADDRESS_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.ADDRESS_FIELD).send_keys(address)
        return self
    
    def enter_coordinates(self, coordinates):
        self.wait_element_to_be_clickable(self.locator.COORDINATES_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.COORDINATES_FIELD).send_keys(coordinates)
        return self
    
    def enter_phone(self, phone):
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).send_keys(phone)
        return self
    
    def click_add_button(self):
        self.wait_element_to_be_clickable(self.locator.ADD_BUTTON).click()
        return self
    
    def click_close_button(self):
        self.wait_element_to_be_clickable(self.locator.CLOSE_BUTTON).click()
        return self
    
    def get_error_messages(self):
        messages = self.wait_elements_to_appear(self.locator.ERROR_MESSAGES)
        return [msg.text for msg in messages]
