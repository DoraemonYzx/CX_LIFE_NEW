#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: confirm_order_page.py
@time: 2020/02/16
"""
from common.base_action import BaseAction

"""
确认订单page
"""


class ConfirmOrderPage(BaseAction):
    loc_address = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                            "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/"
                            "android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/"
                            "android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]")
    loc_pay = ("xpath", r"//*[@text='微信支付 ']")
    loc_return_home = ("xpath", r"//*[@text='返回首页']")
    loc_return_order = ("xpath", r"//*[@text='查看订单']")

    def click_address(self):
        self.click(self.loc_address)

    def click_pay(self):
        self.click(self.loc_pay)

    def click_return_home(self):
        self.click(self.loc_return_home)

    def click_return_order(self):
        self.click(self.loc_return_order)

    def assert_pay(self):
        try:
            self.find_element(self.loc_pay)
        except:
            return False
        else:
            return True
