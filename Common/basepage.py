# -*- coding: utf-8 -*-
'''
@Time :  17:27
@Author : maodongdong
@File : basepage.py
'''
import datetime
import logging
import os

import win32con
import win32gui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,driver):
        self.driver = driver
        logging.getLogger().setLevel(logging.INFO)

    #等待元素可见
    def wait_ele_Visible(self,element,time,poll_frequency=0.5,doc="",):
        '''
        :param element: 需要查询的元素
        :param time: 等待的时间
        :param poll_frequency: 查询频率，每隔多久查询一个
        :param doc:模块名称
        :return: True 或者 False
        '''
        logging.info("等待元素 {} 可见".format(element))
        try:
            # 开始时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver,time,poll_frequency).until(EC.visibility_of_element_located(element))
            # 结束时间
            end = datetime.datetime.now()
            #时间差
            logging.info("等待结束，等待时间为{}".format(end-start))
        except:
            logging.exception("等待元素可见失败！！！")
            logging.exception("等待元素可见失败！！！")
            self.save_screenshot(doc)
            raise

    #等待元素存在
    def wait_ele_existence(self,element,time,poll_frequency=0.5,doc="",):
        '''

        :param element: 定位的元素
        :param time: 等待的时间
        :param poll_frequency: 查询频率，每隔多久查询一个
        :param doc: 模块名称
        :return: True 或者 False
        '''
        try:
            #开始时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver,time,poll_frequency).until(EC.presence_of_all_elements_located(*element))
            #结束时间
            end = datetime.datetime.now()
            #时间差
            logging.info("等待结束，等待时间为{}".format(end-start))
        except:
            logging.exception("等待元素不存在!!!")
            self.save_screenshot(doc)
            raise

    #查找元素
    def get_element(self,element,doc="",):
        '''
        :param element: 定位的元素
        :param doc: 所属模块
        :return:
        '''
        # logging.info("开始查找元素{}".format(element))
        try:
            ele = self.driver.find_element(*element)
            return ele
            logging.info("查找元素{}成功".format(element))
        except:
            logging.exception("查询元素{}失败".format(element))
            self.save_screenshot(doc)
            raise

    #点击元素
    def click_element(self,element,doc="",):
        '''
        :param element: 定位的元素
        :param doc: 所属模块
        :return:
        '''
        #查找元素
        ele = self.get_element(element,doc)
        logging.info("开始点击元素{}".format(element))
        try:
            ele.click()
        except:
            logging.exception("元素点击失败！！！")
            self.save_screenshot(doc)
            raise


    #输入操作
    def send_ele_keys(self,element,text,doc="",):
        '''

        :param element: 定位的元素
        :param text: 输入的字段
        :param doc: 所属模块
        :return:
        '''
        #查找元素
        ele = self.get_element(element,doc)
        logging.info("开始输入参数{}".format(text))
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入失败!!!")
            self.save_screenshot(doc)
            raise

    #获取元素文本内容
    def get_ele_text(self,element,doc="",):
        '''
        :param element: 定位的元素
        :param doc: 所属模块
        :return:
        '''
        #查找元素
        ele = self.get_element(element,doc)
        logging.info("开始获取元素{}的文本".format(element))
        try:
            ele.text
            return ele.text
            logging.info("获取元素{}文本成功！".format(element))
        except:
            logging.exception("获取元素文本失败！！！")
            self.save_screenshot(doc)
            raise

    #获取元素的属性

    def get_ele(self,element,doc="",):
        '''
        :param element: 定位的元素
        :param doc: 所属模块
        :return:
        '''
        #查找元素
        ele = self.get_element(element,doc)
        logging.info("开始获取元素{}的属性".format(element))
        try:
            ele.get_attribute()
            return ele.get_attribute()
        except:
            logging.exception("获取元素属性失败！！！")
            self.save_screenshot(doc)
            raise

    #alert处理--.accept():点击alert的确认按钮，dismiss()：点击Alert的【取消】按钮；send_keys(keysToSend)：在Alert的输入框输入信息；text：获取Alert上的文言信息
    def handle_Alert(self,element,doc="",):
        #查找元素
        ele = self.get_element(element,doc)
        logging.info("开始进行alert处理！！！")
        try:
            ele.switch_to_alert()
            return ele.switch_to_alert()
        except:
            logging.exception("alert处理失败！！！")
            self.save_screenshot(doc)
            raise

    #切换frame操作
    def handle_Frame(self,element,index="",doc="",):
        '''
        :param element: 定位的元素
        :param index: frame 的下标，可以不传
        :param doc: 模块名称
        :return:
        '''
        #查找元素
        ele = self.get_element(element,doc)
        logging.info("开始进行frame操作！！！")
        try:
            ele.switch_to.frame(element)
        except:
            logging.exception("frame操作失败！！！")
            self.save_screenshot(doc)
            raise


    #截图
    def save_screenshot(self,name):
        '''
        :param name: 模块名称
        :return:
        '''
        time = str(datetime.date.today())
        basePath = "../Outputs/Image/"
        if os.path.exists(basePath + time):
            #图片名称 = 模块名称，操作名称，时间.png
            fileName = "{0}/{1}.png".format(basePath + time, name)
            logging.info("开始截图!!!")
            self.driver.save_screenshot(fileName)
            logging.info("截取网页页面成功，文件地址为{}".format(fileName))
        else:
            os.mkdir(basePath + time)
            fileName = "{0}/{1}.png".format(basePath + time, name)
            self.driver.save_screenshot(fileName)
            logging.info("截取网页页面成功，文件地址为{}".format(fileName))

    #文件上传
    def fileipload(self, fileAddress):
        '''
        :param fileAddress: 文件地址---现在是本地的地址（绝对路径），后续可以使用当前项目下的相对路径这样就可以脱离绝对路径的文件限制，在项目移植的时候可以将相关测试文件一起打包。
        :return:
        '''
        # 打开窗口
        dialog = win32gui.FindWindow("#32770", r"打开")  # 一级窗口
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", None)  # 三级
        Edit = win32gui.FindWindowEx(ComboBox, 0, "Edit", None)  # 四级---输入框
        open = win32gui.FindWindowEx(dialog, 0, "Button", "打开")  # 打开按钮
        close = win32gui.FindWindowEx(dialog, 0, "Button", "取消")  # 关闭弹窗
        # 输入文件地址，点击打开按钮，提交按钮
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, 0, fileAddress)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, open)  # 点击打开按钮
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, close)  # 点击关闭按钮


def wait_ele_existence():
    return None