# -*- coding: utf-8 -*-
'''
@Time :  15:45
@Author : maodongdong
@File : home_elements.py
'''
from Page_Elements.Home import pub_home_elements


class Home:
    def __init__(self,driver):
        self.driver = driver

    def into_planfromA(self):
        self.driver.find_element(pub_home_elements.A_planfrom).click()

    def into_planfromB(self):
        self.driver.find_element(pub_home_elements.B_planfrom).click()
