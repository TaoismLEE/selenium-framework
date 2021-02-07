# -*- coding:utf-8 -*-

import random
from time import sleep
from selenium.webdriver.common.by import By
from lib.page_objects.BasePage import BasePage


class HomePage(BasePage):
    """
    Home page of project, each page can be maintain as a class inheriting from BasePage
    Locators: maintain elements locators of current page
    Functions: maintain functions can perform on current page
    """

    # Locators
    loc_search_input = (By.XPATH, "//input[@id='kw']")
    loc_submit_search = (By.XPATH, "//input[@id='su']")

    # Functions
    def search_input(self, data):
        self.find_element(*self.loc_search_input).clear()
        self.find_element(*self.loc_search_input).send_keys(data)

    # trigger search
    def submit_search(self):
        self.find_element(*self.loc_submit_search).click()

    # # Page navigation
    # def switch_to_police_rule_detail_page(self, current_handle):
    #     all_handles = self.get_window_handles()
    #     for handle in all_handles:
    #         if handle != current_handle:
    #             self.switch_to_window(handle)
    #     page_object = PoliceRuleDetailPage(self.driver)
    #     return page_object
    #
    # # switch to article list page from home page
    # def switch_to_article_list_page(self, current_handle):
    #     all_handles = self.get_window_handles()
    #     for handle in all_handles:
    #         if handle != current_handle:
    #             self.switch_to_window(handle)
    #     page_object = ArticleListPage(self.driver)
    #     return page_object
