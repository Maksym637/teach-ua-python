from teachua.base.base_page import BasePage
from teachua.locators.page_locators import NewsPageLocators
from teachua.components.card_component import NewsCardComponent, ClubCardComponent
import allure


class NewsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = NewsPageLocators
    
    def get_news_title(self):
        return self.wait_element_to_appear(self.locator.NEWS_TITLE).text
    
    def get_clubs_title(self):
        return self.wait_element_to_appear(self.locator.CLUBS_TITLE).text
    
    def get_all_news(self):
        return len(self.wait_elements_to_appear(self.locator.NEWS_CARDS))
    
    def get_all_clubs(self):
        return len(self.wait_elements_to_appear(self.locator.CLUB_CARDS))
    
    @allure.step("Choose certain news : news number in list is {card_number}")
    def choose_news_card(self, card_number):
        card_root = self.wait_elements_to_appear(self.locator.NEWS_CARDS)[card_number]
        return NewsCardComponent(self.driver, card_root)
    
    @allure.step("Choose certain club : club number in list is {card_number}")
    def choose_club_card(self, card_number):
        card_root = self.wait_elements_to_appear(self.locator.CLUB_CARDS)[card_number]
        return ClubCardComponent(self.driver, card_root)
