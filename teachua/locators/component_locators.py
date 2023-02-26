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
