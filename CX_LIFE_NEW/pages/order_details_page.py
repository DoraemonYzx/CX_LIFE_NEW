#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: order_details_page.py
@time: 2020/02/19
"""
from common.base_action import BaseAction

"""
订单详情page
"""


class OrderDetailsPage(BaseAction):
    loc_cx_life = ("xpath", r"//*[@text='CX-LIFE']")

    def assert_cx_life(self):
        try:
            self.find_element(self.loc_cx_life)
        except:
            print("订单详情页面元素定位失败")
            return False
        else:
            print("订单详情页面元素定位成功")
            return True