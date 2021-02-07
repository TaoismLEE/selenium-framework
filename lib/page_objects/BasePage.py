# -*- coding:utf-8 -*-
import os
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from lib.common.log import logger


class BasePage(object):
    """
    Base page class, all other page class inherit from this class
    Mainly maintain basic and shared functions each page may perform
    """

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def wait(wait_time):
        sleep(wait_time)

    def on_page(self, url):
        return self.driver.current_url == url

    def move_back(self):
        self.driver.back()
        self.wait(1)

    def move_forward(self):
        self.driver.forward()
        self.wait(1)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *loc):
        try:
            return WebDriverWait(self.driver, 10, 1).until(ec.presence_of_element_located(loc))
        except TimeoutException or NoSuchElementException:
            logger.error("The element:{} has not been shown in current page!".format(str(loc)))
            return False

    def find_elements(self, *loc):
        try:
            return WebDriverWait(self.driver, 10, 1).until(ec.presence_of_all_elements_located(loc))
        except TimeoutException or NoSuchElementException:
            logger.error("The elements:{} have not been shown in current page!".format(str(loc)))
            return False

    def get_current_window_handle(self):
        return self.driver.current_window_handle

    def get_window_handles(self):
        return self.driver.window_handles

    def close_current_window(self):
        self.driver.close()
        sleep(1)

    def switch_to_window(self, new_handle):
        self.driver.switch_to_window(new_handle)

    def execute_js(self, js):
        self.driver.execute_script(js)

    def send_keys(self, value, clear_first=True, click_first=True, *loc):
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except Exception as e:
            logger.error("Element with locator: %s has not been found!" % str(loc))
            logger.error(e)

    def find_element_which_displayed(self, *loc):
        try:
            return WebDriverWait(self.driver, 10, 1).until(ec.presence_of_element_located(loc))
        except TimeoutException or NoSuchElementException:
            logger.error("The element: {} has not shown in current page!".format(str(loc)))
            return False

    def find_element_which_displayed_without_error_log(self, *loc):
        try:
            return WebDriverWait(self.driver, 10, 1).until(ec.presence_of_element_located(loc))
        except TimeoutException or NoSuchElementException:
            return False

    def find_element_which_clickable(self, *loc):
        try:
            return WebDriverWait(self.driver, 10, 1).until(ec.element_to_be_clickable(loc))
        except TimeoutException or NoSuchElementException:
            logger.error("The element: {} has not shown in current page or clickable!".format(str(loc)))
            return False

    # function to capture snapshot and save to report folder
    def capture_snapshot(self, file_name):
        try:
            base_dir = os.getcwd()
            file_path = base_dir + "/report/" + file_name
            file_path = os.path.abspath(file_path)
            self.driver.get_screenshot_as_file(file_path)
        except Exception as err:
            logger.error(err)
            logger.error("Failed to save snapshot: %s" % file_name)
