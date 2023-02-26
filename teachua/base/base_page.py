from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.constants import TimeoutVariables


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TimeoutVariables.EXPLICIT_WAIT.value)
    
    def open(self, url):
        self.driver.get(url)

    def wait_element_to_appear(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def wait_element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    def wait_elements_to_appear(self, locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def wait_different_elements_to_appear(self, elements):
        result_elements = []
        for element in elements:
            result_elements.append(self.wait_element_to_appear(element))
        return result_elements
