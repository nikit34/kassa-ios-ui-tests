from random import randrange
from time import sleep
import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.PerformancesPage import PerformancePage
from locators.performance_locators import PerformancePageLocators
from locators.movies_locators import MoviesPageLocators


@pytest.mark.skip('performance is not exists')
@pytest.mark.usefixtures('driver')
class Test_001_PerformancePage:
    @classmethod
    def setup_class(cls):
        cls.performance_locators = PerformancePageLocators()
        cls.movies_locators = MoviesPageLocators()

    def test_001_performance_page_is_open(self, driver):
        """Вкладка Спектакли открыта"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.find_element(*self.movies_locators.text_title)
            old_movie_title = self.movie_page.find_element(*self.movies_locators.text_movie_title).text
            self.movie_page.click(*self.performance_locators.tab)
        with allure.step('PerformancePage'):
            self.performance_page = PerformancePage(driver)
            self.performance_page.set_custom_wait(10)
            self.performance_page.matching_text(*self.performance_locators.text_event_title, equal=False, pattern=old_movie_title)

    def test_002_every_perfomance_in_featurer_has_content(self, driver):
        """Каждый event имеет название/описание + время, тег, цену"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.performance_locators.tab)
        with allure.step('PerformancePage'):
            self.performance_page = PerformancePage(driver)
            self.performance_page.set_custom_wait(10)
            performance_base_canvas_row = self.performance_page.find_element(*self.performance_locators.video_row_carousel)

            random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
            while True:
                current_check = random_num % 4

                if current_check == 0:
                    performance_base_canvas_row.find_element(*self.performance_locators.text_event_title)
                elif current_check == 1:
                    performance_base_canvas_row.find_element(*self.performance_locators.text_data)
                elif current_check == 2:
                    performance_base_canvas_row.find_element(*self.performance_locators.text_time)
                elif current_check == 3:
                    performance_base_canvas_row.find_element(*self.performance_locators.btn_price)

                random_num //= 4
                if random_num == 0:
                    break
                self.performance_page.act.swipe(80, 30, 20, 30)

    def test_003_popular_is_visible(self, driver):
        """На экране присутствует блок Популярно сейчас """
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.performance_locators.tab)
        with allure.step('PerformancePage'):
            self.performance_page = PerformancePage(driver)
            self.performance_page.set_custom_wait(10)
            sleep(5)
            self.performance_page.act.swipe(50, 70, 50, 30)
            sleep(1)
            self.performance_page.find_element(*self.performance_locators.text_popular_title)
            self.performance_page.find_element(*self.performance_locators.btn_popular_all)
            self.performance_page.find_element(*self.performance_locators.text_popular_event_name)
            self.performance_page.find_element(*self.performance_locators.img_popular)



