# -*- coding: utf-8 -*-
'''
@Time :  11:32
@Author : maodongdong
@File : pub_home_elements.py
'''
from selenium.webdriver.common.by import By

B_planfrom = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[1]/div[1]/img')
A_planfrom = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[1]/div[2]/img')
logistics = (By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[1]/div[3]/img')
business_management = (By.XPATH,"//p[@class = 'word']//span[@class='blue pointer']")#企业管理
drop_down = (By.XPATH,"//div[@class = 'el-dropdown']//span[@class='el-dropdown-link el-dropdown-selfdefine  ']")#下拉框
bell = (By.XPATH,"//img[@src = 'static/images/infoLogo.png']") #小铃铛
logo = (By.XPATH,"//img[@class = 'left pointer']")