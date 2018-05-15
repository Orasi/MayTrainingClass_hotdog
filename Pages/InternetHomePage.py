from selenium.webdriver.common.by import By
from Helpers.BasePage import BasePage

class InternetHomePage(BasePage):

    _welcome_header = (By.TAG_NAME, 'h1')
    _examples_header = (By.TAG_NAME, 'h2')
    _example_link = (By.TAG_NAME, 'a')

    @property
    def welcome_header(self):
        return self.find('_welcome_header')

    @property
    def examples_header(self):
        return self.find('_examples_header')

    @property
    def example_links(self):
        return self.find('_example_link')

    def navigate_to_link(self,example_name):
        home_page_links = self.example_links

        for link in home_page_links:
            if link.text.lower().strip() == example_name.lower().strip():
                link.click()
                break