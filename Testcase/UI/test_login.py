# -*- coding: utf-8 -*-
'''
@Time :  11:08
@Author : maodongdong
@File : test_login.py
'''
import os
import time
import ddt as ddt
import pytest
from Common.basepage import BasePage
from Page_Elements.Home import pub_home_elements
from Page_Elements.Login import loginpage_elements
from TestDatas.Login import login_datas as Login_Data
from TestDatas import Common_Datas
from browser_operation import browser_operation
from PageObjects.login import Login


@ddt.ddt()
class TestLogin:

    @classmethod
    def setUp(self):
        print("=======所有用例执行之前都会执行一次=========")
        self.driver = browser_operation('chrome')
        self.driver.get(Common_Datas.login_url)
        self.driver.maximize_window()

    #用户名和密码的验证
    @classmethod
    @pytest.mark.smoke   #可以打多个标签
    def test_login(self):
        # 步骤
        Login(self.driver).test_login_way(Login_Data.success_data["username"], Login_Data.success_data["password"])
        # 断言
        self.assertTrue(BasePage(self.driver).wait_ele_Visible(pub_home_elements.bell,10,0.6,"登录验证小铃铛"),"校验失败")

    # 账号错误----使用ddt
    @ddt.data(*Login_Data.username_data)
    def test_login_username(self, value):
        # 步骤
        Login(self.driver).test_login_way_1(value["username"], value["password"])
        # 断言
        time.sleep(3)
        self.assertEqual(BasePage(self.driver).get_ele_text(loginpage_elements.login_ddt_error), value["check"])#需要断言的元素是同一个，可以是文字不同。

    # 用户名未填写

    # 密码未填写

    # 验证码未填写

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        pytest.main(['test_login.py','-s','--alluredir','../reports/tmp'])

        os.system('allure server -p ../reports/tmp')

