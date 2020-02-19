#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:余振新
@file: wx_page.py
@time: 2020/02/14
"""
from common.base_action import BaseAction

"""
微信page
"""

class WxPage(BaseAction):
    loc_cxlife = ("xpath", "//android.widget.FrameLayout[@content-desc='当前所在页面,与的聊天']/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/"
                           "android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.tencent.mm.ui.mogic.WxViewPager/android.widget.FrameLayout/"
                           "android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/"
                           "android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.RelativeLayout/android.support.v7.widget.RecyclerView/"
                           "android.widget.RelativeLayout[1]")
    loc_search = ("id", "com.tencent.mm:id/r_")

    def click_cxlife(self):
        self.click(self.loc_cxlife)

    def assert_find_search(self):
        try:
            self.find_element(self.loc_search)
        except:
            print("微信没有启动")
            return False
        else:
            print("微信启动了")
            return True
