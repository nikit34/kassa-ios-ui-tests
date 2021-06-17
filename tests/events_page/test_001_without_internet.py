import os
from time import sleep

import pytest
import allure

from screens.MoviesPage import MoviesPage
from screens.TicketsDetailsPage import TicketsDetailsPage
from screens.TicketsPage import TicketsPage
from locators.tickets_locators import TicketsPageLocators
from locators.tickets_details_locators import TicketsDetailsPageLocators
from locators.common_locators import CommonLocators


@pytest.mark.skip(reason="need ticket")
@allure.testcase('http://testrail.rambler-co.ru/index.php?/cases/view/712855', 'testrail points: all')
@pytest.mark.usefixtures('driver')
class Test_001_EventsPage:
    @classmethod
    def setup_class(cls):
        cls.common_locators = CommonLocators()
        cls.tickets_locators = TicketsPageLocators()
        cls.tickets_details_locators = TicketsDetailsPageLocators()

    @classmethod
    def teardown_class(cls):
        os.system(f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup -setnetworkserviceenabled Wi-Fi on')

    @pytest.mark.skip(reason="need single user for macos account")
    def test_001_without_internet_events(self, driver):
        """тапнуть на кнопку События в нижнем навбаре"""
        with allure.step('MoviesPage'):
            os.system(f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup -setnetworkserviceenabled Wi-Fi off')
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_search)
            self.movie_page.find_element(*self.events_locators.text_error)
            self.movie_page.find_element(*self.events_locators.btn_try_yet)

    @pytest.mark.skip(reason="need single user for macos account")
    def test_002_update_with_internet(self, driver):
        """включить доступ к сети и тапнуть на Попробовать еще"""
        with allure.step('MoviesPage'):
            os.system(f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup -setnetworkserviceenabled Wi-Fi on')
            sleep(5)
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_search)
            sleep(10)
            self.movie_page.click(*self.events_locators.btn_try_yet)
            sleep(20)
            self.movie_page.find_element(*self.events_locators.btn_card_price)
            self.movie_page.find_element(*self.events_locators.btn_card_release_date)
            self.movie_page.find_element(*self.events_locators.btn_first_up_input_field)
            self.movie_page.find_element(*self.events_locators.btn_first_under_input_field)

    def test_003_common_ticket(self, driver):
        """тапнуть на кнопку Билеты в нижнем навбаре"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_ticket)
        with allure.step('TicketsPage'):
            self.tickets_page = TicketsPage(driver)
            self.tickets_page.set_custom_wait(10)
            self.tickets_page.find_element(*self.tickets_locators.text_title_ticket)
            self.tickets_page.find_element(*self.tickets_locators.text_time_ticket)
            self.tickets_page.find_element(*self.tickets_locators.text_status_ticket)
            self.tickets_page.find_element(*self.tickets_locators.btn_download_ticket)

    def test_004_card_ticket(self, driver):
        """тапнуть на билет"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_ticket)
        with allure.step('TicketsPage'):
            self.tickets_page = TicketsPage(driver)
            self.tickets_page.set_custom_wait(10)
            self.tickets_page.click(*self.tickets_locators.img_ticket)
        with allure.step('TicketsDetailsPage'):
            self.tickets_details_page = TicketsDetailsPage(driver)
            self.tickets_details_page.set_custom_wait(10)
            self.tickets_details_page.find_element(*self.tickets_details_locators.info_table)
            self.tickets_details_page.find_element(*self.tickets_details_locators.live_table)

    def test_005_close(self, driver):
        """напнуть на крестик"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_ticket)
        with allure.step('TicketsPage'):
            self.tickets_page = TicketsPage(driver)
            self.tickets_page.set_custom_wait(10)
            self.tickets_page.click(*self.tickets_locators.img_ticket)
        with allure.step('TicketsDetailsPage'):
            self.tickets_details_page = TicketsDetailsPage(driver)
            self.tickets_details_page.set_custom_wait(10)
            self.tickets_details_page.click(*self.tickets_details_locators.btn_close)
        with allure.step('TicketsPage'):
            self.tickets_page.find_element(*self.tickets_locators.img_ticket)

    @pytest.mark.skip(reason="need single user for macos account")
    def test_006_turn_off_internet_tiket(self, driver):
        """отключить доступ к сети, тапнуть еще раз на билет"""
        with allure.step('MoviesPage'):
            self.movie_page = MoviesPage(driver)
            self.movie_page.set_custom_wait(10)
            self.movie_page.click(*self.common_locators.tab_ticket)
        with allure.step('TicketsPage'):
            self.tickets_page = TicketsPage(driver)
            self.tickets_page.set_custom_wait(10)
            os.system(f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup -setnetworkserviceenabled Wi-Fi off')
            self.tickets_page.click(*self.tickets_locators.img_ticket)
        with allure.step('TicketsDetailsPage'):
            self.tickets_details_page = TicketsDetailsPage(driver)
            self.tickets_details_page.set_custom_wait(10)
            self.tickets_details_page.find_element(*self.tickets_details_locators.info_table)
            self.tickets_details_page.find_element(*self.tickets_details_locators.live_table)
            os.system(f'echo "{os.environ["IOS_HOST_PASSWORD"]}" | sudo -S networksetup -setnetworkserviceenabled Wi-Fi on')


    #