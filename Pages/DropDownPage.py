from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage
from selenium.webdriver.support.select import Select

class DropDownPage(BasePage):

    _header = (By.TAG_NAME,'h3')
    _dropdown = (By.ID,'dropdown')

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

    def select_by_index(self,index):
        selector = self.dropdown_select
        selector.select_by_index(index)

    def select_by_text(self,text):
        selector = self.dropdown_select
        selector.select_by_visible_text(text)

    def select_by_value(self,value):
        selector = self.dropdown_select
        selector.select_by_value(value)




