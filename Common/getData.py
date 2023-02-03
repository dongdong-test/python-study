# -*- coding: utf-8 -*-
'''
@Time :  15:49
@Author : maodongdong
@File : getData.py
'''

import pandas as pd
from project_path import test_case_path

class GetData:
    Cookie = None
    NoRegTel = pd.read_excel(test_case_path,sheet_name='init').iloc[0,0]
