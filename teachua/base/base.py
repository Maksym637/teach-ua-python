from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import TimeoutVariables


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TimeoutVariables.EXPLICIT_WAIT.value)
    
    def open(self, url):
        self.driver.get(url)

    def wait_element_to_appear(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
