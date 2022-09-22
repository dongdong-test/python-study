# -*- coding: utf-8 -*-
'''
@Time :  13:42
@Author : maodongdong
@File : Popup.py
'''

#业务开通弹窗
from selenium.webdriver.common.by import By

basic_info = (By.XPATH,"//label[text()='基础信息']")   #基础信息
online_sign = (By.XPATH,"//span[text() = '在线签署']") #在线签署
cance = (By.XPATH,"//span[text() = '取消']")#取消按钮
P_Reapply = (By.XPATH,"//p[text() = '平台审核未通过']/parent::div//span[text()='重新申请']")#平台审核未通过 ---重新申请
Y_Reapply = (By.XPATH,"//p[text() = '银行授信审核未通过']/parent::div//span[text()='重新申请") #银行授信审核未通过 ---重新申请
