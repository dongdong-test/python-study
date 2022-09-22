# -*- coding: utf-8 -*-
'''
@Time :  15:48
@Author : maodongdong
@File : v3_token.py
'''

import unittest

import run
from Api_Objects import login_way
from Common.ExcelDate import Handle_Excel
from Common.api_base import HttpRequest
from Common.common_data import method_post
from Common.config import Host
from Common.api_url import Url
from Common.getData import GetData


class TestV3(unittest.TestCase):
    def setUp(self, res=None):
        #平台登陆
        login_url = f'{Host}{Url.login}'
        date = {"userName":"zhangxiaoyu001","pwd":"zhangxiaoyu001","smsCode":"233900","subsystems":["hnfh-backend","hnfh-sc","hnfh-fin"],"smsToken":"p:com.evisible.sms:captcha:ca6b8027-3e66-4fbd-8e7f-94dcecc0ebb6"}
        res = HttpRequest().http_request(login_url,date,method_post,getattr(GetData,'Cookie')).json()
        token = res['data']['token']
        self.headers = {"Authorization":token}

    def test_v3(self):
        api_name='进入富宝通转换token'
        case_date =  r'D:\test_automation\test_automation\TestDatas\Login\testcase.xlsx'
        test_data = Handle_Excel().get_excel_data(case_date)
        run.run(test_data, case_date,self.headers)

    def tearDown(self):
        pass