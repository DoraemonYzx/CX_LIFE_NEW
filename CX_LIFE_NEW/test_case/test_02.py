#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: test_01.py
@time: 2020/02/18
"""

import unittest
from selenium import webdriver
from common.base_driver import base_driver
from common.base_action import BaseAction
from pages.wx_page import WxPage
from pages.home_page import HomePage
from pages.commodity_details_page import CommodityDetailsPage
from pages.my_page import MyPage
from pages.navigation_bar_page import NavigationBarPage
from pages.confirm_order_page import ConfirmOrderPage
from pages.pay_complete_page import PayCompletePage
from pages.my_order_page import MyOrderPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.order_details_page import OrderDetailsPage
from time import sleep

"""
从首页选择商品加入购物车从购物车购买：
1、进入小程序
2、从首页选择一个商品
3、将商品加入购物车
4、在购物车结算
5、进行付款
6、查看订单
"""


class TestCase02(unittest.TestCase):
    """从首页选择商品加入购物车从购物车购买"""
    @classmethod
    def setUpClass(cls):
        cls.driver = base_driver()
        cls.baseaction = BaseAction(cls.driver)
        cls.wx_page = WxPage(cls.driver)
        cls.home_page = HomePage(cls.driver)
        cls.commodity_details_page = CommodityDetailsPage(cls.driver)
        cls.my_page = MyPage(cls.driver)
        cls.navigation_bar_page = NavigationBarPage(cls.driver)
        cls.confirm_order_page = ConfirmOrderPage(cls.driver)
        cls.pay_complete_page = PayCompletePage(cls.driver)
        cls.my_order_page = MyOrderPage(cls.driver)
        cls.shopping_cart_page = ShoppingCartPage(cls.driver)
        cls.order_details_page = OrderDetailsPage(cls.driver)
        print("开始测试")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_001(self):
        """进入常笑生活小程序"""
        for i in range(3):
            self.wx_open = self.wx_page.assert_find_search()
            print(self.wx_open)
            if self.wx_open:
                print("已经进入微信页面，开始下一步操作")
                self.baseaction.swipe_up_and_down(0.5, 0.2, 0.8)
                self.wx_page.click_cxlife()
                break
            else:
                print("还没有进入微信。")
        self.assertTrue(self.wx_open,msg="进入微信超时")

    def test_002(self):
        """选择某一商品"""
        for i in range(4):
            self.home_open = self.home_page.assert_find_must_buy_one()
            print(self.home_open)
            self.home_page.assert_click_plus_coupon()
            if self.home_open:
                self.navigation_bar_page.click_shopping_cart()
                self.navigation_bar_page.click_home()
                print("已经常笑生活首页，开始下一步操作")
                self.baseaction.swipe_up_and_down(0.5, 0.8, 0.3)
                sleep(1.5)
                self.home_page.click_commodity_one()
                break
            else:
                print("还没有进入首页。")
        self.assertTrue(self.commodity_details_page.assert_buy(), msg="没有进入商品详情页！")

    def test_003(self):
        """商品加入购物车"""
        self.commodity_details_page.click_add_to_cart()
        self.not_login_in = self.my_page.assert_confirm_login()
        if self.not_login_in:
            self.my_page.click_confirm_login()
            self.my_page.click_wx_login()
            self.commodity_details_page.click_add_to_cart()
        else:
            pass
        self.assertTrue(self.shopping_cart_page.assert_buy_now(), msg="没有进入购物车")

    def test_004(self):
        """在购物车结算"""
        self.shopping_cart_page.click_buy_now()
        self.assertTrue(self.confirm_order_page.assert_pay(), msg="没有进入确认订单页面")

    def test_005(self):
        """进行付款"""
        self.confirm_order_page.click_pay()
        self.assertTrue(self.pay_complete_page.assert_pay_success(), msg="没有支付完成")

    def test_006(self):
        """查看订单"""
        self.pay_complete_page.click_return_order()
        self.assertTrue(self.my_order_page.assert_all(), msg="没有进入全部订单页面")

    def test_007(self):
        """查看订单详情"""
        self.my_order_page.click_order_one()
        self.assertTrue(self.order_details_page.assert_cx_life(), msg="没有进入订单详情页")
