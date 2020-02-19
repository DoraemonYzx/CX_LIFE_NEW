#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: commodity_details_page.py
@time: 2020/02/14
"""
from common.base_action import BaseAction


class CommodityDetailsPage(BaseAction):
    loc_buy = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                    "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[3]/"
                    "android.widget.LinearLayout/android.widget.RelativeLayout[4]")
    loc_add_to_cart = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/"
                                "android.widget.RelativeLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout[3]")
    loc_cart = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                         "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/"
                         "android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout[2]")
    loc_home = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                         "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/"
                         "android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout[1]")

    def click_buy(self):
        self.click(self.loc_buy)

    def click_add_to_cart(self):
        self.click(self.loc_add_to_cart)

    def click_cart(self):
        self.click(self.loc_cart)

    def click_home(self):
        self.click(self.loc_home)

    def assert_buy(self):
        try:
            self.find_element(self.loc_buy)
        except:
            return False
        else:
            return True



