from selenium.common.exceptions import NoSuchElementException

from locators.info_locators import InfoPageLocators
from templates.base import Wait
from templates.statistic import RecordTimeout


class InfoPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.info_locators = InfoPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def pass_without_info(self):
        try:
            self.click(*self.info_locators.btn_switch_allow)
            self.click(*self.info_locators.btn_covid_next_old)
        except NoSuchElementException:
            try:
                self.click(*self.info_locators.btn_covid_next)
            except NoSuchElementException:
                pass
            pass
