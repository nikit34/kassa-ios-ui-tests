import random
from time import sleep

from selenium.common.exceptions import NoSuchElementException

from app.get_api import GetAPI
from locators.movies_locators import MoviesPageLocators
from locators.places_locators import PlacesPageLocators
from locators.popup_locators import PopupLocators
from locators.movies_details_locators import MoviesDetailsPageLocators
from templates.action import Action
from templates.base import Wait
from templates.error import base_error
from templates.statistic import RecordTimeout


class MoviesPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.movies_locators = MoviesPageLocators()
        self.movies_details_locators = MoviesDetailsPageLocators()
        self.popup_locators = PopupLocators()
        self.places_locators = PlacesPageLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_popup(self):
        self.find_element(*self.movies_locators.btn_popup_next)
        self.find_element(*self.movies_locators.text_popup_header)

    def click_random_top_movie(self, border=2):
        rand_index = random.randint(0, border)
        locator = self.movies_locators.img_row_top
        left_part_locator, right_part_locator = locator[1].split('0')
        locator_index = left_part_locator + str(rand_index) + right_part_locator
        element = self.find_element(locator[0], locator_index)
        self.click_elem(element)

    def select_session(self, _number_session=0, _number_slide=0):
        for i in range(_number_slide):
            sleep(5)
            self.act.swipe(80, 30, 20, 30)
        locator = self.movies_locators.btn_time_session
        sessions = self.driver.find_elements(*locator)
        self.click_elem(sessions[_number_session])
        if len(sessions) == 0:
            raise base_error(self.driver, ValueError, *locator, crash_site='click_elem', msg='No session buttons found')

    def pass_allow_photo_media(self):
        try:
            self.click(*self.popup_locators.btn_allow)
        except AssertionError:
            pass

    def proccessing_error(self):
        last_wait = self.get_last_wait()
        self.set_custom_wait(10)
        try:
            elem = self.find_element(*self.movies_locators.btn_try_right)
            self.click_elem(elem)
        except NoSuchElementException:
            pass
        self.set_custom_wait(last_wait)

    def allow_geolocation(self):
        last_wait = self.get_last_wait()
        self.set_custom_wait(10)
        try:
            self.find_element(*self.places_locators.btn_cancel_location)
            self.click(*self.places_locators.btn_allow_location)
        except NoSuchElementException:
            pass
        self.set_custom_wait(last_wait)

    def check_state_selected(self, *locator, state=True):
        elem = self.find_element(*locator)
        if state:
            assert elem.is_selected(), f'invalid state: {elem}'
        else:
            assert not elem.is_selected(), f'invalid state: {elem}'

    def get_json_covid_notification(self, city='Абдулино', _number_slide=0, _number_place=0, _number_session=0):
        sleep(self.get_last_wait() / 2)  # МАИ любит костыли
        for i in range(_number_slide):
            sleep(2)
            self.act.swipe(80, 30, 20, 30)
        self.act.click_by_coords(50, 30)
        name_movie = self.find_element(*self.movies_details_locators.text_event_name).text
        id_city = GetAPI.get_id_city(city)
        session_id = GetAPI.get_session_id_movies_featured(name_movie, id_city, _number_place, _number_session)
        response = GetAPI.get_json_hall(session_id)
        try:
            self.click(*self.movies_details_locators.btn_back)
            return response['covidNotification']
        except KeyError:
            _number_slide += 1
            self.click(*self.movies_details_locators.btn_back)
            return self.get_json_covid_notification(city=city, _number_slide=_number_slide, _number_place=_number_place, _number_session=_number_session)


