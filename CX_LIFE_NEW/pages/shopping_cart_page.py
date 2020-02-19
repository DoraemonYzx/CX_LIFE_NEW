#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: shopping_cart_page.py
@time: 2020/02/16
"""

from common.base_action import BaseAction

"""
购物车page
"""

class ShoppingCartPage(BaseAction):
    loc_delete_one = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                               "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                               "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                               "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[5]")
    loc_delete_two = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                               "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                               "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                               "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[12]")
    loc_delete_three = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                 "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                                 "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                                 "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[18]")

    loc_subtract_one = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                 "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                                 "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                                 "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Image[1]")
    loc_subtract_two = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                 "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                                 "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                                 "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Image[3]")
    loc_subtract_three = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                   "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                   "android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/"
                                   "android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/"
                                   "android.widget.Image[5]")

    loc_add_one = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                            "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                            "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                            "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Image[2]")
    loc_add_two = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                            "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                            "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                            "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Image[4]")
    loc_add_three = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                              "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                              "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                              "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.widget.Image[6]")

    loc_select_one = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                               "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                               "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                               "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]")
    loc_select_two = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                               "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                               "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                               "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[9]/")
    loc_select_three = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                 "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                                 "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                                 "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[15]/")
    loc_select_all = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                               "android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/"
                               "android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.FrameLayout[1]/"
                               "android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[118]/"
                               "android.view.View[1]/android.widget.Image")

    loc_buy_now = ("xpath", "//*[@text='wx0f98b556b1c08f70:pages/carts/carts.html:VISIBLE']/android.view.View[73]/android.view.View[6]")
    loc_go_shoping = ("xpath", "//*[@text='快去购物']")

    def click_delete_one(self):
        self.click(self.loc_delete_one)

    def click_delete_two(self):
        self.click(self.loc_delete_two)

    def click_delete_three(self):
        self.click(self.loc_delete_three)

    def click_subtract_one(self):
        self.click(self.loc_subtract_one)

    def click_subtract_two(self):
        self.click(self.loc_subtract_two)

    def click_subtract_three(self):
        self.click(self.loc_subtract_three)

    def click_add_one(self):
        self.click(self.loc_add_one)

    def click_add_two(self):
        self.click(self.loc_add_two)

    def click_add_three(self):
        self.click(self.loc_add_three)

    def click_select_one(self):
        self.click(self.loc_select_one)

    def click_select_two(self):
        self.click(self.loc_select_two)

    def click_select_three(self):
        self.click(self.loc_select_three)

    def click_select_all(self):
        self.click(self.loc_select_all)

    def click_buy_now(self):
        self.click(self.loc_buy_now)

    def assert_buy_now(self):
        try:
            self.find_element(self.loc_buy_now)
        except:
            print("购物车页面元素定位失败")
            return False
        else:
            print("购物车页面元素定位成功")
            return True

    def assert_go_shoping(self):
        try:
            self.find_element(self.loc_go_shoping)
        except:
            print("购物车页面元素定位失败")
            return False
        else:
            print("购物车页面元素定位成功")
            return True

