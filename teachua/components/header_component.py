from teachua.base.base_page import BasePage
from teachua.locators.component_locators import HeaderComponentLocators
from teachua.components.menu_component import (
    UserMenuComponent, 
    AdminMenuComponent, 
    GuestMenuComponent
    )
from teachua.pages.clubs_page import ClubsPage
from teachua.pages.news_page import NewsPage


class HeaderComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HeaderComponentLocators
    
    def click_clubs_button(self):
        self.wait_element_to_be_clickable(self.locator.CLUBS_BUTTON).click()
        return ClubsPage(self.driver)

    def click_news_button(self):
        self.wait_element_to_be_clickable(self.locator.NEWS_BUTTON).click()
        return NewsPage(self.driver)
    
    def move_to_guest_menu(self):
        self.wait_element_to_be_clickable(self.locator.USER_ICON_NOT_LOGIN).click()
        return GuestMenuComponent(self.driver)
    
    def move_to_user_menu(self):
        self.wait_element_to_be_clickable(self.locator.USER_ICON_LOGIN).click()
        return UserMenuComponent(self.driver)
    
    def move_to_admin_menu(self):
        self.wait_element_to_be_clickable(self.locator.USER_ICON_LOGIN).click()
        return AdminMenuComponent(self.driver)
