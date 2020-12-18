#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-18 17:00:10
# LastEditors  : randolf
# LastEditTime : 2020-12-18 17:33:33
# FilePath     : /CheeseBox/src/test/test_string_helper.py
# 
import pytest
import allure

import sys
import os
from os import path

src_path =  path.dirname(path.dirname(path.abspath(__file__)))
util_path =  path.join(src_path, 'util')
pipe_path =  path.join(src_path, 'pipe')

sys.path.append(src_path)
sys.path.append(util_path)
sys.path.append(pipe_path)

from string_helper import StringHelper

@allure.step("获取拼音")
def chinese_pinyin_test(string_helper_obj, chinese_string):
    return string_helper_obj.get_string_pinyin(chinese_string)

@allure.step('初始化StringHelper')
def init_string_helper():
    return StringHelper()

@allure.step('获取排序后列表')
def get_sorted_string_list(string_helper_obj, string_list):
    return string_helper_obj.chinese_string_sort(string_list)

@allure.feature('测试中英文排序功能')# 用feature说明产品需求
class TestStringHelper(object):

    @allure.story('测试获取拼音功能') # 用story说明用户场景
    def test_pinyin_get(self):
        string_helper_test = init_string_helper()
        item_list = ['hello','pdd','1','_','张荣侨','踟蹰','踟躇', 'randolf0210ppp', 'rand_olf张荣侨ppp']
        target_list = ['hello', 'pdd', '1', '_', 'zhangrongqiao', 'chichu', 'chichu', 'randolf0210ppp', 'rand_olfzhangrongqiaoppp']
        ans_list = []
        for item in item_list:
            ans_list.append(chinese_pinyin_test(string_helper_test, item))
        assert ans_list == target_list
        
    @allure.story('测试排序功能') # 用story说明用户场景
    def test_sort_all(self):
        string_helper_test = init_string_helper()
        item_list = ['hello','pdd','1','_','张荣侨','踟蹰','踟躇', 'randolf0210ppp', 'rand_olf张荣侨ppp']
        target_list = ['1', '_', '踟蹰', '踟躇', 'hello', 'pdd', 'rand_olf张荣侨ppp', 'randolf0210ppp', '张荣侨']
        ans_list = get_sorted_string_list(string_helper_test, item_list)
        assert ans_list == target_list

import os

if __name__=="__main__":

    #生成测试报告json

    pytest.main(["-s", "-q", '--alluredir', 'report/result', 'test_string_helper.py'])

    #将测试报告转为html格式

    split='allure '+'generate '+'./report/result '+'-o '+'./report/html '+'--clean'

    os.system('cd ./report')

    os.system(split)

    print(split)