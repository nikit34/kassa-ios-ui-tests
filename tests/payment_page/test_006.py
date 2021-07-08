import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.SeatSelectionPage import SeatSelectionPage
from screens.CheckOutPage import CheckOutPage
from screens.InfoPage import InfoPage
from locators.seat_selection_locators import SeatSelectionLocators
from locators.checkout_locators import CheckoutPageLocators


@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures('driver')
class Test_001_PaymentPage:
    @classmethod
    def setup_class(cls):
        cls.checkout_locators = CheckoutPageLocators()
        cls.seat_selection_locators = SeatSelectionLocators()

    def test_001_payment_page_is_open(self, driver):
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
            self.check_out_page.find_element(*self.checkout_locators.block_ticket)
            self.check_out_page.find_element(*self.checkout_locators.btn_buy_ipay)
            self.check_out_page.click(*self.checkout_locators.btn_buy)
