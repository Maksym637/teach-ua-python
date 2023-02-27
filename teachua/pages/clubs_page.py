from teachua.base.base_page import BasePage
from teachua.locators.page_locators import ClubsPageLocators
from teachua.components.card_component import ClubCardComponent


class ClubsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ClubsPageLocators
    
    def get_clubs_title(self):
        return self.wait_element_to_appear(self.locator.CLUBS_TITLE).text
    
    def get_all_clubs(self):
        return len(self.wait_elements_to_appear(self.locator.CLUB_CARDS))
    
    def choose_club_card(self, card_number):
        card_root = self.wait_elements_to_appear(self.locator.CLUB_CARDS)[card_number]
        return ClubCardComponent(self.driver, card_root)
