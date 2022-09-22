# -*- coding: utf-8 -*-
'''
@Time :  14:14
@Author : maodongdong
@File : service_fulfillment_page.py
'''
from Common.basepage import BasePage
from Page_Elements.ServiceFulfillment.BaseInfo import baseinfo_elements


class Service_Page:

    def __init__(self, driver):
        self.driver = driver

    #不输入参数直接点击提交
    def submit_service(self):
        #操作
        BasePage(self.driver).click_element(baseinfo_elements.element_submit,"基础信息-提交")


    #校验企业注册日期
    def check_enterpriseRegistDate(self,enterpriseRegistDate):
        BasePage(self.driver).send_ele_keys(baseinfo_elements.element_1,enterpriseRegistDate,"输入企业注册日期")

        BasePage(self.driver).wait_ele_existence(baseinfo_elements.error_code_1,30,"校验企业注册日期")

        BasePage(self.driver).click_element(baseinfo_elements.login_username,"基础信息-提交")


