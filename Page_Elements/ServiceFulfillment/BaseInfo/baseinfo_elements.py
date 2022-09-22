# -*- coding: utf-8 -*-
'''
@Time :  11:28
@Author : maodongdong
@File : baseinfo_elements.py
'''
from selenium.webdriver.common.by import By

element_1 = (By.ID,"enterpriseBasicInfo.enterpriseRegistDate") #企业注册日期
element_2 = (By.ID,'//p[text() = "企业地区码"]/parent::label/parent::div//input[@class = "el-input__inner"]')  #企业地区码
element_3 = (By.ID,'enterpriseBasicInfo.enterpriseMobile')
element_4 = (By.ID,'enterpriseBasicInfo.enterpriseClassification')
element_4_1 = (By.XPATH,"//span[text() = '其他机构']")
element_4_2 = (By.XPATH,"//span[text() = '法定代表人企业']")

element_5 = (By.ID,'enterpriseBasicInfo.enterpriseCategory')
element_5_1 = (By.XPATH,"//span[text() = '国有企业']")
element_5_2 = (By.XPATH,"//span[text() = '集体企业']")

element_6 = (By.ID,'enterpriseBasicInfo.enterpriseStopSign')
element_6_1 = (By.XPATH,"//span[text() = '关停']")
element_6_2 = (By.XPATH,"//span[text() = '未关停']")

element_7 = (By.ID,'enterpriseBasicInfo.labourIntensiveSign')
element_7_1 = (By.XPATH,"/html/body/div[8]/div[1]/div[1]/ul/li[1]")
element_7_2 = (By.XPATH,"/html/body/div[8]/div[1]/div[1]/ul/li[2]")

element_8 = (By.ID,'enterpriseBasicInfo.ruralCitySign')
element_8_1 = (By.XPATH,"//span[text() = '农村']")
element_8_2 = (By.XPATH,"//span[text() = '城市']")

element_9 = (By.ID,'enterpriseBasicInfo.domesticOverseasSign')
element_9_1 = (By.XPATH,"//span[text() = '境内']")
element_9_2 = (By.XPATH,"//span[text() = '境外']")

element_10 = (By.ID,'enterpriseBasicInfo.groupCustomersSign')
element_10_1 = (By.XPATH,"/html/body/div[11]/div[1]/div[1]/ul/li[1]")
element_10_2 = (By.XPATH,"/html/body/div[11]/div[1]/div[1]/ul/li[2]")



element_11 = [By.ID,'enterpriseBasicInfo.parentCompany']

element_12 = [By.ID,'enterpriseBasicInfo.shareholdingRatio']

element_13 = [By.XPATH,"//input[@id = 'enterpriseBasicInfo.shareholdingRatio']/ancestor::div[@class ='el-form-item outsideForm']/following::div[@class = 'el-input el-input--suffix is-focus']//input"] #行业分类

element_14 = [By.ID,'enterpriseBasicInfo.businessScope']

element_15 = [By.ID,'enterpriseBasicInfo.paidInCapital']

element_16 = [By.ID,'enterpriseBasicInfo.employeeNumber']
element_17 = [By.ID,'enterpriseBasicInfo.sellSum']
element_18 = [By.ID,'enterpriseBasicInfo.totalAssets']
element_19 = [By.ID,'enterpriseBasicInfo.listedCompanySign']
element_19_1 = [By.XPATH,'/html/body/div[12]/div[1]/div[1]/ul/li[1]']
element_19_2 = [By.XPATH,'/html/body/div[12]/div[1]/div[1]/ul/li[2]']

element_20 = [By.ID,'enterpriseBasicInfo.listedPlace']

element_21 = [By.ID,'enterpriseBasicInfo.listedCompanyStockCode']

element_22 = [By.ID,'enterpriseBasicInfo.listedCountry']
element_22_1 = [By.XPATH,"//li[@class = 'el-select-dropdown__item hover']//span[text() = '中国']"]

element_23 = [By.ID,'enterpriseBasicInfo.businessStatus']
element_23_1 = [By.XPATH,"//span[text()='正常运营']"]
element_23_2 = [By.XPATH,"//span[text()='筹建']"]

element_24 = [By.ID,'enterpriseBasicInfo.economicComponents']
element_24_1 = [By.XPATH,"//span[text()='国有绝对控股']"]
element_24_2 = [By.XPATH,"//span[text()='国有控股']"]

element_25 = [By.ID,'enterpriseBasicInfo.nationalEconomicSector']
element_24_1 = [By.XPATH,"//span[text()='机关团体']"]
element_24_2 = [By.XPATH,"//span[text()='部队']"]

#法人信息
element_26 = [By.ID,'corporationBasicInfo.corporationIdStartDate']#法定代表人证件签发日期
element_27 = [By.ID,'corporationBasicInfo.corporationIdEndDate'] #法定代表人证件到期日期
element_28 = [By.ID,'corporationBasicInfo.corporationSex']#法定代表人性别
element_28_1 =[By.XPATH,'/html/body/div[17]/div[1]/div[1]/ul/li[1]']
element_28_2 =[By.XPATH,'/html/body/div[17]/div[1]/div[1]/ul/li[2]']
element_29 = [By.ID,'corporationBasicInfo.corporationMobile']#法定代表人手机号

#授权经办人信息
element_30 = [By.ID,'authLoanExtInfo.contactsName']#姓名
element_31 = [By.ID,'authLoanExtInfo.contactTelephone']#联系电话
element_32 = [By.ID,'authLoanExtInfo.serviceAddress']#办公地址
element_33 = [By.ID,'authLoanExtInfo.postalCode']#邮编
#实际控制人信息
element_34 = [By.ID,'authLoanExtInfo.postalCode']#实际控制人证件签发日期
element_35 = [By.ID,'authLoanExtInfo.postalCode']#实际控制人证件到期日期
element_36 = [By.ID,'authLoanExtInfo.postalCode']#实际控制人手机号




element_submit = [By.XPATH,"//span[text()='提交']"]
error_code_1 = [By.XPATH,"//p[ @class = 'el-message__content']"] #弹窗错误

error_element_bottom = [By.XPATH,"//div[@class = 'el-form-item__error']"]