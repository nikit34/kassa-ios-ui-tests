import os
import pytest
import allure

from locators.profile_locators import ProfilePageLocators
from screens.MoviesPage import MoviesPage
from screens.AuthPage import AuthPage
from locators.common_locators import CommonLocators
from locators.auth_locators import AuthPageLocators
from locators.movies_locators import MoviesPageLocators
from screens.OnboardingPage import OnboardingPage


@allure.feature('noCache')
@pytest.mark.usefixtures('driver_noCache')
class Test_001_AuthPage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.auth_locators = AuthPageLocators()
        cls.movies_locators = MoviesPageLocators()

    def test_001_auth_page_is_opened(self, driver):
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.skip_onboarding()
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.movies_locators.btn_popup_next)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.click(*self.auth_locators.btn_popup_next)
            self.auth_page.find_element(*self.auth_locators.btn_settings)
            self.auth_page.find_element(*self.auth_locators.btn_onboarding_login)
            # self.auth_page.find_element(*self.auth_locators.btn_onboarding_sberid)


@allure.feature('auth_page')
@pytest.mark.usefixtures('driver')
class Test_002_AuthPage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.auth_locators = AuthPageLocators()
        cls.profile_locators = ProfilePageLocators()

    def test_002_auth_page_is_opened(self, driver):
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.click(*self.auth_locators.btn_onboarding_login)
            self.auth_page.find_element(*self.auth_locators.btn_login)
            self.auth_page.find_element(*self.auth_locators.btn_auth_apple)
            self.auth_page.find_element(*self.auth_locators.btn_vk)
            self.auth_page.find_element(*self.auth_locators.btn_fb)
            self.auth_page.find_element(*self.auth_locators.btn_lj)
            self.auth_page.find_element(*self.auth_locators.btn_ok)
            self.auth_page.find_element(*self.auth_locators.btn_more)
            self.auth_page.find_element(*self.auth_locators.btn_cancel)

    def test_003_auth_pass_invalid(self, driver):
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.click(*self.auth_locators.btn_onboarding_login)
            self.auth_page.input('autotest-negative@rambler.ru', *self.auth_locators.input_login_email)
            self.auth_page.input('Negative', *self.auth_locators.input_login_password)
            self.auth_page.click(*self.auth_locators.btn_login)
            self.auth_page.pass_verification()

    def test_004_auth_pass_vk(self, driver):
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.click(*self.auth_locators.btn_onboarding_login)
            self.auth_page.click(*self.auth_locators.btn_vk)
            self.auth_page.find_element(*self.auth_locators.input_vk_login)
            self.auth_page.find_element(*self.auth_locators.input_vk_password)
            self.auth_page.find_element(*self.auth_locators.btn_vk_login)
