from teachua.base.base_component import BaseComponent
from teachua.components.header_component import HeaderComponent


class BasePage(BaseComponent):

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)
    
    def move_to_header(self):
        return self.header
