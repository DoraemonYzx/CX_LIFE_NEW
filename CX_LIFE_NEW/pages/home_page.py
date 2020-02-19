#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: home_page.py
@time: 2020/02/14
"""
from common.base_action import BaseAction


class HomePage(BaseAction):
    loc_commodity_one = ("xpath", r"//*[@text='wx0f98b556b1c08f70:pages/index/index.html:VISIBLE']/android.widget.Image[6]")
    loc_commodity_two = ("xpath", r"//*[@text='wx0f98b556b1c08f70:pages/index/index.html:VISIBLE']/android.widget.Image[7]")
    loc_commodity_three = ("xpath", r"//*[@text='wx0f98b556b1c08f70:pages/index/index.html:VISIBLE']/android.widget.Image[8]")
    loc_framelayoutw = ("id", "com.tencent.mm:id/w")
    loc_plus_coupon = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                                "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                                "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[64]/"
                                "android.view.View/android.view.View/android.view.View[2]")

    loc_myst_buy_one = ("xpath", r"//*[@text='wx0f98b556b1c08f70:pages/index/index.html:VISIBLE']/android.view.View[11]")

    def click_commodity_one(self):
        self.click(self.loc_commodity_one)

    def click_commodity_two(self):
        self.click(self.loc_commodity_two)

    def click_commodity_three(self):
        self.click(self.loc_commodity_three)

    def assert_find_framelayoutw(self):
        try:
            self.find_element(self.loc_framelayoutw)
        except:
            return False
        else:
            return True

    def assert_click_plus_coupon(self):
        try:
            self.find_element(self.loc_plus_coupon)
        except:
            print("没有出现")
            self.click(self.loc_plus_coupon)
        else:
            self.click(self.loc_plus_coupon)

    def click_plus_coupon(self):
        self.click(self.loc_plus_coupon)


    def assert_find_must_buy_one(self):
        try:
            self.find_element(self.loc_myst_buy_one)
        except:
            return False
        else:
            return True
