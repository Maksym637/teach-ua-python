import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.constants import TimeoutVariables, Urls


# Only for the first time :
from selenium.webdriver.common.by import By


@pytest.fixture
def configure_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get(Urls.HOME_PAGE.value)
    driver.implicitly_wait(TimeoutVariables.IMPLICIT_WAIT.value)

    # Only for the first time :
    driver.find_element(By.ID, "details-button").click()
    driver.find_element(By.ID, "proceed-link").click()

    yield driver
    driver.quit()
