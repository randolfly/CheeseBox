#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-18 17:31:52
# LastEditors  : randolf
# LastEditTime : 2020-12-20 23:56:23
# FilePath     : /CheeseBox/src/test/test_tree.py
# 
import pytest
import allure

import sys
import os
from os import path

src_path =  path.dirname(path.dirname(path.abspath(__file__)))
util_path =  path.join(src_path, 'util')
pipe_path =  path.join(src_path, 'pipes')
test_path =  path.join(src_path, 'test')


sys.path.append(src_path)
sys.path.append(util_path)
sys.path.append(pipe_path)
sys.path.append(test_path)


from tree import Tree
from node import Node
from test_node import *


@allure.step("初始化树")
def init_tree(file_name):
    return Tree(init_node(file_name))

@allure.step("给定相对路径，获取子树顶点")
def get_subtree_node(tree, relative_dir):
    return tree.get_subtree_node(relative_dir)


@allure.feature('测试Tree树结构的功能')# 用feature说明产品需求
class TestTree(object):
    
    @allure.story('测试生成树')
    def test_tree_init(self):
        # 初始化树
        tree = Tree(init_node('hello'))
        root_node = tree.root_node
        first_level_node_list = [init_node(x) for x in ['胖嘟嘟', '老干妈', '123']]
        for item in first_level_node_list:
            add_child(root_node, item)
        pdd_node_pos = binary_search(root_node, '胖嘟嘟')
        lgm_node_pos = binary_search(root_node, '老干妈')
        assert pdd_node_pos == 2
        assert lgm_node_pos == 1
        root_node_child_list = get_child_list(root_node)
        pdd_node = root_node_child_list[pdd_node_pos]
        lgm_node = root_node_child_list[lgm_node_pos]
        
        pdd_node_list = [init_node(x) for x in ['12', '1', '张荣侨', '张荣Randolf', '配方法']]
        lgm_node_list = [init_node(x) for x in ['沃尔沃','爱人1','怕扫平']]
        for item in pdd_node_list:
            add_child(pdd_node, item)
        for item in lgm_node_list:
            add_child(lgm_node, item)
        # 检测
        target_list = ['123', '老干妈', '胖嘟嘟']
        ans_list = [x.file_name for x in get_child_list(root_node)]
        assert target_list == ans_list
        
        target_list = ['1', '12', '配方法', '张荣Randolf', '张荣侨']
        ans_list = [x.file_name for x in get_child_list(pdd_node)]
        assert target_list == ans_list
        
        target_list = ['爱人1', '怕扫平', '沃尔沃']
        ans_list = [x.file_name for x in get_child_list(pdd_node)]
        assert target_list == ans_list
    
    @allure.story('测试树相对路径访问')
    def test_tree_init(self):
        # 初始化树
        tree = Tree(init_node('hello'))
        root_node = tree.root_node
        first_level_node_list = [init_node(x) for x in ['胖嘟嘟', '老干妈', '123']]
        for item in first_level_node_list:
            add_child(root_node, item)
        pdd_node_pos = binary_search(root_node, '胖嘟嘟')
        lgm_node_pos = binary_search(root_node, '老干妈')
        assert pdd_node_pos == 2
        assert lgm_node_pos == 1
        
        root_node_child_list = get_child_list(root_node)
        pdd_node = root_node_child_list[pdd_node_pos]
        lgm_node = root_node_child_list[lgm_node_pos]
        
        pdd_node_list = [init_node(x) for x in ['12', '1', '张荣侨', '张荣Randolf', '配方法']]
        lgm_node_list = [init_node(x) for x in ['沃尔沃','爱人1','怕扫平']]
        
        for item in pdd_node_list:
            add_child(pdd_node, item)
        for item in lgm_node_list:
            add_child(lgm_node, item)
        temp_node = init_node('测试节点{}'.format(0))
        add_child(lgm_node,temp_node)
        # 长链
        for index in range(1,10):
            temp_father_node = temp_node
            temp_node = init_node('测试节点{}'.format(index))
            add_child(temp_father_node, temp_node)
            temp_noise_node = init_node('噪声')
            add_child(temp_father_node, temp_noise_node)
        
        tree.print_tree()
        t1 = get_subtree_node(tree, '老干妈/爱人1')
        t2 = get_subtree_node(tree, '老干妈/爱人')
        t3 = get_subtree_node(tree, '老干妈/测试节点0')
        t4 = get_subtree_node(tree, '老干妈/测试节点0/测试节点1/测试节点2/测试节点3')
        
        assert t1.file_name=='爱人1'
        assert t2 == None
        assert t3.file_name == '测试节点0'
        assert t4.file_name == '测试节点3'
        

import os

if __name__=="__main__":

    #生成测试报告json

    pytest.main(["-s", "-q", '--alluredir', 'report/result', 'test_tree.py'])

    #将测试报告转为html格式

    split='allure '+'generate '+'./report/result '+'-o '+'./report/html '+'--clean'

    os.system('cd ./report')

    os.system(split)

    print(split)