from teachua.base.base import Base
from teachua.components.header_component import HeaderComponent


class BasePage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.header = HeaderComponent(driver)
    
    def move_to_header(self):
        return self.header
