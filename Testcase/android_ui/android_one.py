# -*- coding: utf-8 -*-
'''
@Time    : 2022/5/8 22:15
@Author  : maodongdong
@File    : android_one.py
'''

# 导包
from appium import webdriver
import time

# 设置desired_capablities 字典
desired_caps = {}
# 指定移动平台操作系统
desired_caps["platformName"] = "Android"
# 指定操作系统版本
desired_caps["platformVersion"] = "7.1.2"
# 指定设备 可通过adb device查看
desired_caps["deviceName"] = "127.0.0.1:62001"
# 指定需要测试的app的程序包名
desired_caps["appPackage"] = "com.kmxs.reader"
# 指定启动页面的名字
desired_caps["appActivity"] ="com.km.app.home.view.LoadingActivity"
# 指定每次运存测试前重新安装测试的app
desired_caps['noReset'] = True
'''
查看app启动页Activity
1. 使用adb shell 命令进入Android端shell命令界面
2. 执行命令 : dumpsys package 包名
    在前几行找到带有Activity的一串即为启动页面
'''

# 启动app
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_caps)

# 设置缺省等待时间
driver.implicitly_wait(5)

# 操作元素 (自动完成2+5的操作)
# driver.find_element_by_id("com.miui.calculator:id/btn_2_s").click()  # 点击事件
# driver.find_element_by_id("com.miui.calculator:id/btn_plus_s").click()  # 点击事件
# driver.find_element_by_id("com.miui.calculator:id/btn_5_s").click()  # 点击事件
#
# # driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="等于"]').click()  # 点击事件
# # 回车代替等号
# driver.press_keycode(66)
time.sleep(5)
# 退出app
driver.quit()
