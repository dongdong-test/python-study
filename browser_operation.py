# -*- coding: utf-8 -*-
'''
@Time :  11:00
@Author : maodongdong
@File : browser_operation.py
'''
from selenium import webdriver


def browser_operation(driver_type):
    '''
    :param driver_type: 浏览器名称，现在只支持  chrome/filefox/ie 三种
    :return:
    '''
    if driver_type == 'chrome':
        driver = webdriver.Chrome(r"D:\dirver\chromedriver_win32\chromedriver.exe")
        return driver
    elif driver_type == 'filefox':
        driver = webdriver.firefox(r"D:\dirver\geckodriver-v0.29.1-win64\geckodriver.exe")
        return driver
    elif driver_type == 'edge':
        driver = webdriver.ie(r"D:\dirver\edgedriver_win64\msedgedriver.exe")
        return driver
    elif driver_type == "safari":
        driver = webdriver.safari(r"")
    else:
        print('我们暂时还不支持该浏览器的ui自动化')