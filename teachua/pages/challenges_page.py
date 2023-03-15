from teachua.base.base_page import BasePage
from teachua.locators.page_locators import (
    ChallengesPageLocators, 
    AddChallengePageLocators
)


class ChallengesPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = ChallengesPageLocators
    
    def search_challenge(self, challenge):
        self.wait_element_to_be_clickable(self.locator.SEARCH_CHALLENGES).click()
        self.wait_element_to_be_clickable(self.locator.SEARCH_CHALLENGES).send_keys(challenge)
        return self
    
    def click_search(self):
        self.wait_element_to_be_clickable(self.locator.SEARCH_BUTTON).click()
        return self
    
    def click_delete_challenge(self):
        self.wait_element_to_be_clickable(self.locator.DELETE_CHALLENGE).click()
        return self
    
    def confirm_delete_challenge(self):
        self.wait_element_to_be_clickable(self.locator.CONFIRM_DELETE_CHALLENGE).click()
        return self
    
    def click_add_challenge(self):
        self.wait_element_to_be_clickable(self.locator.ADD_CHALLENGE_BUTTON).click()
        return AddChallengePage(self.driver)


class AddChallengePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = AddChallengePageLocators
    
    def go_to_challenges(self):
        self.wait_element_to_be_clickable(self.locator.CHALLENGES_LIST).click()
        return ChallengesPage(self.driver)
    
    def enter_sort_number(self, sort_number):
        self.wait_element_to_be_clickable(self.locator.SORT_NUMBER_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.SORT_NUMBER_FIELD).send_keys(sort_number)
        return self
    
    def enter_challenge_name(self, name):
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).send_keys(name)
        return self
    
    def enter_challenge_title(self, title):
        self.wait_element_to_be_clickable(self.locator.TITLE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.TITLE_FIELD).send_keys(title)
        return self
    
    def enter_description(self, description):
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).send_keys(description)
        return self
    
    def upload_photo(self, photo_path):
        self.driver.find_element(*self.locator.PHOTO_FIELD).send_keys(photo_path)
        self.wait_element_to_appear(self.locator.PHOTO_APPEARED)
        return self
    
    def click_save_button(self):
        self.wait_element_to_be_clickable(self.locator.SAVE_BUTTON).click()
        return self
    
    def check_success_message(self):
        return self.wait_element_to_appear(self.locator.SUCCESS_MESSAGE).text
