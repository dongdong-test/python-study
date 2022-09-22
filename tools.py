# -*- coding: utf-8 -*-
'''
@Time :  17:03
@Author : maodongdong
@File : tools.py
'''
import datetime
import random
import re
import time

class tools:
    def __init__(self,driver):
        self.driver = driver

    '''
    根据当前时间获取时间戳
    '''
    #字符类型的时间
    def date_operation_1(self,time):
        # 字符类型的时间
        # time = '2013-10-10 23:40:00'
        # 转为时间数组
        timeArray = time.strptime(time, "%Y-%m-%d %H:%M:%S")
        # timeArray可以调用tm_year等

        # 转为时间戳
        timeStamp = int(time.mktime(timeArray))

    #获取当前时间按照指定格式显示，其中：time_style有2中一种是time，一种是date_time;style分为两种，一种是原始数据style1，一种是处理的数据style2
    def date_operation_2(self,time_style,style):
        # time获取当前时间戳
        if time_style == "time":
            now = int(time.time())
            timeArray = time.localtime(now)
            if style == "style1":
                return timeArray
            elif style == "style2":
                otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                return otherStyleTime
            else:
                print('请输入正确的style参数')
        elif time_style == 'date_time':
            now = datetime.datetime.now()
            if style == "style1":
                return now
            elif style == "style2":
                otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
                return otherStyleTime
            else:
                print("请输入正确的style参数")
        else:
            print("请输入正确的time_style参数")


    #生成手机号
    def create_phone(self):
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]

        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]

        # 最后八位数字
        suffix = random.randint(9999999, 100000000)

        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)

    #正则验证手机号
    def verify_phone(self,phone):
        reg = re.compile("(13\d|14[579]|15[^4\D]|17[^49\D]|18\d)\d{8}")
        if reg.match(phone):
            print('Verify passed!')
        else:
            print("Verify failed!")






