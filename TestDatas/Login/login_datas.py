# -*- coding: utf-8 -*-
'''
@Time :  15:02
@Author : maodongdong
@File : login_datas.py
'''

#正常场景
success_data = {'username':"zhangxiaoyu001",'password':'zhangxiaoyu001'}

#异常用例--用户名格式不正确
username_data = [
    {"username":"1111111111111111111111111111111111111111111111111111111111111111111111111111","password":"zhangxiaoyu001","check":"请输入正确的手机号或用户名"},
    {"username":"1","password":"zhangxiaoyu001","check":"请输入正确的手机号或用户名"},
    {"username":"","password":"zhangxiaoyu001","check":"请输入用户名/手机号"}
]

#业务开通的异常用例账号
services_data = {'username':"hnfh_test5_gys_1761",'password':']k4L#~_{gU{:~LuD'}