# -*- coding: utf-8 -*-
'''
@Time :  10:12
@Author : maodongdong
@File : login_way.py
'''
import time
from Common.basepage import BasePage
from Page_Elements.Login import loginpage_elements


class Login:
    def __init__(self, driver):
        self.driver = driver

    # 登录全流程
    def test_login_way(self, username, password):
        BasePage(self.driver).send_ele_keys(loginpage_elements.login_username,username,"登录-用户名")
        BasePage(self.driver).send_ele_keys(loginpage_elements.login_password,password,"登录-密码")
        BasePage(self.driver).click_element(loginpage_elements.login_getSms_button,"获取验证码")
        time.sleep(3)
        BasePage(self.driver).send_ele_keys(loginpage_elements.login_sendSms,"233900","输入验证码")
        BasePage(self.driver).click_element(loginpage_elements.login_submit,"点击登录按钮")

    # 登录-校验账号和密码
    def test_login_way_1(self, username, password):
        BasePage(self.driver).send_ele_keys(loginpage_elements.login_username,username,"登录-用户名")
        BasePage(self.driver).send_ele_keys(loginpage_elements.login_password, password, "登录-密码")
        BasePage(self.driver).click_element(loginpage_elements.login_submit,"点击登录按钮")

    # 获取校验提示-登录区域
    def get_check_element_from_login(self):
        BasePage(self.driver).wait_ele_existence(loginpage_elements.login_ddt_error,"报错元素")

