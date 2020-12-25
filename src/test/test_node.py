#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-18 17:31:52
# LastEditors  : randolf
# LastEditTime : 2020-12-18 20:19:32
# FilePath     : /src/test/test_node.py
# 
import pytest
import allure

import sys
import os
from os import path

src_path =  path.dirname(path.dirname(path.abspath(__file__)))
util_path =  path.join(src_path, 'util')
pipe_path =  path.join(src_path, 'pipes')

sys.path.append(src_path)
sys.path.append(util_path)
sys.path.append(pipe_path)

from node import Node

@allure.step("初始化Node")
def init_node(file_name):
    return Node(file_name)

@allure.step('根据FileName，查找孩子中最接近的位置的左边index')
def search_left(node, file_name):
    return node.search_left(file_name)

@allure.step('根据FileName，二分查找孩子的index')
def binary_search(node, file_name):
    return node.binary_search(file_name)

@allure.step('添加一个孩子')
def add_child(node, child_node):
    return node.add_child(child_node)

@allure.step('删除一个孩子')
def delete_child(node, file_name):
    return node.delete_child(file_name)

@allure.step('获取节点的父亲')
def get_father(node):
    return node.get_father()

@allure.step('获取节点的孩子列表')
def get_child_list(node):
    return node.get_child()

@allure.step('打印节点树')
def show_file_tree(node):
    return node.show()

@allure.feature('测试Node节点的功能')# 用feature说明产品需求
class TestNode(object):
    
    @allure.story('测试插入子节点功能')
    def test_node_insert(self):
        root_node = init_node('hello')
        test_list = [init_node(x) for x in ['胖嘟嘟', '老干妈', '123',
                                   '12', '1', '张荣侨', '张荣Randolf', '配方法','sin']]
        for item in test_list:
            root_node.add_child(item)
        target_list = ['1', '12', '123', '老干妈', '胖嘟嘟', '配方法', 'sin', '张荣Randolf', '张荣侨']
        ans_list = [x.file_name for x in get_child_list(root_node)]
        assert ans_list == target_list
        
    @allure.story('测试删除子节点功能')
    def test_node_delete(self):
        root_node = init_node('hello')
        test_list = [init_node(x) for x in ['胖嘟嘟', '老干妈', '123',
                                   '12', '1', '张荣侨', '张荣Randolf', '配方法','sin']]
        for item in test_list:
            root_node.add_child(item)
        
        delete_child(root_node, '张荣侨')
        delete_child(root_node, '张荣侨')
        delete_child(root_node, '配方法')
        
        target_list = ['1', '12', '123', '老干妈', '胖嘟嘟', 'sin', '张荣Randolf']
        ans_list = [x.file_name for x in get_child_list(root_node)]
        assert ans_list == target_list

    @allure.story('测试从左搜索功能')
    def test_search_method(self):
        root_node = init_node('hello')
        test_list = [init_node(x) for x in ['胖嘟嘟', '老干妈', '123',
                                   '12', '1', '张荣侨', '张荣Randolf', '配方法','sin']]
        for item in test_list:
            root_node.add_child(item)
        s1 = search_left(root_node, '1')
        s2 = search_left(root_node, '2')
        s3 = search_left(root_node, '张荣')
        s4 = search_left(root_node, '刘')
        s5 = search_left(root_node, '_')
        
        # 按照从大到小顺序搜索
        # ['1', '12', '123', '老干妈', '胖嘟嘟', '配方法', 'sin', '张荣Randolf', '张荣侨']
        assert s1 == 0
        assert s2 == 3
        assert s3 == 7
        assert s4 == 4
        assert s5 == 3
        
    @allure.story('测试二分准确搜索功能')
    def test_binary_search(self):
        root_node = init_node('hello')
        test_list = [init_node(x) for x in ['胖嘟嘟', '老干妈', '123',
                                   '12', '1', '张荣侨', '张荣Randolf', '配方法','sin']]
        for item in test_list:
            root_node.add_child(item)
            
        s1 = binary_search(root_node, '1')
        s2 = binary_search(root_node, '2')
        s3 = binary_search(root_node, '张荣')
        s4 = binary_search(root_node, '刘')
        s5 = binary_search(root_node, '张荣侨')

        # 按照从大到小顺序搜索
        # ['1', '12', '123', '老干妈', '胖嘟嘟', '配方法', 'sin', '张荣Randolf', '张荣侨']
        assert s1 == 0
        assert s2 == -1
        assert s3 == -1
        assert s4 == -1
        assert s5 == 8
        

import os

if __name__=="__main__":

    #生成测试报告json

    pytest.main(["-s", "-q", '--alluredir', 'report/result', 'test_node.py'])

    #将测试报告转为html格式

    split='allure '+'generate '+'./report/result '+'-o '+'./report/html '+'--clean'

    os.system('cd ./report')

    os.system(split)

    print(split)