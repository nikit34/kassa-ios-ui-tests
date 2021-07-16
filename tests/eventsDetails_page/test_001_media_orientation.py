from time import sleep
import pytest
import allure

from locators.movies_locators import MoviesPageLocators
from locators.movies_details_locators import MoviesDetailsPageLocators
from screens.MoviesPage import MoviesPage
from screens.MoviesDetailsPage import MoviesDetailsPage
from app.debug_api import DebugAPI
from app.check_api import HandlersAPI
from utils.internet import enable_proxy


@allure.testcase('http://testrail.rambler-co.ru/index.php?/cases/view/712859', 'testrail points: all')
@pytest.mark.usefixtures('driver')
class Test_001_MoviePage:
    @classmethod
    def setup_class(cls):
        cls.movies_locators = MoviesPageLocators()
        cls.movies_details_locators = MoviesDetailsPageLocators()

    @staticmethod
    def teardown_class(cls):
        enable_proxy(mode=False)

    def test_001_change_screen_orientation(self, driver):
        """На фичере развернуть телефон
        тапнуть на превью любого мероприятия
        Перейти в галерею внутри карточки мероприятия, повернуть девайс
        Выйти из галереи"""
        dbg_api = DebugAPI.run(response=True, mapi_handler=HandlersAPI.url_creations_movie_filter)
        try:
            with allure.step('MoviesPage'):
                self.movie_page = MoviesPage(driver)
                self.movie_page.set_custom_wait(10)
                sleep(5)
                self.movie_page.click(*self.movies_locators.img_row_top)
            with allure.step('MoviesDetailsPage'):
                self.event_detail_page = MoviesDetailsPage(driver)
                self.event_detail_page.set_custom_wait(10)
                sleep(7)
                if self.event_detail_page.check_img_view(dbg_api):
                    self.event_detail_page.click(*self.movies_details_locators.img_gallery)
                    self.event_detail_page.check_img_gallery_orientation()
        finally:
            dbg_api.kill()

    def test_002_open_video_full_screen(self, driver):
        """Открыть видео в карточке на фулскрин"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.movies_locators.img_row_top)
        with allure.step('MoviesDetailsPage'):
            self.event_detail_page = MoviesDetailsPage(driver)
            self.event_detail_page.set_custom_wait(10)
            sleep(2)
            self.event_detail_page.click(*self.movies_details_locators.btn_screen_mode)
            self.event_detail_page.check_video_opened_full_mode()

