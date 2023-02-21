from selenium.webdriver.common.by import By


class HomePageLocators:
    pass


class ProfilePageLocators:
    MENU_TITLE = (By.XPATH, "//div[@class='menu-title']")
    PROFILE_TITLE = (By.XPATH, "//div[@class='content-title']")
    USER_NAME_FIELD = (By.XPATH, "//div[@class='user-name']")
    USER_ROLE_FIELD = (By.XPATH, "//div[@class='user-role']")
    USER_PHONE_FIELD = (By.XPATH, "//div[@class='user-phone-data']")
    USER_EMAIL_FIELD = (By.XPATH, "//div[@class='user-email-data']")
    EDIT_PROFILE_BUTTON = (By.XPATH, "//div[@class='edit-button']//button")
    ADD_BUTTON = (By.XPATH, "//button[contains(@class, 'add-button')]")
    ADD_CLUB_BUTTON = (By.XPATH, "//li[contains(@data-menu-id, 'tmp_key-0')]")
    ADD_CENTRE_BUTTON = (By.XPATH, "//li[contains(@data-menu-id, 'tmp_key-1')]")
