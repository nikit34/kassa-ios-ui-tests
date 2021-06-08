from time import sleep
import pytest
import allure

from app.api import DebugAPI
from locators.events_details_locators import EventsDetailsPageLocators
from locators.movies_locators import MoviesPageLocators
from locators.shedule_locators import ShedulePageLocators
from screens.MoviesPage import MoviesPage
from screens.EventDetailsPage import EventsDetailsPage
from screens.ShedulePage import ShedulePage


@pytest.mark.usefixtures('driver')
class Test_001_ShedulePage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.shedule_locators = ShedulePageLocators()
        cls.event_detail_page_locators = EventsDetailsPageLocators()

    @classmethod
    def teardown_class(cls):
        dbg_api = DebugAPI()
        dbg_api.enable_proxy(mode=False)
        dbg_api.clear_buffer()

    def test_001_elements_exists(self, driver):
        """тапнуть на фичерс,
        тапнуть на смотреть расписание,
        найти кнопку отмены, кнопку карты, поле поиска"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(10)
            self.movie_page.act.click_by_coords(50, 30)
        with allure.step('EventDetailsPage'):
            self.event_detail_page = EventsDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_view_timetable)
        with allure.step('ShedulePage'):
            self.shedule_page = ShedulePage(driver)
            self.shedule_page.set_custom_wait(20)
            self.shedule_page.find_element(*self.shedule_locators.btn_back)
            self.shedule_page.find_element(*self.shedule_locators.btn_map)
            self.shedule_page.find_element(*self.shedule_locators.search_field)

    def test_002_valid_filters(self, driver):
        """тапнуть на фичерс,
        тапнуть на смотреть расписание,
        проверить соответствие фильтров и ответа сервера
        проверить порядок фильтров
        """
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(10)
            self.movie_page.act.click_by_coords(50, 30)
            dbg_api = DebugAPI.run(request=False)
        with allure.step('EventDetailsPage'):
            self.event_detail_page = EventsDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_view_timetable)
        with allure.step('ShedulePage'):
            self.shedule_page = ShedulePage(driver)
            self.shedule_page.set_custom_wait(20)
            self.shedule_page.check_rows_filters(dbg_api)
            dbg_api.kill()
            dbg_api.clear_buffer()

    def test_003_check_time_ticket_filter(self, driver):
        """тапнуть на фичерс,
        тапнуть на смотреть расписание,
        проверять соответствие времени на билетах с выставленными фильтрами"""
        with allure.step('MoviesPage'):
            dbg_api = DebugAPI.run(request=False)
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(10)
            self.movie_page.act.click_by_coords(50, 30)
        with allure.step('EventDetailsPage'):
            self.event_detail_page = EventsDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.click(*self.event_detail_page_locators.btn_view_timetable)
        with allure.step('ShedulePage'):
            self.shedule_page = ShedulePage(driver)
            self.shedule_page.set_custom_wait(20)
            self.shedule_page.compare_time_tickets_second_filter(dbg_api)
            dbg_api.kill()
            dbg_api.clear_buffer()