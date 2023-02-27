from teachua.base.base_page import BasePage
from teachua.locators.component_locators import NewsCardComponentLocators, ClubCardComponentLocators
from teachua.pages.view_item_page import ViewNewsPage, ViewClubPage


class NewsCardComponent(BasePage):

    def __init__(self, driver, root):
        super().__init__(driver)
        self.root = root
        self.locator = NewsCardComponentLocators
    
    def get_news_date(self):
        return self.root.find_element(*self.locator.NEWS_DATE).text
    
    def get_news_title(self):
        return self.root.find_element(*self.locator.NEWS_TITLE).text
    
    def click_details_button(self):
        self.root.find_element(*self.locator.DETAILS_BUTTON).click()
        return ViewNewsPage(self.driver)


class ClubCardComponent(BasePage):

    def __init__(self, driver, root):
        super().__init__(driver)
        self.root = root
        self.locator = ClubCardComponentLocators
    
    def get_club_title(self):
        return self.root.find_element(*self.locator.CLUB_TITLE)
    
    def click_details_button(self):
        self.root.find_element(*self.locator.DETAILS_BUTTON).click()
        return ViewClubPage(self.driver)
