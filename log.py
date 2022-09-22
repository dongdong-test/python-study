# -*- coding: utf-8 -*-
'''
@Time    : 2021/6/13 23:48
@Author  : maodongdong
@File    : log.py
'''
import logging

class Log():
    def my_log(self,msg,level):
    # 定义一个日志收集器
        my_log = logging.getLogger()

        #设定级别
        my_log.setLevel('DEBUG')

        #设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        #创建一个输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)
        fh = logging.FileHandler('文件的的地址')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        #两者对接
        my_log.addHandler(ch)
        my_log.addHandler(fh)

        #收集日志
        if level == 'DEBUG':
            my_log.debug(msg)
        elif level =='INFO':
            my_log.info(msg)
        elif level == 'WARNING':
            my_log.warning(msg)
        elif level == 'ERROR':
            my_log.error(msg)
        else:
            my_log.critical(msg)

        #关闭日志收集器
        my_log.removeFilter(ch)
        my_log.removeFilter(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')



