# -*- coding: utf-8 -*-
'''
@Time :  10:26
@Author : maodongdong
@File : run.py
'''
from Common.ExcelDate import Handle_Excel
from Common.api_base import HttpRequest
from Common.getData import GetData


def run(test_data,file_name,headers=None):
                for item in test_data:
                        print('正在测试的用用例是：{}'.format(item['case_des']))
                        res = HttpRequest().http_request(item['case_url'], eval(item['case_data']), item['case_way'],getattr(GetData,'Cookie'),headers)
                        if res.cookies:
                                setattr(GetData,'Cookie',res.cookies)
                        try:
                                assert(res.json()["message"] == item['case_expectData'])
                                result = "pass"
                        except AssertionError as e:
                                result = 'faile'
                                raise e
                        finally:
                        # if(res.json()["message"] == item['case_expectData']):
                        #         result = "pass"
                        # else:
                        #         result = 'faile'
                        # assert res["message"] == item['case_expectData']
                                print('请求的结果是{}'.format(res.json()))
                                Handle_Excel().do_excel_writeback(file_name,item['sheet_name'],item['case_id']+1,str(res.json()),result)


