import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.TicketsPage import TicketsPage
from locators.tickets_locators import TicketsPageLocators
from locators.common_locators import CommonLocators



@pytest.mark.usefixtures('driver')
class Test_001_TicketsPage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.tickets_locators = TicketsPageLocators()

    def test_001_tickets_page_are_opened(self, driver):
        """Открыта вкладка Билеты"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.click(*self.common_locators.tab_ticket)
        with allure.step('TicketsPage'):
            self.tickets_page = TicketsPage(driver)
            self.tickets_page.set_custom_wait(20)
            self.tickets_page.click(*self.tickets_locators.btn_search_events)
