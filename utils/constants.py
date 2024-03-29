from enum import Enum


class TimeoutVariables(Enum):
    IMPLICIT_WAIT = 50
    EXPLICIT_WAIT = 100


class Urls(Enum):
    HOME_PAGE = "https://speak-ukrainian.org.ua/dev/"
    TEST_CASES = "https://jira.softserve.academy/browse"


class Paths(Enum):
    CREDENTIALS_PATH = "./credentials.ini"
