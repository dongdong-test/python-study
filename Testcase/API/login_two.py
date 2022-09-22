# -*- coding: utf-8 -*-
'''
@Time :  17:19
@Author : maodongdong
@File : login_two.py
'''
import unittest
import run
from Common.ExcelDate import Handle_Excel
from project_path import test_case_path


class TestLogin(unittest.TestCase):
    def setup(self):
        pass

    def test_login(self):
        test_data = Handle_Excel().get_excel_data(test_case_path)
        run.run(test_data, test_case_path)

    def tearDown(self):
        pass