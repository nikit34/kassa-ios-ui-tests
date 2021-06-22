from random import randrange
from time import sleep
import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.TheatersPage import TheatersPage
from locators.theaters_locators import TheatersPageLocators
from locators.movies_locators import MoviesPageLocators


@pytest.mark.usefixtures('driver')
class Test_001_TheatersPage:
    @classmethod
    def setup_class(cls):
        cls.theaters_locators = TheatersPageLocators()
        cls.movies_locators = MoviesPageLocators()

    def test_001(self, driver):
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.movies_locators.btn_close_curtain)
            old_movie_title = self.movie_page.find_element(*self.movies_locators.text_movie_title).text
            self.movie_page.click(*self.theaters_locators.tab)
        with allure.step('TheatersPage'):
            self.theaters_page = TheatersPage(driver)
            self.theaters_page.set_custom_wait(10)
            self.theaters_page.matching_text(*self.theaters_locators.text_event_name, equal=False, pattern=old_movie_title)

    def test_002(self, driver):
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.movies_locators.btn_close_curtain)
            self.movie_page.click(*self.theaters_locators.tab)
        with allure.step('TheatersPage'):
            self.theaters_page = TheatersPage(driver)
            self.theaters_page.set_custom_wait(10)
            base_cover = self.theaters_page.find_element(*self.theaters_locators.base_cover)

            random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
            while True:
                current_check = random_num % 5

                if current_check == 0:
                    base_cover.find_element(*self.theaters_locators.text_event_name)
                elif current_check == 1:
                    base_cover.find_element(*self.theaters_locators.text_place_name)
                elif current_check == 2:
                    base_cover.find_element(*self.theaters_locators.text_date)
                elif current_check == 3:
                    base_cover.find_element(*self.theaters_locators.text_time)
                elif current_check == 4:
                    base_cover.find_element(*self.theaters_locators.btn_buy)

                random_num //= 4
                if random_num == 0:
                    break
                self.theaters_page.act.swipe(80, 30, 20, 30)

    def test_003_popular_is_visible(self, driver):
        """На экране присутствует блок Популярно сейчас """
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.theaters_locators.tab)
        with allure.step('TheatersPage'):
            self.theaters_page = TheatersPage(driver)
            self.theaters_page.set_custom_wait(10)
            sleep(5)
            self.theaters_page.act.swipe(50, 70, 50, 30)
            sleep(1)
            self.theaters_page.find_element(*self.theaters_locators.text_popular_title)
            self.theaters_page.find_element(*self.theaters_locators.btn_popular_all)
            self.theaters_page.find_element(*self.theaters_locators.text_popular_event_name)
            self.theaters_page.find_element(*self.theaters_locators.img_popular)



