from selenium.webdriver.common.by import By


class HeaderComponentLocators:
    CLUBS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'clubs')]")
    NEWS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'news')]")
    LOCATION_BUTTON = (By.XPATH, "//div[@class='ant-dropdown-trigger city']")
    LOCATIONS_LIST = (
        By.XPATH, "(//div[contains(@Class, 'ant-dropdown-show-arrow') and not(contains(@Class, 'ant-dropdown-hidden'))])//ul//li"
    )
    USER_ICON_NOT_LOGIN = (By.XPATH, "//span[contains(@class, 'avatarIfNotLogin')]")
    USER_ICON_LOGIN = (By.XPATH, "//span[contains(@class, 'avatarIfLogin')]")


class GuestMenuComponentLocators:
    REGISTER_BUTTON = (By.XPATH, "//li[contains(@data-menu-id, 'register')]")
    LOGIN_BUTTON = (By.XPATH, "//li[contains(@data-menu-id, 'login')]")


class UserMenuComponentLocators:
    ADD_CLUB = (By.XPATH, "//li[contains(@data-menu-id, 'add_club')]")
    ADD_CENTRE = (By.XPATH, "//li[contains(@data-menu-id, 'add_centre')]")
    PROFILE_ACCOUNT = (By.XPATH, "//li[contains(@data-menu-id, 'profile')]")
    LOG_OUT = (By.XPATH, "//li[contains(@data-menu-id, 'logout')]")


class AdminMenuComponentLocators:
    CONTENT_MENU = (By.XPATH, "//div[contains(@aria-controls, 'content-popup')]")
    CHALLENGES_MENU = (By.XPATH, "//div[contains(@aria-controls, 'challenges-submenu-popup')]")
    TASKS_BUTTON = (By.XPATH, "//ul[contains(@id, 'challenges-submenu-popup')]//a[contains(@href, 'tasks')]")
    CHALLENGES_BUTTON = (By.XPATH, "//ul[contains(@id, 'challenges-submenu-popup')]//a[contains(@href, 'challenges')]")


class RegistrationComponentLocators:
    LAST_NAME_FIELD = (By.XPATH, "//input[@id='lastName']")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@id='firstName']")
    PHONE_FIELD = (By.XPATH, "//input[@id='phone']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@id='confirm']")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(@class, 'registration-button')]")
    CLOSE_BUTTON = (
        By.XPATH, "//div[contains(@class, 'modal-registration')]//span[contains(@class, 'close-x')]"
    )


class LoginComponentLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@id='basic_email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='basic_password']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(@class, 'login-button')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'ant-message-success')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'ant-message-error')]")


class EditProfileComponentLocators:
    EDIT_PROFILE_TITLE = (By.XPATH, "//div[@class='edit-header']")
    EDIT_LAST_NAME_FIELD = (By.XPATH, "//input[@id='edit_lastName']")
    ALERT_MSG_LAST_NAME = (By.XPATH, "//div[@id='edit_lastName_help' and @role='alert']")
    EDIT_FIRST_NAME_FIELD = (By.XPATH, "//input[@id='edit_firstName']")
    ALERT_MSG_FIRST_NAME = (By.XPATH, "//div[@id='edit_firstName_help' and @role='alert']")
    EDIT_PHONE_FIELD = (By.XPATH, "//input[@id='edit_phone']")
    ALERT_MSG_PHONE = (By.XPATH, "//div[@id='edit_phone_help' and @role='alert']")
    UPLOAD_PHOTO_FIELD = (By.XPATH, "//input[@id='edit_urlLogo']")
    UPLOADED_PHOTO_APPEARED = (
        By.XPATH, "//div[contains(@class, 'ant-upload-list-item-done')"
    )
    CHANGE_PASSWORD_SECTION = (By.XPATH, "//input[@class='checkbox']")
    EDIT_CURRENT_PASSWORD = (By.XPATH, "//input[@id='edit_currentPassword']")
    ALERT_MSG_CURRENT_PASSWORD = (By.XPATH, "//div[@id='edit_currentPassword_help' and @role='alert']")
    NEW_PASSWORD_FIELD = (By.XPATH, "//input[@id='edit_password']")
    ALERT_MSG_NEW_PASSWORD = (By.XPATH, "//div[@id='edit_password_help' and @role='alert']")
    CONFIRM_NEW_PASSWORD = (By.XPATH, "//input[@id='edit_confirmPassword']")
    ALERT_MSG_CONFIRM_PASSWORD = (By.XPATH, "//div[@id='edit_confirmPassword_help' and @role='alert']")
    SAVE_CHANGES_BUTTON = (
        By.XPATH, "//button[contains(@class, 'submit-button')]"
    )
    CLOSE_BUTTON = (By.XPATH, "(//button[@class='ant-modal-close'])[2]")


