# -*- coding: utf-8 -*-
'''
@Time :  13:37
@Author : maodongdong
@File : loginpage_elements.py
'''
from selenium.webdriver.common.by import By

login_username = (By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/form/div[1]/div/div[1]/input')
login_password = (By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/form/div[2]/div/div[1]/input')
login_getSms_button =(By.XPATH,'//span[text()="获取验证码" and @class = "smsCodeTip" ]')
login_sendSms = (By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/form/div[3]/div/div/input')
login_submit = (By.XPATH,'//*[@id="app"]/div[2]/div[1]/div/div[2]/form/div[4]/div/button')

login_error_1 = (By.XPATH,'//div[@class = "el-message el-message--error"]//p[text()="用户名密码不匹配"]')
login_error_2 = (By.XPATH,'//div[@class = "el-form-item__error"]')
login_error_3 = (By.XPATH,'//div[@class = "el-message el-message--error"]//p[text()="请按提示填写相关内容"]')

login_ddt_error = (By.XPATH,'//div[@class ="el-form-item__error"]')