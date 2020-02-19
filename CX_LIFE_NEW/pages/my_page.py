#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: my_page.py
@time: 2020/02/16
"""
from common.base_action import BaseAction


class MyPage(BaseAction):
    loc_login = ("xpath", r"//*[@text='登录/注册']")
    loc_pending_payment = ("xpath", r"//*[@text='待付款']")
    loc_to_be_shipped = ("xpath", r"//*[@text='待发货']")
    loc_receivable = ("xpath", r"//*[@text='待收款']")
    loc_all_orders = ("xpath", r"//*[@text='全部订单']")

    loc_wx_login = ("xpath", r"//*[@text='微信登录']")

    loc_allow = ("xpath", r"//*[@text='允许']")

    # 未登录时弹出的登录提醒中的"确认登录"按钮
    loc_confirm_login = ("id", "com.tencent.mm:id/b49")

    def click_login(self):
        self.click(self.loc_login)

    def click_pending_payment(self):
        self.click(self.loc_pending_payment)

    def click_to_be_shipped(self):
        self.click(self.loc_to_be_shipped)

    def click_receivable(self):
        self.click(self.loc_receivable)

    def click_all_orders(self):
        self.click(self.loc_all_orders)

    def click_wx_login(self):
        self.click(self.loc_wx_login)

    def click_allow(self):
        self.click(self.loc_allow)

    def click_confirm_login(self):
        self.click(self.loc_confirm_login)

    # 判断是否有未登录登录提醒弹窗弹出
    def assert_confirm_login(self):
        try:
            self.find_element(self.loc_confirm_login)
        except:
            print("已登录，登录提示框未弹出")
            return False
        else:
            print("未登录，登录提示框弹出")
            return True
