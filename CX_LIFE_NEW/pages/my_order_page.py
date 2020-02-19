#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: my_order_page.py
@time: 2020/02/18
"""
from common.base_action import BaseAction
from selenium import webdriver


class MyOrderPage(BaseAction):
    loc_pending_payment = ("xpath", r"//*[@text='待付款']")
    loc_to_be_shipped = ("xpath", r"//*[@text='待发货']")
    loc_receivable = ("xpath", r"//*[@text='待收货']")
    loc_all = ("xpath", r"//*[@text='全部']")
    loc_completed = ("xpath", r"//*[@text='已完成']")
    loc_order_no = ("xpath", r"//*[@text='wx0f98b556b1c08f70:pages/order/pages/orderList/orderList.html:VISIBLE']/android.view.View[1]/android.view.View[3]")
    loc_order_one = ("xpath", r"//*[@text='wx0f98b556b1c08f70:pages/order/pages/orderList/orderList.html:VISIBLE']/android.view.View[1]/android.view.View[5]")

    def click_pending_payment(self):
        self.click(self.loc_pending_payment)

    def click_to_be_shipped(self):
        self.click(self.loc_to_be_shipped)

    def click_receivable(self):
        self.click(self.loc_receivable)

    def click_all(self):
        self.click(self.loc_all)

    def click_completed(self):
        self.click(self.loc_completed)

    def order_no(self):
        order_no = self.find_element(self.loc_order_no).text
        return order_no

    def click_order_one(self):
        self.click(self.loc_order_one)



    def assert_all(self):
        try:
            self.find_element(self.loc_all)
        except:
            print("我的订单页面元素定位失败")
            return False
        else:
            print("我的订单页面元素定位成功")
            return True
