from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage

class DropDownPage(BasePage):

    _header = (By.TAG_NAME, 'h3')
    _dropdown = (By.ID, 'dropdown')

    sync_element = _dropdown

    @property
    def header(self):
        return self.find('_header')

    @property
    def dropdown(self):
        return self.find('_dropdown')

    @property
    def dropdown_select(self):
        selector = Select(self.dropdown)
        return selector

    def select_by_index(self):
        selector = self.dropdown_select
        selector.select_by_index(index)

    def