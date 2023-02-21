from teachua.base.base_page import BasePage
from teachua.locators.component_locators import HeaderComponentLocators
from teachua.components.menu_component import (
    UserMenuComponent, 
    AdminMenuComponent, 
    GuestMenuComponent
    )
from teachua.pages.clubs_page import ClubsPage
from teachua.pages.news_page import NewsPage
from utils.constants import Scripts, UserRoles


class HeaderComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HeaderComponentLocators
    
    def is_logged(self):
        return self.driver.execute_script(Scripts.LOCAL_STORAGE.value)
    
    def click_clubs_button(self):
        self.wait_element_to_be_clickable(self.locator.CLUBS_BUTTON).click()
        return ClubsPage(self.driver)

    def click_news_button(self):
        self.wait_element_to_be_clickable(self.locator.NEWS_BUTTON).click()
        return NewsPage(self.driver)
    
    def click_user_icon(self):
        self.wait_element_to_be_clickable(self.locator.USER_ICON).click()
        if self.is_logged() == UserRoles.USER.value:
            return UserMenuComponent(self.driver)
        elif self.is_logged() == UserRoles.ADMIN.value:
            return AdminMenuComponent(self.driver)
        return GuestMenuComponent(self.driver)
