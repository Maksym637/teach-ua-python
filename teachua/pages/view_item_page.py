from teachua.base.base_page import BasePage
from teachua.locators.page_locators import ViewNewsPageLocators, ViewClubPageLocators


class ViewNewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ViewNewsPageLocators
    
    def get_news_content(self):
        fields = self.wait_different_elements_to_appear([
            self.locator.NEWS_TITLE, self.locator.NEWS_DATE, self.locator.NEWS_DESCRIPTION
        ])
        return [field.text for field in fields]
    
    def is_donate_button_enabled(self):
        return self.wait_element_to_appear(self.locator.DONATE_BUTTON).is_enabled()


class ViewClubPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ViewClubPageLocators
    
    def get_club_content(self):
        fields = self.wait_different_elements_to_appear([
            self.locator.CLUB_TITLE, self.locator.CLUB_DESCRIPTION
        ])
        return [field.text for field in fields]
    
    def is_subscribe_button_enabled(self):
        return self.wait_element_to_appear(self.locator.SUBSCRIBE_BUTTON).is_enabled()
