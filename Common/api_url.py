# -*- coding: utf-8 -*-
'''
@Time :  15:42
@Author : maodongdong
@File : api_url.py
'''
class Url:
    #注册
    register = 'api/auth/api/v1.0/user/register'

    #短信验证
    hnfh_sms = 'api/auth/api/v1.0/user/send-captcha-sms'

    #登录
    login = 'api/auth/api/v1.0/token/new'

    #认证中心短信验证
    rz_sms = 'image/imgcheck/v1.0/validate'

    #认证中心登录认证
    rz_login = 'auth/api/v1.0/token/new'

    #V3a接口转换token
    v3 = 'api/auth/api/v1.0/token/refresh/v3'

    #个人认证
    rz_personal = 'auth/api/v1.0/real-name-authentication'

    #个人实名认证通过
    rz_personal_pass = 'auth/api/v1.0/real-name-authentication/audit/pass'

    #企业实名认证
    rz_business = 'orguser/org/v1.0/entryRequest'

    #企业实名认证通过
    rz_business_pass = 'orguser/org/v1.0/entryRequest/pass'


