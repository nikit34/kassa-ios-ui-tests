from random import randrange
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
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.movies_locators.text_info_block)
        with allure.step('MoviesDetailsPage'):
            self.event_details_page = MoviesDetailsPage(driver)
            self.event_details_page.set_custom_wait(10)
            self.event_details_page.find_element(*self.movies_details_locators.text_event_name)
            self.event_details_page.find_element(*self.movies_details_locators.text_time)
            self.event_details_page.find_element(*self.movies_details_locators.btn_view_timetable)

    def test_002_from_details_to_featurer_by_back_button(self, driver):
        """Выход из Event details через кнопку назад"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.movies_locators.text_info_block)
        with allure.step('MoviesDetailsPage'):
            self.event_details_page = MoviesDetailsPage(driver)
            self.event_details_page.set_custom_wait(10)
            self.event_details_page.click(*self.movies_details_locators.btn_back)
            self.movie_page.find_element(*self.movies_locators.text_movie_title)

    def test_001_mathing_title_movie_feature_detail(self, driver):
        """Переход с главной на подробную страницу - совпадение по названию фильма"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            old_name_event = self.movie_page.find_element(*self.movies_locators.text_movie_title).text
            self.movie_page.click(*self.movies_locators.text_info_block)
        with allure.step('MoviesDetailsPage'):
            self.movies_details_page = MoviesDetailsPage(driver)
            self.movies_details_page.set_custom_wait(10)
            self.movies_details_page.matching_text(*self.movies_details_locators.text_event_name, equal=True,
                                                   pattern=old_name_event)

    def test_002_every_concert_in_featurer_has_content(self, driver):
        """Каждый event имеет название/описание + время, тег, цену"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            concert_base_canvas_row = self.movie_page.find_element(*self.movies_locators.video_row_carousel)

            random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
            while True:
                current_check = random_num % 3

                if current_check == 0:
                    concert_base_canvas_row.find_element(*self.movies_locators.text_movie_title)
                if current_check == 1:
                    concert_base_canvas_row.find_element(*self.movies_locators.text_place)
                elif current_check == 2:
                    concert_base_canvas_row.find_element(*self.movies_locators.btn_time_session)

                random_num //= 4
                if random_num == 0:
                    break
                self.movie_page.act.swipe(80, 30, 20, 30)