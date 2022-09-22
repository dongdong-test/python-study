# -*- coding: utf-8 -*-
'''
@Time :  10:22
@Author : maodongdong
@File : sms.py
'''
import os
import unittest
import pytest
import run
from Common import common_data
from Api_Objects.login_way import *
from Common.ExcelDate import Handle_Excel

#
# class TestSms:
#     @pytest.mark.parametrize('resWay,inBody,expData',Handle_Excel().get_excel_data('短信验证','SMS')) #数据驱动
#     def test_sms(self,resWay,inBody,expData):
#         #调用短信验证的接口代码
#         res = LoginPage().sms(resWay,inBody).json()
#         assert res['message'] == expData['message']
#         Handle_Excel().do_excel_writeback("短信验证",)
#         if (res['status'] == 200 ):
#             common_data.smstoken = common_data.smstoken + res['data']['uid']
#             print(common_data.smstoken)
#         else:
#             print('接口调用失败，失败原因：{}'.format(res['message']))
from project_path import test_case_path


class TestSms(unittest.TestCase):
    def setUp(self):
        pass
    def test_sms(self):
        test_data = Handle_Excel().get_excel_data(test_case_path)
        run.run(test_data, test_case_path)
    def tearDown(self):
        pass
