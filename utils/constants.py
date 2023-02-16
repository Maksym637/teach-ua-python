from enum import Enum


class TimeoutVariables(Enum):
    IMPLICIT_WAIT = 50
    EXPLICIT_WAIT = 100


class Scripts(Enum):
    LOCAL_STORAGE = "localStorage.getItem('role')"


class Urls(Enum):
    HOME_PAGE = "https://speak-ukrainian.org.ua/dev/"
    PROFILE_PAGE = "https://speak-ukrainian.org.ua/dev/user/1/page"
