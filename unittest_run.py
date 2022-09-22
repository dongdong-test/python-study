# -*- coding: utf-8 -*-
'''
@Time :  17:27
@Author : maodongdong
@File : unittest_run.py
'''

import unittest
from HwTestReport import HTMLTestReport
from Local.HwTestReport_local import  HTMLTestReport
from HwTestReport import HTMLTestReportEN
from Testcase.API.login_two import TestLogin
from Testcase.API.sms import TestSms
from Testcase.API.v3_token import TestV3

suite = unittest.TestSuite()
loader = unittest.TestLoader()
# suite.addTest(TestLogin('test_login'))
suite.addTest(loader.loadTestsFromTestCase(TestLogin))
suite.addTest(loader.loadTestsFromTestCase(TestV3))
suite.addTest(loader.loadTestsFromTestCase(TestSms))



with open(r"D:\test_automation\test_automation\Outputs\Reports\HttpRunner_Html\HttpRunner_Html.html",'wb') as file:
    runner = HTMLTestReport(stream=file,
                                verbosity=2,
                                images=True,
                                title='植得星投',
                                description='植得app测试用例报告',
                                tester='毛冬冬')
    runner.run(suite)