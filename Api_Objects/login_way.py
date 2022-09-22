# -*- coding: utf-8 -*-
'''
@Time :  15:46
@Author : maodongdong
@File : login_way.py
'''
from Common.api_base import HttpRequest
from Common.config import Host
from Common.api_url import Url

'''
   登录
'''
class LoginPage:

    '''
    短信验证
    '''
    def sms(self,method,inData):
        sms_url = f'{Host}{Url.hnfh_sms}'
        res = HttpRequest().http_request(sms_url,inData,method)
        return res


    '''
    登录
    '''
    def login(self,method,inData):
        login_url = f'{Host}{Url.login}'
        res = HttpRequest().http_request2(login_url, inData,method)
        return res
