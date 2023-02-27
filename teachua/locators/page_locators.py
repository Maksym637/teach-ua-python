from selenium.webdriver.common.by import By


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


class NewsPageLocators:
    NEWS_TITLE = (By.XPATH, "//div[@class='city-name-box']//h2")
    CLUBS_TITLE = (By.XPATH, "//div[@class='sider-header']//h2")
    NEWS_CARDS = (By.XPATH, "//div[@id='newsContainer']")
    CLUB_CARDS = (By.XPATH, "//div[@class='ant-card-body']")


class ViewNewsPageLocators:
    NEWS_TITLE = (By.XPATH, "//div[@id='major-title']")
    NEWS_DATE = (By.XPATH, "//div[@id='date']")
    NEWS_DESCRIPTION = (By.XPATH, "//div[@id='description']")
    DONATE_BUTTON = (By.XPATH, "//button[contains(@class, 'donate-button')]")


class ViewClubPageLocators:
    CLUB_TITLE = (By.XPATH, "//span[@class='club-name']")
    CLUB_DESCRIPTION = (By.XPATH, "//div[@class='content']")
    SUBSCRIBE_BUTTON = (
        By.XPATH, "//div[@class='apply-box']//button[contains(@class, 'apply-button')]"
    )


class ClubsPageLocators:
    CLUBS_TITLE = (By.XPATH, "//h2[@class='city-name']")
    CLUB_CARDS = (By.XPATH, "//div[@class='ant-card-body']")
