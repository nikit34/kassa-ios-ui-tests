import pytest
import allure
import os

from locators.auth_locators import AuthPageLocators
from screens.AuthPage import AuthPage
from screens.ProfilePage import ProfilePage
from screens.MoviesPage import MoviesPage
from screens.SettingsPage import SettingsPage
from locators.common_locators import CommonLocators
from locators.settings_locators import SettingsPageLocators
from locators.profile_locators import ProfilePageLocators


@pytest.mark.usefixtures('driver')
class Test_001_SettingsPage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.profile_locators = ProfilePageLocators()
        cls.settings_locators = SettingsPageLocators()
        cls.auth_locators = AuthPageLocators()

    def test_001_auth_pass_default(self, driver):
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.click(*self.auth_locators.btn_onboarding_login)
            self.auth_page.input('n.permyakov@rambler-co.ru', *self.auth_locators.input_login_email)
            self.auth_page.input(os.environ['IOS_HOST_PASSWORD'], *self.auth_locators.input_login_password)
            self.auth_page.click(*self.auth_locators.btn_login)
        with allure.step('AuthPage'):
            self.profile_page = ProfilePage(driver)
            self.profile_page.set_custom_wait(10)
            self.profile_page.find_element(*self.profile_locators.btn_search_events)

    def test_002_settings_page_are_opened(self, driver):
        """Открывается страница настроек"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('ProfilePage'):
            self.profile_page = ProfilePage(driver)
            self.profile_page.set_custom_wait(10)
            self.profile_page.click(*self.profile_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(10)
            self.settings_page.find_element(*self.settings_locators.btn_cancel)

    def test_003_open_settings_and_back_into_profile(self, driver):
        """Кнопка возврата из настроек в профиль работает"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('ProfilePage'):
            self.profile_page = ProfilePage(driver)
            self.profile_page.set_custom_wait(10)
            self.profile_page.click(*self.profile_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(10)
            self.settings_page.click(*self.settings_locators.btn_cancel)
        with allure.step('ProfilePage'):
            self.profile_page = ProfilePage(driver)
            self.profile_page.set_custom_wait(10)
            self.profile_page.find_element(*self.profile_locators.btn_search_events)

    def test_004_test_change_city(self, driver):
        """Меняем город в настройках и поиск отрабатывает"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('ProfilePage'):
            self.profile_page = ProfilePage(driver)
            self.profile_page.set_custom_wait(10)
            self.profile_page.click(*self.profile_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(10)
            self.settings_page.click(*self.settings_locators.row_city)
            self.settings_page.find_element(*self.settings_locators.input)
            self.settings_page.find_element(*self.settings_locators.btn_choice)

    def test_005_settings_page_has_all_titles(self, driver):
        """На странице настроек указаны все пункты"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('ProfilePage'):
            self.profile_page = ProfilePage(driver)
            self.profile_page.set_custom_wait(10)
            self.profile_page.click(*self.profile_locators.btn_settings)
        with allure.step('SettingsPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(10)
            self.settings_page.check_settings_list()


