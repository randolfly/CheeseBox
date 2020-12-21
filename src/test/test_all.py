#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-18 17:33:24
# LastEditors  : randolf
# LastEditTime : 2020-12-21 15:35:51
# FilePath     : /CheeseBox/src/test/test_all.py
# 
import os
import pytest
import allure


if __name__=="__main__":

    #生成测试报告json

    pytest.main(["-s", "-q", '--alluredir', 'report/result', 'test_string_helper.py', 'test_node.py', 'test_tree.py', 'test_file_pipe.py'])

    #将测试报告转为html格式
    split='allure '+'generate '+'./report/result '+'-o '+'./report/html '+'--clean'
    os.system('cd ./report')
    os.system(split)
    print(split)