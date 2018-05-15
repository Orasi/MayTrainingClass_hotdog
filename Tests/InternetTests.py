from Helpers.BaseTest import BaseTest
from Pages.DropDownPage import DropDownPage
from selenium.webdriver.support.select import Select

class InternetTests(BaseTest):

    def test_home_page_element_verification(self):
        self.driver.get(self.page_url)

        home_page = DropDownPage(self.driver)

        assert home_page.welcome_header.is_displayed()
        # assert home_page.examples_header.is_displayed()
        assert home_page.example_option

    def test_select_elements(self):
        self.driver.get(self.page_url)

        home_page = DropDownPage(self.driver)

        home_page.navigate_to_link('dropdown')
        print(1)