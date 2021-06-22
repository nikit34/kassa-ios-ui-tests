from random import randrange
import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.ConcertsPage import ConcertsPage
from locators.movies_locators import MoviesPageLocators
from locators.concerts_locators import ConcertsPageLocators


@allure.feature('eventsDetails_page')
@pytest.mark.usefixtures('driver')
class Test_001_ConcertsPage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.concerts_locators = ConcertsPageLocators()

    def test_001(self, driver):
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.movies_locators.btn_close_curtain)
            self.movie_page.click(*self.concerts_locators.tab)
        with allure.step('ConcertsPage'):
            self.concerts_page = ConcertsPage(driver)
            self.concerts_page.set_custom_wait(10)
            base_cover = self.concerts_page.find_element(*self.concerts_locators.base_cover)

            random_num = randrange(64, 255)  # 1000 to 3333 in 4 notation
            while True:
                current_check = random_num % 5

                if current_check == 0:
                    base_cover.find_element(*self.concerts_locators.text_event_name)
                elif current_check == 1:
                    base_cover.find_element(*self.concerts_locators.text_place_name)
                elif current_check == 2:
                    base_cover.find_element(*self.concerts_locators.text_date)
                elif current_check == 3:
                    base_cover.find_element(*self.concerts_locators.text_time)
                elif current_check == 4:
                    base_cover.find_element(*self.concerts_locators.btn_buy)

                random_num //= 4
                if random_num == 0:
                    break
                self.movie_page.act.swipe(80, 30, 20, 30)