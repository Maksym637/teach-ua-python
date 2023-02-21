from selenium.webdriver.common.by import By


class HeaderComponentLocators:
    CLUBS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'clubs')]")
    NEWS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'news')]")
    USER_ICON = (By.XPATH, "//div[contains(@class, 'user-profile')]")


class GuestMenuComponentLocators:
    REGISTER_BUTTON = (By.XPATH, "//li[contains(@data-menu-id, 'register')]")
    LOGIN_BUTTON = (By.XPATH, "//li[contains(@data-menu-id, 'login')]")


class UserMenuComponentLocators:
    pass


class AdminMenuComponentLocators:
    pass


class LoginComponentLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@id='basic_email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='basic_password']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(@class, 'login-button')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'ant-message-success')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'ant-message-error')]")