class StepLocators:
    PREVIOUS_STEP = (By.XPATH, "//button[contains(@class, 'prev')]")
    NEXT_STEP = (By.XPATH, "//button[contains(@class, 'next')]")


class CentreMainInfoComponentLocators:
    NAME_FIELD = (By.XPATH, "//input[@id='basic_name']")
    ALERT_MSG_NAME_FIELD = (By.XPATH, "//div[@id='basic_name_help']")
    ADD_LOCATION_BUTTON = (By.XPATH, "//button[contains(@class, 'add-location-btn')]")
    LOCATIONS_LIST = (By.XPATH, "//div[contains(@class, 'location-list')]")
    LOCATIONS_CHOICE = (By.XPATH, "//div[@id='basic_locations']//label")


class CentreContactsComponentLocators:
    PHONE_FIELD = (By.XPATH, "//input[@id='contacts_contactТелефон']")


class CentreDescriptionComponentLocators:
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[@class='ant-input editor-textarea']")


class CentreClubsComponentLocators:
    CLUBS_CHOICE = (
        By.XPATH, "//div[@class='ant-checkbox-group']/*[position() <= 5]//label"
    )
    FINISH_BUTTON = (By.XPATH, "//button[@class='finish-btn']")


class AddLocationComponentLocators:
    NAME_FIELD = (By.XPATH, "//input[@id='name']")
    CITY_FIELD = (By.XPATH, "(//div[@class='ant-select-selector'])[2]")
    CITIES_LIST = (
        By.XPATH, "//div[@id='cityName_list']/..//div[contains(@class, 'inner')]/*[position() <= 5]"
    )
    REGION_FIELD = (By.XPATH, "(//div[@class='ant-select-selector'])[3]")
    REGIONS_LIST = (
        By.XPATH, "//div[@id='districtName_list']/..//div[contains(@class, 'inner')]/*[position() <= 5]"
    )
    ADDRESS_FIELD = (By.XPATH, "//input[@id='address']")
    COORDINATES_FIELD = (By.XPATH, "//input[@id='coordinates']")
    PHONE_FIELD = (By.XPATH, "//input[@id='phone']")
    ADD_BUTTON = (By.XPATH, "//div[contains(@class, 'add-location-button')]//button")
    ERROR_MESSAGES = (
        By.XPATH, "//div[contains(@class, 'modal-add-club')]//div[contains(@class, 'explain-error')]"
    )
    CLOSE_BUTTON = (By.XPATH, "(//span[@class='ant-modal-close-x'])[3]")


class ClubMainInfoComponentLocators:
    NAME_FIELD = (By.XPATH, "//input[@id='basic_name']")
    CATEGORIES_BOXES = (By.XPATH, "//label/span[contains(@class, 'ant-checkbox')]")
    AGE_FROM = (By.XPATH, "//input[@id='basic_ageFrom']")
    AGE_TO = (By.XPATH, "//input[@id='basic_ageTo']")


class ClubContactsComponentLocators:
    PHONE_FIELD = (By.XPATH, "//input[@id='basic_contactТелефон']")


class ClubDescriptionComponentLocators:
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[@id='basic_description']")
    FINISH_BUTTON = (By.XPATH, "//span[text()='Завершити']")
    DESCRIPTION_SUCESS = (By.XPATH, "//span[contains(@class, 'success')]")
    DESCRIPTION_ERROR_MSG = (By.XPATH, "//div[@id='basic_description_help']")
    CREATED_SUCCESS_MSG = (By.XPATH, "//div[contains(@class, 'ant-message-success')]")


class NewsCardComponentLocators:
    NEWS_DATE = (By.XPATH, ".//div[@id='newsDate']")
    NEWS_TITLE = (By.XPATH, ".//div[@id='newsTitle']")
    DETAILS_BUTTON = (By.XPATH, ".//span[@aria-label='arrow-right']")


class ClubCardComponentLocators:
    CLUB_TITLE = (By.XPATH, ".//div[@class='name']")
    DETAILS_BUTTON = (By.XPATH, ".//button[contains(@class, 'details-button')]")


class CalendarComponentLocators:
    # locators to year :
    YEAR_BUTTON = (By.XPATH, "//button[@class='ant-picker-year-btn']")
    NEXT_YEAR_BUTTON = (By.XPATH, "//button[@class='ant-picker-header-super-next-btn']")
    PREVIOUS_YEAR_BUTTON = (By.XPATH, "//button[@class='ant-picker-header-super-prev-btn']")
    # locators to month :
    MONTH_BUTTON = (By.XPATH, "//button[@class='ant-picker-month-btn']")
    NEXT_MONTH_BUTTON = (By.XPATH, "//button[@class='ant-picker-header-next-btn']")
    PREVIOUS_MONTH_BUTTON = (By.XPATH, "//button[@class='ant-picker-header-prev-btn']")
    # locators to day :
    DAY_BUTTON = (By.XPATH, "//td[contains(@class, 'ant-picker-cell-in-view')]")
