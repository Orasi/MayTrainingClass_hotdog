from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from selenium.webdriver.support.select import Select
class DropDownPage(BasePage):

    # dropdown option
    _dropdown_options = (By.ID, 'dropdown')

    # header
    _header = (By.TAG_NAME, 'h3')

    sync_element = _dropdown_options

    @property
    def drop_down_options(self):
        return self.find('_dropdown_options')

    @property
    def drop_down_header(self):
        return self.find('_header')

    def dropdown_select(self):
        select = Select(self.drop_down_options)
        return select

    def select_by_index(self, index):
        selector = self.dropdown_select()
        selector.select_by_index(index)

    def select_by_value(self, value):
        selector = self.dropdown_select()
        selector.select_by_value(value)

        for options in drop_down_name:
            if options.text.lower().strip() == option_name.lower().strip():
                options.click()