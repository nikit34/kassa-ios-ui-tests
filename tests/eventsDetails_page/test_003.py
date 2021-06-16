import pytest
import allure
from screens.MoviesPage import MoviesPage
from screens.MoviesDetailsPage import MoviesDetailsPage
from locators.movies_locators import MoviesPageLocators
from locators.movies_details_locators import MoviesDetailsPageLocators



@allure.feature('eventsDetails_page')
@pytest.mark.usefixtures('driver')
class Test_001_EventDetailsPage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.movies_details_locators = MoviesDetailsPageLocators()

    def test_001_all_fields_are_available(self, driver):
        """Event details показывается после закрытия расписания"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.click(*self.movies_locators.text_info_block)
        with allure.step('MoviesDetailsPage'):
            self.event_details_page = MoviesDetailsPage(driver)
            self.event_details_page.set_custom_wait(20)
            self.event_details_page.find_element(*self.movies_details_locators.text_event_name)
            self.event_details_page.find_element(*self.movies_details_locators.text_time)
            self.event_details_page.find_element(*self.movies_details_locators.btn_view_timetable)

    def test_002_from_details_to_featurer_by_back_button(self, driver):
        """Выход из Event details через кнопку назад"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.click(*self.movies_locators.text_info_block)
        with allure.step('MoviesDetailsPage'):
            self.event_details_page = MoviesDetailsPage(driver)
            self.event_details_page.set_custom_wait(20)
            self.event_details_page.click(*self.movies_details_locators.btn_back)
            self.movie_page.find_element(*self.movies_locators.text_movie_title)