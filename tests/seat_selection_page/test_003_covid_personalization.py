from time import sleep

import pytest
import allure

from locators.browser_locators import BrowserLocators
from locators.info_locators import InfoPageLocators
from locators.seat_selection_locators import SeatSelectionLocators
from screens.MoviesPage import MoviesPage
from screens.InfoPage import InfoPage
from screens.SeatSelectionPage import SeatSelectionPage
from screens.PaymentPage import PaymentPage
from locators.payment_locators import PaymentPageLocators
from screens.PaymentDetailsPage import PaymentDetailsPage
from screens.BrowserPage import BrowserPage
from locators.payment_details_locators import PaymentDetailsPageLocators



@allure.testcase('http://testrail.rambler-co.ru/index.php?/cases/view/768085', 'testrail points: all')
@pytest.mark.usefixtures('driver')
class Test_001_InfoPage:
    @classmethod
    def setup_class(cls):
        cls.seat_selection_locators = SeatSelectionLocators()
        cls.info_locators = InfoPageLocators()
        cls.browser_locators = BrowserLocators()
        cls.payment_locators = PaymentPageLocators()
        cls.payment_details_locators = PaymentDetailsPageLocators()

    def test_001_012_any_session(self, driver):
        """на схеме зала выбрать 2 места, тапнуть на Продолжить"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)

    def test_002_empty_block(self, driver):
        """new: тапнуть на кнопку детали,
        проверить количество билетов,
        вернуться на страницу оплаты
        old: проверить количество и содержание блоков с пустыми полями"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            self.payment_page.click(*self.payment_locators.btn_movie_details)
        with allure.step('PaymentDetailsPage'):
            self.payment_details_page = PaymentDetailsPage(driver)
            self.payment_details_page.set_custom_wait(10)
            self.payment_details_page.find_element(*self.payment_details_locators.btn_tickets)
            self.payment_details_page.find_element(*self.payment_details_locators.btn_products)
            self.payment_details_page.check_count_tickets(count_tickets=2)

    def test_003_input_block(self, driver):
        """заполнить один блок с полями рандомными валидными данными"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            sleep(2)
            self.payment_page.act.swipe(50, 80, 50, 20)
            self.payment_page.find_element(*self.payment_locators.fulled_field_input_email)
            self.payment_page.input('+79779918074', *self.payment_locators.input_phone)
            self.payment_page.click(*self.payment_locators.btn_done)
            self.payment_page.find_element(*self.payment_locators.btn_payment)
            self.payment_page.find_element(*self.payment_locators.btn_apple_payment)

    def test_004_pass_link(self, driver):
        """в блоке со ссылками перейти по ссылке"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            sleep(2)
            self.payment_page.act.swipe(50, 80, 50, 20)
            self.payment_page.click(*self.payment_locators.link_personal_access)
        with allure.step('BrowserPage'):
            self.browser_page = BrowserPage(driver)
            self.browser_page.set_custom_wait(10)
            self.browser_page.find_element(*self.browser_locators.link_address)

    def test_006_continue(self, driver):
        """тапнуть на Продолжить"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            self.payment_page.click(*self.payment_locators.btn_payment)
            self.payment_page.find_element(*self.payment_locators.btn_payment)

    def test_007_switcher(self, driver):
        """в блоке со свитчером переключить свитчер"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            sleep(2)
            self.payment_page.act.swipe(50, 60, 50, 40)
            self.payment_page.click(*self.payment_locators.btn_bank_card)
            self.payment_page.check_status_switcher(*self.payment_locators.radio_bank_card, status=True)

    def test_008_continue(self, driver):
        """тапнуть на кнопку Продолжить"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            self.payment_page.click(*self.payment_locators.btn_payment)
            self.payment_page.find_element(*self.payment_locators.btn_payment)

    def test_009_input_all_fields(self, driver):
        """заполнить все незаполненные поля
        тапнуть на Продолжить"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            sleep(2)
            self.payment_page.act.swipe(50, 80, 50, 20)
            self.payment_page.find_element(*self.payment_locators.fulled_field_input_email)
            self.payment_page.input('+79779918074', *self.payment_locators.input_phone)
            self.payment_page.click(*self.payment_locators.btn_payment)
            self.payment_page.find_element(*self.payment_locators.btn_payment)

    def test_011_back(self, driver):
        """тапнуть на чекауте на кнопку назад"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            self.payment_page.click(*self.payment_locators.btn_cancel)

    def test_012_continue(self, driver):
        """тапнуть на Продолжить"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)

    def test_013_two_buttons(self, driver):
        """new: увидеть кнопки ОПЛАТИТЬ и Купить с Apple Pay"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            self.payment_page.find_element(*self.payment_locators.btn_payment)
            self.payment_page.find_element(*self.payment_locators.btn_apple_payment)

    def test_014_details_two_tabs(self, driver):
        """new: тапнуть на детали через название
        проверить переключение вкладок Билеты-Товары"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            self.payment_page.click(*self.payment_locators.btn_movie_details)
        with allure.step('PaymentDetailsPage'):
            self.payment_details_page = PaymentDetailsPage(driver)
            self.payment_details_page.set_custom_wait(10)
            self.payment_details_page.click(*self.payment_details_locators.btn_products)
            self.payment_details_page.not_displayed(*self.payment_details_locators.block_first_ticket)
            self.payment_details_page.click(*self.payment_details_locators.btn_tickets)
            self.payment_details_page.check_count_tickets(count_tickets=2)

    def test_015_details_cancel(self, driver):
        """new: тапнуть на детали
        тапнуть на закрыть
        билеты не сбросились"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(10)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(10)
            self.seat_selection_page.skip_seat_selection(count_places=2)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_continue)
        with allure.step('PaymentPage'):
            self.payment_page = PaymentPage(driver)
            self.payment_page.set_custom_wait(10)
            self.payment_page.click(*self.payment_locators.btn_movie_details)
        with allure.step('PaymentDetailsPage'):
            self.payment_details_page = PaymentDetailsPage(driver)
            self.payment_details_page.set_custom_wait(10)
            self.payment_details_page.click(*self.payment_details_locators.btn_cancel)
        with allure.step('PaymentPage'):
            self.payment_page.click(*self.payment_locators.btn_movie_details)
        with allure.step('PaymentDetailsPage'):
            self.payment_details_page.check_count_tickets(count_tickets=2)


