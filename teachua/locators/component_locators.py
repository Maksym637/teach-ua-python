from selenium.webdriver.common.by import By


class HeaderComponentLocators:
    CLUBS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'clubs')]")
    NEWS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'news')]")
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
    EDIT_FIRST_NAME_FIELD = (By.XPATH, "//input[@id='edit_firstName']")
    EDIT_PHONE_FIELD = (By.XPATH, "//input[@id='edit_phone']")
    UPLOAD_PHOTO_FIELD = (By.XPATH, "//input[@id='edit_urlLogo']")
    UPLOADED_PHOTO_APPEARED = (
        By.XPATH, "//div[contains(@class, 'ant-upload-list-item-done')"
    )
    CHANGE_PASSWORD_SECTION = (By.XPATH, "//input[@class='checkbox']")
    EDIT_CURRENT_PASSWORD = (By.XPATH, "//input[@id='edit_currentPassword']")
    NEW_PASSWORD_FIELD = (By.XPATH, "//input[@id='edit_password']")
    CONFIRM_NEW_PASSWORD = (By.XPATH, "//input[@id='edit_confirmPassword']")
    ERROR_MESSAGES = (By.XPATH, "//div[@class='ant-form-item-explain-error']")
    SAVE_CHANGES_BUTTON = (
        By.XPATH, "//button[contains(@class, 'submit-button')]"
    )
    CLOSE_BUTTON = (By.XPATH, "(//button[@class='ant-modal-close'])[2]")


class CentreStepLocators:
    PREVIOUS_STEP = (By.XPATH, "//button[contains(@class, 'prev-btn')]")
    NEXT_STEP = (By.XPATH, "//button[contains(@class, 'next-btn')]")


class CentreMainInfoComponentLocators:
    NAME_FIELD = (By.XPATH, "//input[@id='basic_name']")
    ADD_LOCATION_BUTTON = (By.XPATH, "//button[contains(@class, 'add-location-btn')]")
    LOCATIONS_CHOICE = (By.XPATH, "//div[@id='basic_locations']/*[position() <= 3]")


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
