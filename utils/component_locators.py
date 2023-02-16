from selenium.webdriver.common.by import By


class HeaderComponentLocators:
    LOGO = (By.XPATH, "//div[@class='left-side-menu']")
    CLUBS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'clubs')]")
    NEWS_BUTTON = (By.XPATH, "//li[contains(@data-menu-id,'news')]")
    USER_ICON = (By.XPATH, "//span[contains(@class, 'avatarIfNotLogin')]")
