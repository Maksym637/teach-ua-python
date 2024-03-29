from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import TimeoutVariables, Urls


class BasePage:

    def __init__(self, driver, base_url=Urls.HOME_PAGE.value):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, TimeoutVariables.EXPLICIT_WAIT.value)
    
    def open(self, url=""):
        self.driver.get(self.base_url + url)

    def wait_element_to_appear(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_elements_to_appear(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def wait_different_elements_to_appear(self, locators):
        result_elements = []
        for locator in locators:
            result_elements.append(self.wait_element_to_appear(locator))
        return result_elements
    
    def scroll_until_element_in_view(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView();", element)
