#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: navigation_bar_page.py
@time: 2020/02/16
"""
from common.base_action import BaseAction


class NavigationBarPage(BaseAction):
    loc_home = ("xpath", r"//*[@resource-id='com.tencent.mm:id/w']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]")
    loc_classification = ("xpath", r"//*[@resource-id='com.tencent.mm:id/w']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]")
    loc_shopping_cart = ("xpath", r"//*[@resource-id='com.tencent.mm:id/w']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[3]")
    loc_my = ("xpath", r"//*[@resource-id='com.tencent.mm:id/w']/android.widget.LinearLayout[1]/android.widget.RelativeLayout[4]")

    def click_home(self):
        self.click(self.loc_home)

    def click_classification(self):
        self.click(self.loc_classification)

    def click_shopping_cart(self):
        self.click(self.loc_shopping_cart)

    def click_my(self):
        self.click(self.loc_my)
