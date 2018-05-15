from Helpers.BaseTest import BaseTest
from Pages.InternetHomePage import InternetHomePage
from Pages.DropDownPage import DropDownPage

class InternetTest(BaseTest):

    def test_home_page_element_verification(self):
        self.driver.get(self.page_url)

        home_page = InternetHomePage(self.driver)

        assert home_page.welcome_header.is_displayed()
        assert home_page.examples_header.is_displayed()
        assert len(home_page.example_links)

    def test_select_elements(self):
        self.driver.get(self.page_url)

        home_page = InternetHomePage(self.driver)

        home_page.navigate_to_link('dropdown')
        drop_down_page = DropDownPage(self.driver)
        drop_down_page.sync()

        drop_down_page.select_by_value('2')
