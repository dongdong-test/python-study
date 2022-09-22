# -*- coding: utf-8 -*-
'''
@Time :  15:57
@Author : maodongdong
@File : class_pandas.py
'''


import pandas as pd

df = pd.read_excel(r'D:\test_automation\test_automation\TestDatas\Login\testcase.xlsx',sheet_name='短信验证')
print(df.index)