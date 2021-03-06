from datetime import datetime, timedelta, date, time
from time import sleep
import cv2
import numpy as np
from allure_commons.types import AttachmentType
from skimage import io
import allure

from app.check_api import CheckAPI
from locators.movies_details_locators import MoviesDetailsPageLocators
from locators.popup_locators import PopupLocators
from utils.factory_screenshots import Screenshot
from templates.action import Action
from templates.base import Wait
from templates.statistic import RecordTimeout


class MoviesDetailsPage(RecordTimeout, Wait):
    def __init__(self, driver):
        super().__init__(driver)

        self.act = Action(driver)

        self.repeat = '0'
        self.extra_interval = 50

        self.movies_details_locators = MoviesDetailsPageLocators()
        self.popup_locators = PopupLocators()

    def set_custom_wait(self, wait):
        self.set_wait(self.driver, wait)

    def check_popup(self):
        self.find_element(*self.movies_details_locators.text_popup_header)
        self.find_element(*self.movies_details_locators.btn_popup_next)

    @staticmethod
    def k_means_clustering_average(screenshot):
        img = io.imread(screenshot.path)[:, :, :-1]
        # making three columns: r g b
        pixels = np.float32(img.reshape(-1, 3))
        # will be separate color on 5 clasters
        n_colors = 5
        # tell cv2 terminated after accuracy is reached
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
        # get result worked algorithm
        _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        # take for calc only unique labels
        _, counts = np.unique(labels, return_counts=True)
        # calc average by 5 separated colors of channels
        return palette[np.argmax(counts)]

    def check_img_gallery_orientation(self):
        sleep(5)
        screenshot_before_rotate = Screenshot(self.driver)
        dominant_before_rotate = self.k_means_clustering_average(screenshot_before_rotate)
        self.act.rotate_simulator('right')
        self.act.rotate_simulator('left')
        self.act.rotate_simulator('right')
        sleep(1)
        screenshot_after_rotate = Screenshot(self.driver)
        dominant_after_rotate = self.k_means_clustering_average(screenshot_after_rotate)
        try:
            for i in range(3):
                if abs(dominant_before_rotate[i] - dominant_after_rotate[i]) < min(dominant_before_rotate[i], dominant_after_rotate[i]):
                    assert False, f'Dominant on {i} does not differ x2 times'
            del screenshot_before_rotate.file
            del screenshot_after_rotate.file
        except AssertionError as error:
            allure.attach(self.driver.get_screenshot_as_png(), name='after_rotate', attachment_type=AttachmentType.PNG)
            allure.attach(self.driver.get_screenshot_as_png(), name='before_rotate', attachment_type=AttachmentType.PNG)
            error.args += ('logging_api error', '[FAILED] check image - it hasn\'t been rotated')
            raise ArithmeticError('[FAILED] check image - it hasn\'t been rotated')

    def check_video_opened_full_mode(self):
        sleep(5)
        screenshot = Screenshot(self.driver)
        dominant_video = self.k_means_clustering_average(screenshot)
        try:
            for i in range(3):
                if dominant_video[i] > 1:
                    assert False, f'Dominant on {i} does not less than 1'
            del screenshot.file
        except AssertionError as error:
            allure.attach(self.driver.get_screenshot_as_png(), name='screenshot_video', attachment_type=AttachmentType.PNG)
            error.args += ('logging_api error', '[FAILED] check video - it hasn\'t opened in full screen mode')
            raise ArithmeticError('[FAILED] check video - it hasn\'t opened in full screen mode')

    @staticmethod
    def check_img_view(dbg_api):
        for line in dbg_api.read_buffer(name_file='redis_filter.log'):
            str_datetime = line.split(';', 1)[0]
            logging_time = datetime.strptime(str_datetime, '%H:%M:%S')
            currented_time = datetime.now() - timedelta(seconds=5)
            if currented_time.time() < logging_time.time():
                return True
        return False
