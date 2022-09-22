# -*- coding: utf-8 -*-
'''
@Time :  15:17
@Author : maodongdong
@File : api_base.py
'''
import logging

import requests

from log import Log

my_log = Log()
class HttpRequest:
    def http_request(self,url,data,method,cookies,headers=None):
        if method == "get":
            try:
                res = requests.get(url,json=data,verify = False)
            except:
                # my_log.info("get请求失败!!!")
                my_log.my_log("get请求失败!!!",'INFO')
                raise
        elif method == "post":
            try:
                res = requests.post(url,json=data,cookies=cookies,headers=headers,verify = False)
            except:
                logging.info("post请求失败！！！")
                raise
        elif method.lower() == "delete":
            res = requests.delete(url,data,verify = False)
        elif method.lower() == "put":
            res = requests.put(url,data,verify = False)
        else:
            raise Exception("不支持的请求方式")
        return res
