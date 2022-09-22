# -*- coding: utf-8 -*-
'''
@Time :  16:38
@Author : maodongdong
@File : create_report.py
'''
import HTMLTestRunner
import time
import unittest


test_dir = '../Testcase'

def case():
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py',top_level_dir=None)
    return discover
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M",time.localtime())
    report_path = '../Reports/' + now + "result.html"
    file_path = open(report_path,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file_path,title='测试报告',description='华南富汇测试报告')

    runner.run(case())
    file_path.close()