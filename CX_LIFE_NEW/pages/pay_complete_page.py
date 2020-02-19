#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: pay_complete_page.py
@time: 2020/02/18
"""
from common.base_action import BaseAction

"""
支付完成page
"""


class PayCompletePage(BaseAction):
    loc_pay_success = ("xpath", "//*[@text='支付成功']")
    loc_pay_fail = ("xpath", "//*[@text='支付失败']")
    loc_return_home = ("xpath", "//*[@text='返回首页']")
    loc_return_order = ("xpath", "//*[@text='查看订单']")

    def click_pay_success(self):
        self.click(self.loc_pay_success)

    def click_pay_fail(self):
        self.click(self.loc_pay_fail)

    def click_return_home(self):
        self.click(self.loc_return_home)

    def click_return_order(self):
        self.click(self.loc_return_order)

    def assert_pay_success(self):
        try:
            self.find_element(self.loc_pay_success)
        except:
            print("支付完成页面元素定位成功")
            return False
        else:
            print("支付完成页面元素定位成功")
            return True

    def assert_pay_fail(self):
        try:
            self.find_element(self.loc_pay_fail)
        except:
            print("支付完成页面元素定位成功")
            return False
        else:
            print("支付完成页面元素定位成功")
            return True

