import pytest
import allure

from locators.movies_locators import MoviesPageLocators
from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators
from locators.popup_locators import PopupLocators
from locators.settings_locators import SettingsPageLocators
from screens.AuthPage import AuthPage
from locators.auth_locators import AuthPageLocators
from screens.MoviesPage import MoviesPage
from locators.common_locators import CommonLocators
from screens.SettingsPage import SettingsPage
from testrail_logging import Testrail


@allure.testcase('http://testrail.rambler-co.ru/index.php?/cases/view/712851', 'testrail points: from 1 to 7')
@allure.feature('noCache')
@pytest.mark.usefixtures('driver_noCache')
class Test_001_OnboardingPage:
    @classmethod
    def setup_class(cls):
        cls.onboarding_page_locators = OnboardingPageLocators()
        cls.popup_locators = PopupLocators()
        cls.movies_locators = MoviesPageLocators()

    def test_001_onboarding_is_opened(self, driver):
        """Установить и запустить приложение"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.find_element(*self.onboarding_page_locators.text_title)
            self.onboarding_page.check_play_video()

    def test_002_drive(self, driver):
        """тапнуть на Поехали"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_page_locators.btn_drive)
            self.onboarding_page.find_element(*self.onboarding_page_locators.btn_choice_city)
            self.onboarding_page.find_element(*self.onboarding_page_locators.text_location)

    def test_003_allow_location(self, driver):
        """тапнуть на Разрешить"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_page_locators.btn_drive)
            self.onboarding_page.click(*self.onboarding_page_locators.btn_allow_location)
            self.onboarding_page.find_element(*self.popup_locators.text_allow_location)
            self.onboarding_page.find_element(*self.popup_locators.btn_allow_while_using_app)
            self.onboarding_page.find_element(*self.popup_locators.btn_dont_allow)

    def test_004_allow_once(self, driver):
        """тапнуть на При использовании"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_page_locators.btn_drive)
            self.onboarding_page.click(*self.onboarding_page_locators.btn_allow_location)
            self.onboarding_page.click(*self.popup_locators.btn_allow_once)
            self.onboarding_page.find_element(*self.onboarding_page_locators.btn_pass)

    def test_005_turn_on_notification(self, driver):
        """тапнуть на Включить уведомления"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_page_locators.btn_drive)
            self.onboarding_page.click(*self.onboarding_page_locators.btn_allow_location)
            self.onboarding_page.click(*self.popup_locators.btn_allow_once)
            self.onboarding_page.click(*self.onboarding_page_locators.btn_enable_notification)
            self.onboarding_page.find_element(*self.popup_locators.btn_dont_allow)
            self.onboarding_page.click(*self.popup_locators.btn_allow)

    def test_006_allow(self, driver):
        """тапнуть на Разрешить"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.skip_onboarding()
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.check_popup()

    def test_007_knowlenge(self, driver):
        """тапнуть на Понятно"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver, city='Абдулино')
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.skip_onboarding()
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.movies_locators.btn_popup_next)
            self.movie_page.not_displayed(*self.movies_locators.btn_popup_next)


@allure.testcase('http://testrail.rambler-co.ru/index.php?/cases/view/712851', 'testrail points: from 8 to 13')
@pytest.mark.usefixtures('driver')
class Test_002_MoviesPage:
    @classmethod
    def setup_class(cls):
        cls.auth_locators = AuthPageLocators()
        cls.settings_locators = SettingsPageLocators()
        cls.common_locators = CommonLocators()

    def test_008_profile_popup(self, driver):
        """тапнуть в нижнем навбаре на кнопку Профиль"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.check_popup()

    def test_009_profile(self, driver):
        """тапнуть на Понятно"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.click(*self.auth_locators.btn_popup_next)
            self.auth_page.not_displayed(*self.auth_locators.btn_popup_next)

    def test_010_settings(self, driver):
        """тапнуть на иконку шестеренки в правом верхнем углу"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('AuthPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(10)
            self.settings_page.check_settings_list()

    def test_011_geolocation(self, driver):
        """найти раздел Геолокация"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('AuthPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(10)
            self.settings_page.check_state_switcher(*self.settings_locators.btn_geolocation, state=False)

    @pytest.mark.xfail(reason='bug Simulator -> check real device')
    def test_012_notifications(self, driver):
        """найти раздел Уведомления"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_profile)
        with allure.step('AuthPage'):
            self.auth_page = AuthPage(driver)
            self.auth_page.set_custom_wait(10)
            self.auth_page.click(*self.auth_locators.btn_settings)
        with allure.step('AuthPage'):
            self.settings_page = SettingsPage(driver)
            self.settings_page.set_custom_wait(10)
            self.settings_page.check_state_switcher(*self.settings_locators.btn_notifications, state=False)

    @pytest.mark.xfail(condition=lambda: True, reason='need real devices')
    def test_013_push(self, driver):
        """свернуть приложение, отправить через сервис Пушвуш уведомление на телефон"""
        pass


@pytest.fixture(autouse=True, scope='module')
def module_setup_teardown():
    Testrail.logging_case('C712851')
    yield
    Testrail.logging_result()