from teachua.base.base_page import BasePage
from teachua.locators.page_locators import (
    TasksPageLocators,
    AddTaskPageLocators
)
from teachua.locators.component_locators import CalendarComponentLocators


class TasksPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = TasksPageLocators
    
    def click_add_task(self):
        self.wait_element_to_be_clickable(self.locator.ADD_TASK_BUTTON).click()
        return AddTaskPage(self.driver)


class AddTaskPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = AddTaskPageLocators
        self.calendar = Calendar(self.driver)

    def are_fields_empty(self):
        is_empty = True
        fields = self.wait_different_elements_to_appear([
            self.locator.NAME_FIELD, self.locator.TITLE_FIELD, self.locator.DESCRIPTION_FIELD
        ])
        for field in fields:
            if (field.get_attribute("value") != None and 
                field.get_attribute("value") != False and 
                field.get_attribute("value") != ""):
                is_empty = False
        return is_empty

    def select_start_date(self, day, month, year):
        self.wait_element_to_be_clickable(self.locator.START_DATE_FIELD).click()
        self.calendar.select_date(day, month, year)
        return self
    
    def upload_photo(self, photo_path):
        self.driver.find_element(*self.locator.PHOTO_FIELD).send_keys(photo_path)
        self.wait_element_to_appear(self.locator.PHOTO_APPEARED)
        return self
    
    def enter_task_name(self, name):
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.NAME_FIELD).send_keys(name)
        return self
    
    def enter_task_title(self, title):
        self.wait_element_to_be_clickable(self.locator.TITLE_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.TITLE_FIELD).send_keys(title)
        return self
    
    def enter_description(self, description):
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).click()
        self.wait_element_to_be_clickable(self.locator.DESCRIPTION_FIELD).send_keys(description)
        return self
    
    def choose_challenge(self, challenge_idx):
        self.wait_element_to_be_clickable(self.locator.CHALLENGE_FIELD).click()
        self.wait_elements_to_appear(self.locator.CHALLENGE_LIST)[challenge_idx].click()
        return self
    
    def click_save_button(self):
        self.wait_element_to_be_clickable(self.locator.SAVE_BUTTON).click()
        return self
    
    def get_alert_msg(self):
        return self.wait_element_to_appear(self.locator.ALERT_MESSAGE).text


class Calendar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = CalendarComponentLocators
        self.months = {
            "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
            "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
        }

    def select_date(self, day, month, year):
        self.select_year(year)
        self.select_month(month)
        self.select_day(day)

    def select_year(self, year):
        current_year = int(self.wait_element_to_appear(self.locator.YEAR_BUTTON).text)
        if year > current_year:
            while current_year != year:
                self.wait_element_to_be_clickable(self.locator.NEXT_YEAR_BUTTON).click()
                current_year = int(self.wait_element_to_appear(self.locator.YEAR_BUTTON).text)
        else:
            while current_year != year:
                self.wait_element_to_be_clickable(self.locator.PREVIOUS_YEAR_BUTTON).click()
                current_year = int(self.wait_element_to_appear(self.locator.YEAR_BUTTON).text)

    def select_month(self, month):
        current_month = self.wait_element_to_appear(self.locator.MONTH_BUTTON).text
        if month > self.months[current_month]:
            while self.months[current_month] != month:
                self.wait_element_to_be_clickable(self.locator.NEXT_MONTH_BUTTON).click()
                current_month = self.wait_element_to_appear(self.locator.MONTH_BUTTON).text
        else:
            while self.months[current_month] != month:
                self.wait_element_to_be_clickable(self.locator.PREVIOUS_MONTH_BUTTON).click()
                current_month = self.wait_element_to_appear(self.locator.MONTH_BUTTON).text
    
    def select_day(self, day):
        days = self.wait_elements_to_appear(self.locator.DAY_BUTTON)
        days[day - 1].click()
