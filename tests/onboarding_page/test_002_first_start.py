import pytest
import allure

from locators.movies_locators import MoviesPageLocators
from screens.MoviesPage import MoviesPage
from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators



@allure.testcase('http://testrail.rambler-co.ru/index.php?/cases/view/712849', 'testrail points: from 5 to 8')
@allure.feature('noCache')
@pytest.mark.usefixtures('driver_noCache')
class Test_001_OnboardingPage:
    @classmethod
    def setup_class(cls):
        cls.onboarding_locators = OnboardingPageLocators()
        cls.movies_locators = MoviesPageLocators()

    def test_001_start(self, driver):
        """тапнуть на иконку приложения"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.find_element(*self.onboarding_locators.text_title)
            self.onboarding_page.find_element(*self.onboarding_locators.btn_drive)

    def test_002_drive(self, driver):
        """тапнуть на Поехали"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_locators.btn_drive)
            self.onboarding_page.find_element(*self.onboarding_locators.btn_allow_location)
            self.onboarding_page.find_element(*self.onboarding_locators.btn_choice_city)
            self.onboarding_page.find_element(*self.onboarding_locators.text_location)

    def test_003_choice_city(self, driver):
        """тапнуть на Выбрать город"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_locators.btn_drive)
            self.onboarding_page.click(*self.onboarding_locators.btn_choice_city)
            self.onboarding_page.find_element(*self.onboarding_locators.input_field)
            self.onboarding_page.find_element(*self.onboarding_locators.title_choice_city)
            self.onboarding_page.find_element(*self.onboarding_locators.btn_choice)
            self.onboarding_page.find_element(*self.onboarding_locators.list_cities)

    def test_004_scrolling_cities(self, driver):
        """проскроллить список вниз-вверх, выбрать любой город из списка"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_locators.btn_drive)
            self.onboarding_page.click(*self.onboarding_locators.btn_choice_city)
            self.onboarding_page.act.swipe(50, 80, 50, 20)
            self.onboarding_page.act.swipe(50, 80, 50, 20)
            self.onboarding_page.act.swipe(50, 20, 50, 80)
            self.onboarding_page.check_state_list_disabled()
            self.onboarding_page.act.click_by_coords(50, 50)
            self.onboarding_page.check_state_list_enabled()

    def test_005_input_city(self, driver):
        """в поле поиска ввести Новос"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_locators.btn_drive)
            self.onboarding_page.click(*self.onboarding_locators.btn_choice_city)
            self.onboarding_page.check_city_search('Новос', part_locators=['Новосергиевка', 'Новосибирск'])

    def test_006_define_city(self, driver):
        """тапнуть на Новосибирск, затем на Выбрать"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_locators.btn_drive)
            self.onboarding_page.click(*self.onboarding_locators.btn_choice_city)
            self.onboarding_page.click_define_city(part_locators=['Абдулино'])
            self.onboarding_page.click(*self.onboarding_locators.btn_choice)
            self.onboarding_page.find_element(*self.onboarding_locators.btn_pass)
            self.onboarding_page.find_element(*self.onboarding_locators.btn_enable_notification)
            self.onboarding_page.find_element(*self.onboarding_locators.text_enable_notification)

    def test_007_pass(self, driver):
        """тапнуть на Пропустить"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.skip_onboarding()
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.check_popup()

    def test_008_knowlenge(self, driver):
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.skip_onboarding()
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.movies_locators.btn_popup_next)
            self.movie_page.not_displayed(*self.movies_locators.btn_popup_next)
