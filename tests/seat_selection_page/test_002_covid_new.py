import pytest
import allure

from locators.browser_locators import BrowserLocators
from locators.events_details_locators import EventsDetailsPageLocators
from locators.movies_locators import MoviesPageLocators
from locators.info_locators import InfoPageLocators
from locators.seat_selection_locators import SeatSelectionLocators
from screens.BrowserPage import BrowserPage
from screens.MoviesPage import MoviesPage
from screens.InfoPage import InfoPage



@allure.testcase('http://testrail.rambler-co.ru/index.php?/cases/view/768084', 'testrail points: all')
@pytest.mark.usefixtures('driver')
class Test_001_InfoPage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.seat_selection_locators = SeatSelectionLocators()
        cls.info_locators = InfoPageLocators()
        cls.event_detail_page_locators = EventsDetailsPageLocators()
        cls.browser_locators = BrowserLocators()

    def test_001_any_session(self, driver):
        """тапнуть на любой сеанс в расписании"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.find_element(*self.info_locators.btn_covid_next_old)
            self.info_page.find_element(*self.info_locators.btn_covid_cancel)
            self.info_page.find_element(*self.info_locators.btn_switch_allow)
            self.info_page.find_element(*self.info_locators.link_detail_conditions)

    def test_002_cancel(self, driver):
        """тапнуть на кнопку Отмена"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.click(*self.info_locators.btn_covid_cancel)
        with allure.step('MoviesPage'):
            self.info_page.not_displayed(*self.info_locators.btn_covid_cancel)
            self.movie_page.find_element(*self.movies_locators.btn_time_session)

    def test_003_any_session_yet(self, driver):
        """тапнуть на любой сеанс в расписании"""
        self.test_001_any_session(driver)

    def test_004_next(self, driver):
        """тапнуть по кнопке Подтвердить"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.check_state_selected(*self.info_locators.btn_covid_next_old, state=False)
            self.info_page.click(*self.info_locators.btn_covid_next)
            self.info_page.check_state_selected(*self.info_locators.btn_covid_next_old, state=False)

    def test_005_browser(self, driver):
        """перейти по ссылке, зашитой в тексте ячейки"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.click(*self.info_locators.link_detail_conditions)
        with allure.step('BrowserPage'):
            self.browser_page = BrowserPage(driver)
            self.browser_page.set_custom_wait(20)
            self.browser_page.find_element(*self.browser_locators.link_address)

    def test_006_browser_return(self, driver):
        """вернуться в приложение Касса"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.click(*self.info_locators.link_detail_conditions)
        with allure.step('BrowserPage'):
            self.browser_page = BrowserPage(driver)
            self.browser_page.set_custom_wait(20)
            self.browser_page.click(*self.browser_locators.btn_back_app)
        with allure.step('InfoPage'):
            self.info_page.find_element(*self.info_locators.link_detail_conditions)

    def test_007_state_switch(self, driver):
        """переключить свитчер одной из ячеек со спец значком,
        проверить состояние кнопки Подтвердить
        переключить все свитчеры со спецзначками, проверить состояние кнопки Подтвердить
        тапнуть на Подтвердить"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.click(*self.info_locators.btn_covid_next_old)
            self.info_page.check_state_selected(*self.info_locators.btn_covid_next_old, state=False)
            self.info_page.click(*self.info_locators.btn_switch_allow)
            self.info_page.check_state_selected(*self.info_locators.btn_covid_next_old, state=True)
            self.info_page.click(*self.info_locators.btn_covid_next_old)






