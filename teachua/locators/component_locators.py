from selenium.webdriver.common.by import By


class HeaderComponentLocators:
    LOGO = (By.XPATH, "//div[@class='left-side-menu']")
    CLUBS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'clubs')]")
    NEWS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'news')]")
    USER_ICON_NOT_LOGIN = (By.XPATH, "//span[contains(@class, 'avatarIfNotLogin')]")
    USER_ICON_LOGIN = (By.XPATH, "//span[contains(@class, 'avatarIfLogin')]")


class GuestMenuComponentLocators:
    REGISTER_BUTTON = (By.XPATH, "//li[contains(@data-menu-id, 'register')]")
    LOGIN_BUTTON = (By.XPATH, "//li[contains(@data-menu-id, 'login')]")


class UserMenuComponentLocators:
    pass


class LoginComponentLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@id='basic_email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='basic_password']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(@class, 'login-button')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'ant-message-success')]")
    ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, 'ant-message-error')]")
