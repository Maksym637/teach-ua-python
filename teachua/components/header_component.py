from teachua.base.base_page import BasePage
from teachua.locators.component_locators import HeaderComponentLocators
from teachua.components.menu_component import (
    GuestMenuComponent, 
    UserMenuComponent,
    AdminMenuComponent
)
from teachua.pages.clubs_page import ClubsPage
from teachua.pages.news_page import NewsPage
import allure


class HeaderComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HeaderComponentLocators

    @allure.step("Click on the clubs button")
    def click_clubs_button(self):
        self.wait_element_to_be_clickable(self.locator.CLUBS_BUTTON).click()
        return ClubsPage(self.driver)
    
    @allure.step("Click on the news button")
    def click_news_button(self):
        self.wait_element_to_be_clickable(self.locator.NEWS_BUTTON).click()
        return NewsPage(self.driver)
    
    @allure.step("Click location button")
    def click_location_button(self):
        self.wait_element_to_be_clickable(self.locator.LOCATION_BUTTON).click()
        return self
    
    def get_all_locations(self):
        return self.wait_elements_to_appear(self.locator.LOCATIONS_LIST)
    
    def parse_location_list(self):
        return [location.text for location in self.get_all_locations()]
    
    @allure.step("Choose location : {location_name}")
    def choose_location(self, location_name):
        self.get_all_locations()[self.parse_location_list().index(location_name)].click()
        return self
    
    @allure.step("Move to guest menu")
    def move_to_guest_menu(self):
        self.wait_element_to_be_clickable(self.locator.USER_ICON_NOT_LOGIN).click()
        return GuestMenuComponent(self.driver)
    
    @allure.step("Move to user menu")
    def move_to_user_menu(self):
        self.wait_element_to_be_clickable(self.locator.USER_ICON_LOGIN).click()
        return UserMenuComponent(self.driver)

    @allure.step("Move to admin menu")  
    def move_to_admin_menu(self):
        self.wait_element_to_be_clickable(self.locator.USER_ICON_LOGIN).click()
        return AdminMenuComponent(self.driver)
