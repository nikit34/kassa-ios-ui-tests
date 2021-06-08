from time import sleep

from locators.onboarding_locators import OnboardingPageLocators
from locators.popup_locators import PopupLocators
from utils.factory_screenshots import Screenshot
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


def _generate_selections_accessibility(func):
    def wrapper(self, *args, **kwargs):
        for i, result in enumerate(kwargs['part_locators']):
            kwargs['part_locators'][i] = (OnboardingPageLocators.ACCESSIBILITY_ID, result)
        return func(self, *args, **kwargs)

    return wrapper


class OnboardingPage(RecordTimeout, Wait):
    def __init__(self, driver, city='Абдулино'):
        super().__init__(driver)

        self.repeat = '0'
        self.extra_interval = 50
        self.city = city

        self.act = Action(driver)

        self.onboarding_page_locators = OnboardingPageLocators()
        self.popup_locators = PopupLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def skip_onboarding(self):
        self.click(*self.onboarding_page_locators.btn_drive)
        self.click(*self.onboarding_page_locators.btn_choice_city)
        sleep(2)
        self.click_define_city(part_locators=[self.city])
        self.click(*self.onboarding_page_locators.btn_choice)
        self.click(*self.onboarding_page_locators.btn_pass)

    @_generate_selections_accessibility
    def check_city_search(self, input_city, part_locators=None):
        if not isinstance(part_locators, list):
            raise TypeError("part_locators must be type list")
        self.input(input_city, *self.onboarding_page_locators.input_field)
        for result_city in part_locators:
            city = self.find_element(*result_city)
            assert city.text == result_city[1], f'{city.text} is not relevant result of search'

    @_generate_selections_accessibility
    def click_define_city(self, part_locators=None):
        last_timeout = self.get_last_wait()
        self.set_custom_wait(40)
        if not isinstance(part_locators, list):
            raise TypeError("part_locators must be type list")
        for city in part_locators:
            self.input(city[1], *self.onboarding_page_locators.input_field)
            self.click(*city)
        self.set_custom_wait(last_timeout)

    def check_state_list_enabled(self):
        btn_choice = self.find_element(*self.onboarding_page_locators.btn_choice)
        assert btn_choice.is_enabled(), f'[find_element] {btn_choice} is not enabled'

    def check_state_list_disabled(self):
        btn_choice = self.find_element(*self.onboarding_page_locators.btn_choice)
        assert not btn_choice.is_enabled(), f'[find_element] {btn_choice} is not disabled'

    def check_play_video(self):
        first_screenshots = Screenshot(self.driver)
        first_pix = Screenshot.convert_img_pixels(first_screenshots.path)
        # del first_screenshots.file
        second_screenshots = Screenshot(self.driver)
        second_pix = Screenshot.convert_img_pixels(second_screenshots.path)
        # del second_screenshots.file
        assert Screenshot.compare_images(first_pix, second_pix) is False, 'Images are same'

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value
