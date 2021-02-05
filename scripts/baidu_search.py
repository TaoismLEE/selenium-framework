# -*- coding:utf-8 -*-
import unittest
import os
from lib.common.webdriver import initialize_browser
from lib.common.log import logger
from lib.common.parse_file import ParseYaml
from lib.common.parse_file import ParseCSV
from lib.page_objects.HomePage import HomePage


class BaiduSearch(unittest.TestCase):
    def setUp(self):
        self.driver = initialize_browser()
        # get project url
        try:
            project_data_dict = ParseYaml('project.yml')
            self.URL = project_data_dict.get_yaml_dict()['URL']
        except Exception as e:
            logger.error("Failed to open data file!")
            logger.error(e)

        # preparing test data
        try:
            data_file = os.path.dirname(os.path.dirname(__file__)) + "/data/baidu_search.csv"
            file_path = os.path.abspath(data_file)
            data_obj = ParseCSV(file_path)
            data = data_obj.read_csv()
            self.search_data = data[0][0]
        except Exception as e:
            logger.error("Failed to open data file!")
            logger.error(e)

    def testBaiduSearch(self):
        """
        demo script performing basic search
        """
        home_page = HomePage(self.driver)
        home_page.open(self.URL)
        home_page.search_input(self.search_data)
        home_page.submit_search()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
