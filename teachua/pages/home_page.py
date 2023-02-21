from teachua.base.base_page import BasePage
from teachua.components.header_component import HeaderComponent


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)
