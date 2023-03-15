from teachua.base.base_page import BasePage
from teachua.locators.component_locators import AddLocationComponentLocators
import allure


class AddLocationComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = AddLocationComponentLocators

    @allure.step("Enter location name : {name}")
    def enter_location_name(self, name):
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).send_keys(name)
        return self
    
    @allure.step("Choose city : city number in list is {number}")
    def choose_city(self, number):
        self.wait_element_to_be_clickable(self.locator.CITY_FIELD).click()
        self.wait_elements_to_appear(self.locator.CITIES_LIST)[number].click()
        return self
    
    @allure.step("Choose region : region number in list is {number}")
    def choose_region(self, number):
        self.wait_element_to_be_clickable(self.locator.REGION_FIELD).click()
        self.wait_elements_to_appear(self.locator.REGIONS_LIST)[number].click()
        return self
    
    @allure.step("Enter address : {address}")
    def enter_address(self, address):
        self.wait_element_to_be_clickable(self.locator.ADDRESS_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.ADDRESS_FIELD).send_keys(address)
        return self
    
    @allure.step("Enter coordinates : {coordinates}")
    def enter_coordinates(self, coordinates):
        self.wait_element_to_be_clickable(self.locator.COORDINATES_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.COORDINATES_FIELD).send_keys(coordinates)
        return self
    
    @allure.step("Enter phone number : {phone}")
    def enter_phone(self, phone):
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.PHONE_FIELD).send_keys(phone)
        return self
    
    @allure.step("Click on the add button")
    def click_add_button(self):
        self.wait_element_to_be_clickable(self.locator.ADD_BUTTON).click()
        return self
    
    @allure.step("Click on the close button")
    def click_close_button(self):
        self.wait_element_to_be_clickable(self.locator.CLOSE_BUTTON).click()
        return self
    
    def get_error_messages(self):
        messages = self.wait_elements_to_appear(self.locator.ERROR_MESSAGES)
        return [msg.text for msg in messages]
