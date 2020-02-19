#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: base_driver.py
@time: 2020/02/14
"""

from appium import webdriver


def base_driver():
    desired_caps = dict()
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'xiaomi-redmi_note_5-d0946ac8'
    # desired_caps['platformVersion'] = '5.1.1'
    # desired_caps['deviceName'] = '127.0.0.1:21503'
    # desired_caps['app'] = r'C:\Users\Admin\Downloads\changxiaojiankangv3.2.6_downcc.com.apk'
    desired_caps['appPackage'] = 'com.tencent.mm'
    desired_caps['appActivity'] = 'com.tencent.mm.ui.LauncherUI'
    desired_caps['noReset'] = 'true'
    desired_caps['automationName'] = 'UiAutomator2'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver
