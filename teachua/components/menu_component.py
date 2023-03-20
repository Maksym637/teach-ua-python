from teachua.base.base_page import BasePage
from teachua.locators.component_locators import (
    GuestMenuComponentLocators, 
    UserMenuComponentLocators,
    AdminMenuComponentLocators
)
from teachua.components.register_component import RegistrationComponent
from teachua.components.login_component import LoginComponent
from teachua.components.add_club_component import ClubMainInfoComponent
from teachua.components.add_centre_component import CentreMainInfoComponent
from teachua.pages.profile_page import ProfilePage
from teachua.pages.challenges_page import ChallengesPage
from teachua.pages.tasks_page import TasksPage
import allure


class GuestMenuComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = GuestMenuComponentLocators

    @allure.step("Click on the registration button")
    def click_register_button(self):
        self.wait_element_to_be_clickable(self.locator.REGISTER_BUTTON).click()
        return RegistrationComponent(self.driver)
    
    @allure.step("Click on the login button")
    def click_login_button(self):
        self.wait_element_to_be_clickable(self.locator.LOGIN_BUTTON).click()
        return LoginComponent(self.driver)


class UserMenuComponent(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = UserMenuComponentLocators

    @allure.step("Click on the add club button")
    def click_add_club(self):
        self.wait_element_to_be_clickable(self.locator.ADD_CLUB).click()
        return ClubMainInfoComponent(self.driver)
    
    @allure.step("Click on the add centre button")
    def click_add_centre(self):
        self.wait_element_to_be_clickable(self.locator.ADD_CENTRE).click()
        return CentreMainInfoComponent(self.driver)
    
    @allure.step("Click on the profile account button")
    def click_profile_account(self):
        self.wait_element_to_be_clickable(self.locator.PROFILE_ACCOUNT).click()
        return ProfilePage(self.driver)
    
    @allure.step("Click logout button")
    def click_log_out(self):
        self.wait_element_to_be_clickable(self.locator.LOG_OUT).click()
        return self


class AdminMenuComponent(UserMenuComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator_admin = AdminMenuComponentLocators

    @allure.step("Move to challenges page")
    def move_to_challenges(self):
        self.wait_element_to_be_clickable(self.locator_admin.CONTENT_MENU).click()
        self.wait_element_to_be_clickable(self.locator_admin.CHALLENGES_MENU).click()
        self.wait_element_to_be_clickable(self.locator_admin.CHALLENGES_BUTTON).click()
        return ChallengesPage(self.driver)
    
    def move_to_tasks(self):
        self.wait_element_to_be_clickable(self.locator_admin.CONTENT_MENU).click()
        self.wait_element_to_be_clickable(self.locator_admin.CHALLENGES_MENU).click()
        self.wait_element_to_be_clickable(self.locator_admin.TASKS_BUTTON).click()
        return TasksPage(self.driver)
