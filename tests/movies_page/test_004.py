from random import randrange
from time import sleep
import pytest
import allure

from locators.movies_locators import MoviesPageLocators
from locators.info_locators import InfoPageLocators
from locators.seat_selection_locators import SeatSelectionLocators
from locators.movies_details_locators import MoviesDetailsPageLocators
from locators.shedule_locators import ShedulePageLocators
from screens.MoviesDetailsPage import MoviesDetailsPage
from screens.MoviesPage import MoviesPage
from locators.common_locators import CommonLocators
from screens.InfoPage import InfoPage
from screens.SeatSelectionPage import SeatSelectionPage
from screens.ShedulePage import ShedulePage


@pytest.mark.usefixtures('driver')
class Test_001_MoviePage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.movies_locators = MoviesPageLocators()
        cls.seat_selection_locators = SeatSelectionLocators()
        cls.movies_details_locators = MoviesDetailsPageLocators()
        cls.shedule_locators = ShedulePageLocators()
        cls.info_locators = InfoPageLocators()

    def test_001_open_app_and_tab_movies_is_selected(self, driver):
        """Вкладка КИНО выбрана при открытии приложения"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.check_state_selected(*self.common_locators.tab_trend, state=True)
            self.movie_page.check_state_selected(*self.common_locators.tab_search, state=False)
            self.movie_page.check_state_selected(*self.common_locators.tab_ticket, state=False)
            self.movie_page.check_state_selected(*self.common_locators.tab_places, state=False)
            self.movie_page.check_state_selected(*self.common_locators.tab_profile, state=False)

    def test_002_every_movie_has_a_valid_content_in_featurer(self, driver):
        """Каждый фильм в fitcher имеет название/описание + время, тег, цену"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            movie_base_canvas_row = self.movie_page.find_element(*self.movies_locators.video_row_carousel)

            random_num = randrange(9, 26)  # 100 to 222 in 3 notation
            while True:
                current_check = random_num % 3

                if current_check == 0:
                    movie_base_canvas_row.find_element(*self.movies_locators.text_movie_title)
                elif current_check == 1:
                    movie_base_canvas_row.find_element(*self.movies_locators.text_place)
                elif current_check == 2:
                    movie_base_canvas_row.find_element(*self.movies_locators.row_times_sessions)

                random_num //= 3
                if random_num == 0:
                    break
                self.movie_page.act.swipe(80, 40, 20, 40)

    def test_003(self, driver):
        """Открыть экран выбора места"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.shedule_page = SeatSelectionPage(driver)
            self.shedule_page.set_custom_wait(20)
            self.shedule_page.find_element(*self.seat_selection_locators.img_screen)

    @pytest.mark.xfail(reason='dont know')
    def test_004(self, driver):
        pass

    def test_005_check_hiding_logo_and_header_after_swipe_down(self, driver):
        """Проверяем, что event tabs пропадает при свайпе вниз"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(2)
            self.movie_page.act.swipe(50, 80, 50, 20)
            sleep(1)
            self.movie_page.not_displayed(*self.movies_locators.img_banner)

    def test_006_top_movies_are_visible(self, driver):
        """Топ фильмы отображаются на главном экране"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.find_element(*self.movies_locators.img_row_top)

    def test_007_flop_into_top_movie(self, driver):
        """Открытия фильма из раздела top"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.click_random_top_movie(3)
        with allure.step('MoviesDetailsPage'):
            self.event_detail_page = MoviesDetailsPage(driver)
            self.event_detail_page.set_custom_wait(20)
            self.event_detail_page.find_element(*self.movies_details_locators.text_event_name)

    def test_008_test_hiding_and_showing_headers_after_swipes(self, driver):
        """Event navigation бар пропадает при swipe вниз и появляется при swipe вверх"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(3)
            self.movie_page.act.swipe(50, 80, 50, 20)
            self.movie_page.not_displayed(*self.movies_locators.img_banner)
            self.movie_page.act.swipe(50, 20, 50, 80)
            sleep(2)
            self.movie_page.find_element(*self.movies_locators.img_banner)

    def test_009_popular_movies_are_visible(self, driver):
        """Популярные фильмы видны на экране при запуске"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(2)
            self.movie_page.act.swipe(50, 70, 50, 30)
            sleep(1)
            self.movie_page.find_element(*self.movies_locators.text_row_popular_title)
            self.movie_page.find_element(*self.movies_locators.text_row_popular_all)
            self.movie_page.find_element(*self.movies_locators.img_row_popular)

    def test_0010_premiers_are_available(self, driver):
        """Премьеры присутствуют на экране"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(2)
            self.movie_page.act.swipe(50, 70, 50, 30)
            self.movie_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movie_page.find_element(*self.movies_locators.text_row_premiers_title)
            self.movie_page.find_element(*self.movies_locators.text_row_premiers_name)
            self.movie_page.find_element(*self.movies_locators.img_row_premiers)

    def test_0011_flop_into_popular_movie(self, driver):
        """Проваливаемся в карусель популярные фильмы по клику"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(2)
            self.movie_page.act.swipe(50, 70, 50, 30)
            sleep(1)
            self.movie_page.click(*self.movies_locators.text_row_popular_all)
        with allure.step('ShedulePage'):
            self.sheduler_page = ShedulePage(driver)
            self.sheduler_page.set_custom_wait(20)
            self.sheduler_page.find_element(*self.shedule_locators.img_screen)

    def test_0012_close_schedule_is_working(self, driver):
        """Event details показывается после закрытия расписания кнопкой назад"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.select_session()
        with allure.step('InfoPage'):
            self.info_page = InfoPage(driver)
            self.info_page.set_custom_wait(20)
            self.info_page.pass_without_info()
        with allure.step('SeatSelectionPage'):
            self.seat_selection_page = SeatSelectionPage(driver)
            self.seat_selection_page.set_custom_wait(20)
            self.seat_selection_page.click(*self.seat_selection_locators.btn_back)
            self.movie_page.find_element(*self.movies_locators.text_movie_title)

    def test_0013_flop_into_popular_from_name(self, driver):
        """Проваливаемся в карусель популярные фильмы по клику на названия блока"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(2)
            self.movie_page.act.swipe(50, 80, 50, 20)
            sleep(1)
            self.movie_page.click(*self.movies_locators.text_row_popular)
        with allure.step('MoviesDetailsPage'):
            self.detail_page = MoviesDetailsPage(driver)
            self.detail_page.set_custom_wait(20)
            self.detail_page.find_element(*self.movies_details_locators.text_event_name)

    def test_0014_flop_into_popular_from_in_arrow(self, driver):
        """Проваливаемся в карусель популярные фильмы по клику на стрелку блока"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(2)
            self.movie_page.act.swipe(50, 80, 50, 20)
            sleep(1)
            self.movie_page.click(*self.movies_locators.img_row_popular)
        with allure.step('MoviesDetailsPage'):
            self.detail_page = MoviesDetailsPage(driver)
            self.detail_page.set_custom_wait(20)
            self.detail_page.find_element(*self.movies_details_locators.text_event_name)

    def test_0015_flop_into_details_from_popular_carusel(self, driver):
        """Проваливаемся в event details из карусели популярных фильмов"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(5)
            self.movie_page.act.swipe(50, 80, 50, 20)
            sleep(2)
            self.movie_page.act.swipe(50, 80, 50, 20)
            sleep(1)
            self.movie_page.click(*self.movies_locators.img_row_popular)
        with allure.step('MoviesDetailsPage'):
            self.detail_page = MoviesDetailsPage(driver)
            self.detail_page.set_custom_wait(20)
            self.detail_page.find_element(*self.movies_details_locators.text_time)

    def test_0016_open_premiers_vertical_carousel(self, driver):
        """Проваливаемся в премьеры - горизонтальную карусель"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(5)
            self.movie_page.act.swipe(50, 80, 50, 20)
            self.movie_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movie_page.click(*self.movies_locators.text_row_premiers_all)
        with allure.step('ShedulePage'):
            self.sheduler_page = ShedulePage(driver)
            self.sheduler_page.set_custom_wait(20)
            self.sheduler_page.find_element(*self.shedule_locators.img_screen)

    def test_0017_flop_into_event_details_from_premier_carousel(self, driver):
        """Проваливаемся в эвент детейлз из горизонтальной карусели премьер"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(5)
            self.movie_page.act.swipe(50, 70, 50, 30)
            self.movie_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movie_page.click(*self.movies_locators.img_row_premiers)
        with allure.step('MoviesDetailsPage'):
            self.detail_page = MoviesDetailsPage(driver)
            self.detail_page.set_custom_wait(20)
            self.detail_page.find_element(*self.movies_details_locators.text_event_name)

    # @pytest.mark.skip('No button fast buy')
    def test_0018_open_schedule_btn_fast_buy(self, driver):
        """ Открываем расписание из горизонтальной карусели премьер через кнопку быстрой оплаты"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(5)
            self.movie_page.act.swipe(50, 80, 50, 20)
            self.movie_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movie_page.click(*self.movies_locators.text_row_premiers_all)
        with allure.step('ShedulePage'):
            self.schedule_page = ShedulePage(driver)
            self.schedule_page.set_custom_wait(20)
            self.schedule_page.click(*self.shedule_locators.btn_fastbuy_ticket)
            self.schedule_page.find_element(*self.shedule_locators.col_session_table)

    def test_0019_close_schedule_from_vertical_carousel(self, driver):
        """Закрываем расписание из карусели премьер и попадаем на эвент детейлз"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(5)
            self.movie_page.act.swipe(50, 80, 50, 20)
            self.movie_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movie_page.click(*self.movies_locators.text_row_premiers_all)
        with allure.step('ShedulePage'):
            self.schedule_page = ShedulePage(driver)
            self.schedule_page.set_custom_wait(20)
            self.schedule_page.click(*self.shedule_locators.btn_fastbuy_ticket)
            self.schedule_page.click(*self.shedule_locators.btn_back_bar)
            self.schedule_page.find_element(*self.movies_details_locators.btn_back)

    def test_0020_exit_from_premier_carousel(self, driver):
        """Выходим кнопкой назад из карусели премьер и попадаем на фичер"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            sleep(5)
            self.movie_page.act.swipe(50, 80, 50, 20)
            self.movie_page.act.swipe(50, 60, 50, 40)
            sleep(1)
            self.movie_page.click(*self.movies_locators.text_row_premiers_all)
        with allure.step('ShedulePage'):
            self.schedule_page = ShedulePage(driver)
            self.schedule_page.set_custom_wait(20)
            self.schedule_page.click(*self.shedule_locators.btn_back)
            self.movie_page.find_element(*self.movies_locators.img_row_top)
