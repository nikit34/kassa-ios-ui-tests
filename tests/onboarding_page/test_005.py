import pytest
import allure

from screens.OnboardingPage import OnboardingPage
from locators.onboarding_locators import OnboardingPageLocators



@allure.feature('noCache')
@pytest.mark.usefixtures('driver_noCache')
class Test_001_OnboardingPage:
    @classmethod
    def setup_class(cls):
        cls.onboarding_locators = OnboardingPageLocators()

    def test_003_button_back_from_cities_is_working(self, driver):
        """Сдвиг назад работает на экране выбора города"""
        with allure.step('OnboardingPage'):
            self.onboarding_page = OnboardingPage(driver)
            self.onboarding_page.set_custom_wait(10)
            self.onboarding_page.click(*self.onboarding_locators.btn_drive)
            self.onboarding_page.click(*self.onboarding_locators.btn_choice_city)
            self.onboarding_page.find_element(*self.onboarding_locators.input_field)
            self.onboarding_page.act.swipe(50, 20, 50, 80)
            self.onboarding_page.find_element(*self.onboarding_locators.btn_choice_city)
            self.onboarding_page.find_element(*self.onboarding_locators.btn_allow_location)