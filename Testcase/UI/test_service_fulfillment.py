# -*- coding: utf-8 -*-
'''
@Time :  10:48
@Author : maodongdong
@File : test_service_fulfillment.py
'''
import time
import ddt as ddt
import pytest
from TestDatas.Login import login_datas as Login_Data
from TestDatas import Common_Datas
from TestDatas.service_fulfillment_datas import service_fulfillment as Service_Data
from PageObjects.home import Home
from PageObjects.login import Login
from PageObjects.service_fulfillment_page import Service_Page as Service
from tools import tools
from selenium import webdriver

@ddt.ddt()
class Login_case():

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(r"D:\dirver\chromedriver_win32\chromedriver.exe")
        self.driver.get(Common_Datas.login_url)
        self.driver.maximize_window()
        #登录
        Login(self.driver).test_login_way(Login_Data.services_data["username"], Login_Data.services_data["password"])
        time.sleep(3)
        #进入B模式
        Home(self.driver).into_planfromB()
        #tools 的实例
        self.exist = tools(self.driver)

    '''
    校验所有数据没有填写直接提交
    '''
    @ddt.data(*Service_Data.error_data_no_parameter)
    def test_service_no_parameter(self,data):
        #步骤
        Service(self.driver).submit_service()
        #断言
        self.assertEqual(Service(self.driver).get_errorMessage_from_service(),data["check"])

    '''
    校验企业注册日期
    '''
    @ddt.data(*Service_Data.error_data_code_for_enterpriseRegistDate)
    def test_check_enterpriseRegistDate(self,data):
        #步骤
        Service(self.driver).check_enterpriseRegistDate(data['enterpriseRegistDate'])
        #断言
        # self.assertEqual(self.exist.element_isExist(ui_elements.),data['check'])

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        pytest.main(['test_service_fulfillment','-s'])