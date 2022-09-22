# -*- coding: utf-8 -*-
'''
@Time :  10:24
@Author : maodongdong
@File : project_path.py
'''
import os

project_path = os.path.split(os.path.realpath(__file__))[0]

#测试用例的路径
test_case_path = os.path.join(project_path,'TestDatas','Login','testcase.xlsx')
#测试报告的路径
test_report_path = os.path.join(project_path,'Outputs','Reports','HttpRunner_Html')

case_config_path = os.path.join(project_path,'Common','case_config')

print(case_config_path)