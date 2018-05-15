from Helpers.BaseTest import BaseTest
from Pages.InternetHomePage import InternetHomePage
from Pages.DropDownPage import DropDownPage
from selenium.webdriver.support.select import Select

class InternetTests(BaseTest):

    def test_home_page_element_verification(self):
        self.driver.get(self.page_url)

        home_page = InternetHomePage(self.driver)

        assert home_page.welcome_header.is_displayed()
        assert home_page.examples_header.is_displayed()
        assert len(home_page.example_links)


    def test_select_elements(self):
        self.driver.get(self.page_url)

        home_page = InternetHomePage(self.driver)
        drop_down = DropDownPage(self.driver)

        home_page.navigate_to_link('dropdown')
        drop_down.sync()

        assert drop_down.dropdown.is_displayed()

        drop_down.select_by_index(1)

        print(1)



