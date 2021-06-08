from selenium.common.exceptions import NoSuchElementException

from locators.places_locators import PlacesPageLocators
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class PlacesPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.places_locators = PlacesPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_state_tabs(self):
        tabs = self.driver.find_elements(*self.places_locators.tab)
        for tab in tabs:
            if tab.text == 'Кино':
                assert tab.is_selected(), f'invalid state: {tab}'
            else:
                assert not tab.is_selected(), f'invalid state: {tab}'

    def allow_geolocation(self):
        last_wait = self.get_last_wait()
        self.set_custom_wait(20)
        try:
            self.find_element(*self.places_locators.btn_cancel_location)
            self.click(*self.places_locators.btn_allow_location)
            self.not_displayed(*self.places_locators.btn_allow_location)
        except NoSuchElementException:
            pass
        self.set_custom_wait(last_wait)