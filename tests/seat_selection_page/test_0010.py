import pytest
import allure

from locators.info_locators import InfoPageLocators
from locators.checkout_locators import CheckoutPageLocators
from screens.CheckOutPage import CheckOutPage
from screens.MoviesPage import MoviesPage
from screens.InfoPage import InfoPage
from screens.SeatSelectionPage import SeatSelectionPage
from locators.seat_selection_locators import SeatSelectionLocators



@pytest.mark.usefixtures('driver')
class Test_001_PerformancePage:
    @classmethod
    def setup_class(cls):
        cls.seat_selection_locators = SeatSelectionLocators()
        cls.checkout_locators = CheckoutPageLocators()
        cls.info_locators = InfoPageLocators()

    def test_001_open_checkout_page(self, driver):
        """Выбор места открыт"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.proccessing_error()
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection()
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('CheckOutPage'):
            self.check_out_page = CheckOutPage(driver)
            self.check_out_page.set_custom_wait(10)
            self.check_out_page.find_element(*self.checkout_locators.btn_buy)

