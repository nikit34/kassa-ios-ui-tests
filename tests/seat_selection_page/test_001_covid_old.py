import pytest
import allure
from selenium.common.exceptions import NoSuchElementException, InvalidSessionIdException

from locators.browser_locators import BrowserLocators
from locators.movies_details_locators import MoviesDetailsPageLocators
from locators.movies_locators import MoviesPageLocators
from locators.info_locators import InfoPageLocators
from screens.MoviesPage import MoviesPage
from screens.InfoPage import InfoPage
from screens.OnboardingPage import OnboardingPage
from screens.MoviesDetailsPage import MoviesDetailsPage
from screens.BrowserPage import BrowserPage
from locators.seat_selection_locators import SeatSelectionLocators
from screens.SeatSelectionPage import SeatSelectionPage



@allure.testcase('http://testrail.rambler-co.ru/index.php?/cases/view/760578', 'testrail points: 1')
@pytest.mark.usefixtures('driver_noCache')
class Test_001_InfoPage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.info_locators = InfoPageLocators()
        cls.event_detail_page_locators = MoviesDetailsPageLocators()

    def test_001_session(self, driver):
        """тапнуть на любой сеанс на экране"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver, 'Москва')
            self.onboarding_page.set_custom_wait(20)
            self.onboarding_page.skip_onboarding()
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.click(*self.movies_locators.btn_popup_next)
            covid_info = self.movie_page.get_json_covid_notification(city=self.onboarding_page.city)
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
            self.movie_page.act.click_by_coords(50, 30)
        with allure.step('EventDetailsPage'):
            self.event_detail_page = MoviesDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_view_timetable)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_time_session)
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.pass_without_info()


@allure.testcase('http://testrail.rambler-co.ru/index.php?/cases/view/760578', 'testrail points: from 2 to 8')
@pytest.mark.usefixtures('driver')
class Test_002_InfoPage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.seat_selection_locators = SeatSelectionLocators()
        cls.info_locators = InfoPageLocators()
        cls.event_detail_page_locators = MoviesDetailsPageLocators()
        cls.browser_locators = BrowserLocators()

    def test_002_cancel(self, driver):
        """тапнуть на Отмена"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
        with allure.step('EventDetailsPage'):
            self.event_detail_page = MoviesDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_view_timetable)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_time_session)
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.click(*self.info_locators.btn_covid_cancel)
            self.info_page.not_displayed(*self.info_locators.btn_covid_cancel)
        with allure.step('EventDetailsPage'):
            self.event_detail_page.find_element(*self.event_detail_page_locators.btn_view_timetable)

    def test_003_repeat_to_browser(self, driver):
        """тапнуть на сеанс из шага 1
        тапнуть на Подробные условия"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(30)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
        with allure.step('EventDetailsPage'):
            self.event_detail_page = MoviesDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_view_timetable)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_time_session)
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.click(*self.info_locators.link_detail_conditions)
        with allure.step('BrowserPage'):
            self.browser_page = BrowserPage(driver)
            self.browser_page.set_custom_wait(20)
            self.browser_page.find_element(*self.browser_locators.link_address)

    def test_004_browser_return(self, driver):
        """вернуться в приложение Кассы"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(30)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
        with allure.step('EventDetailsPage'):
            self.event_detail_page = MoviesDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_view_timetable)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_time_session)
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

    def test_005_state_switch(self, driver):
        """тапнуть на Продолжить
        переключить свитчер на вкл
        тапнуть на Продолжить"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            covid_info = self.movie_page.get_json_covid_notification(city='Москва')
            assert len(covid_info) == 5, '[FAILED] covid information has not been added'
        with allure.step('EventDetailsPage'):
            self.event_detail_page = MoviesDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_view_timetable)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_time_session)
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.click(*self.info_locators.btn_covid_next_old)
            self.info_page.check_state_selected(*self.info_locators.btn_covid_next_old, state=False)
            self.info_page.click(*self.info_locators.btn_switch_allow)
            self.info_page.check_state_selected(*self.info_locators.btn_covid_next_old, state=True)
            self.info_page.click(*self.info_locators.btn_covid_next_old)
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(20)
            self.seat_selection_page.find_element(*self.seat_selection_locators.img_screen)



