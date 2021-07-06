from selenium.common.exceptions import StaleElementReferenceException

from locators.settings_locators import SettingsPageLocators
from templates.action import Action
from templates.base import Wait
from templates.error import base_error
from templates.statistic import RecordTimeout


class SettingsPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.settings_locators = SettingsPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_settings_list(self):
        self.find_element(*self.settings_locators.row_card)
        self.find_element(*self.settings_locators.row_bonus_card)
        self.find_element(*self.settings_locators.row_support)
        self.find_element(*self.settings_locators.row_faq)
        self.find_element(*self.settings_locators.row_geolocation)
        self.find_element(*self.settings_locators.row_city)
        self.find_element(*self.settings_locators.row_notifications)
        self.find_element(*self.settings_locators.row_themes)
        self.find_element(*self.settings_locators.row_about_app)

    def check_state_switcher(self, *locator, state=True):
        switcher = None
        try:
            switcher = self.find_element(*locator)
        except StaleElementReferenceException:
            pass
        try:
            if state:
                assert switcher.text == '1', f'invalid state {switcher.text} != 1 on {switcher}'
            else:
                assert switcher.text == '0', f'invalid state {switcher.text} != 0  on {switcher}'
        except AssertionError as error:
            base_error(self.driver, *locator, crash_site='check_state_switcher', msg=f'invalid state {switcher.text} != 1 on {switcher}')
            raise error