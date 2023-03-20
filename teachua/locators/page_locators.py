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


class ChallengesPageLocators:
    SEARCH_CHALLENGES = (By.XPATH, "//input[@placeholder='Пошук по челенджам']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class, 'ant-input-search-button')]")
    DELETE_CHALLENGE = (By.XPATH, "(//span[@class='table-action' and contains (text(), 'Видалити')])[1]")
    CONFIRM_DELETE_CHALLENGE = (By.XPATH, "//button[contains(@class, 'popConfirm-ok-button')]")
    ADD_CHALLENGE_BUTTON = (By.XPATH, "//a[@href='/dev/admin/addChallenge']")


class AddChallengePageLocators:
    CHALLENGES_LIST = (By.XPATH, "//a[@class='back-btn'and @href='/dev/admin/challenges']")
    SORT_NUMBER_FIELD = (By.XPATH, "//input[@id='sortNumber']")
    NAME_FIELD = (By.XPATH, "//input[@id='name']")
    TITLE_FIELD = (By.XPATH, "//input[@id='title']")
    DESCRIPTION_FIELD = (By.XPATH, "//div[contains(@class,'ql-editor')]")
    PHOTO_FIELD = (By.XPATH, "//input[@id='picture']")
    PHOTO_APPEARED = (By.XPATH, "//div[contains(@class, 'ant-upload-list-item-done')]")
    SAVE_BUTTON = (By.XPATH, "//button[contains(@class, 'add-contact-type-button')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='ant-message-custom-content ant-message-success']")


class TasksPageLocators:
    ADD_TASK_BUTTON = (By.XPATH, "//button[contains(@class, 'add-btn')]")


class AddTaskPageLocators:
    START_DATE_FIELD = (By.XPATH, "//input[@id='startDate']")
    PHOTO_FIELD = (By.XPATH, "//input[@id='picture']")
    PHOTO_APPEARED = (By.XPATH, "//div[@class='ant-upload-list-picture-card-container']")
    NAME_FIELD = (By.XPATH, "//input[@id='name']")
    TITLE_FIELD = (
        By.XPATH, "//label[text()='Заголовок']//parent::div//following-sibling::div//div[contains(@class, 'ql-editor')]/p"
    )
    DESCRIPTION_FIELD = (
        By.XPATH, "//label[text()='Опис']//parent::div//following-sibling::div//div[contains(@class, 'ql-editor')]/p"
    )
    CHALLENGE_FIELD = (
        By.XPATH, "//div[contains(@class, 'ant-col-14')]//div[@class='ant-select-selector']"
    )
    CHALLENGE_LIST = (By.XPATH, "//div[@class='rc-virtual-list-holder-inner']/*[position() <= 5]")
    SAVE_BUTTON = (By.XPATH, "//span[text()='Зберегти']//parent::button")
    ALERT_MESSAGE = (By.XPATH, "//div[contains(@class, 'ant-message-warning')]")
