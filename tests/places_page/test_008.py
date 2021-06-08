import pytest
import allure

from locators.places_locators import PlacesPageLocators
from screens.MoviesPage import MoviesPage
from screens.PlacesPage import PlacesPage
from locators.common_locators import CommonLocators



@pytest.mark.usefixtures('driver')
class Test_001_PlacesPage:
    @classmethod
    def setup_class(cls):
        cls.places_locators = PlacesPageLocators()
        cls.common_locators = CommonLocators()

    def test_001_places_screen_is_opened(self, driver):
        """Открыта вкладка Билеты"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.click(*self.common_locators.tab_places)
        with allure.step('PerformancePage'):
            self.places_page = PlacesPage(driver)
            self.places_page.set_custom_wait(20)
            self.places_page.allow_geolocation()
            self.places_page.find_element(*self.places_locators.row_events)

    def test_002_moves_tab_is_selected(self, driver):
        """Таб кино выбран по дефолту"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.click(*self.common_locators.tab_places)
        with allure.step('PlacesPage'):
            self.places_page = PlacesPage(driver)
            self.places_page.set_custom_wait(20)
            self.places_page.check_state_tabs()

    def test_003_screen_contains_all_elements(self, driver):
        """таб МЕСТА подсвечивается выбранным"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.allow_geolocation()
            self.movie_page.click(*self.common_locators.tab_places)
        with allure.step('PlacesPage'):
            self.places_page = PlacesPage(driver)
            self.places_page.set_custom_wait(20)
            self.places_page.find_element(*self.places_locators.block_search)
            self.places_page.find_element(*self.places_locators.btn_map)
            self.places_page.find_element(*self.places_locators.row_labels)

    def test_004_allow_geo_popup(self, driver):
        """в табе МЕСТА имеется попап о геолокации"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.click(*self.common_locators.tab_places)
        with allure.step('PlacesPage'):
            self.places_page = PlacesPage(driver)
            self.places_page.set_custom_wait(20)
            self.places_page.find_element(*self.places_locators.btn_allow_location)
            self.places_page.find_element(*self.places_locators.btn_cancel_location)

    def test_005_close_geo_popup(self, driver):
        """В табе Места закрываем попап о геолокации"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(20)
            self.movie_page.click(*self.common_locators.tab_places)
        with allure.step('PlacesPage'):
            self.places_page = PlacesPage(driver)
            self.places_page.set_custom_wait(20)
            self.places_page.allow_geolocation()
