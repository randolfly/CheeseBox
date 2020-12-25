#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-21 14:59:20
# LastEditors  : randolf
# LastEditTime : 2020-12-25 18:53:31
# FilePath     : /CheeseBox/src/test/test_file_pipe.py
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

from file_pipe import FilePipe
from test_tree import get_subtree_node
from test_node import get_child_list


@allure.step('创建一个FilePipe对象')
def init_file_pipe(file_system_destination, file_system_root_path):
    return FilePipe(file_system_destination, file_system_root_path)

@allure.step('给定文件系统根路径，扫描文件系统生成文件树')
def read_file_system(file_pipe):
    return file_pipe.read_file_system()

@allure.feature('测试FilePipe功能')
class TestFilePipe(object):
    
    @allure.story('测试创建FilePipe文件管道')
    def test_file_pipe_init(self):
        write_pwd = os.getcwd()
        read_path = path.dirname(os.getcwd())
        file_pipe = init_file_pipe(write_pwd, read_path)
        assert file_pipe is not None
        assert file_pipe.file_system_destination == write_pwd
        assert file_pipe.file_system_root_path == read_path
        
    @allure.story('测试扫描文件系统，获取文件树功能')
    def test_read_file_system(self):
        write_pwd = os.getcwd()
        read_path = path.dirname(os.getcwd())
        file_pipe = init_file_pipe(write_pwd, read_path)
        assert file_pipe is not None
        
        file_tree = read_file_system(file_pipe)
        assert file_tree is not None
        
        t1 = get_subtree_node(file_tree, 'main.py')
        t2 = get_subtree_node(file_tree, 'pipe/file_pipe.py')
        t3 = get_subtree_node(file_tree, 'pipe/file_pipe.pyd')
        t4 = get_subtree_node(file_tree, 'test/report/html')
        t5 = get_subtree_node(file_tree, 'test/test_all.py')
        t6 = get_subtree_node(file_tree, 'util/file_tree.py')
        t7 = get_subtree_node(file_tree, 'util')
        # file_tree.print_tree()

        assert t1.file_name == 'main.py'
        assert t2.file_name == 'file_pipe.py'
        assert t3 is None
        assert t4.file_name == 'html'
        assert t5.file_name == 'test_all.py'
        assert t6.file_name == 'file_tree.py'
        assert t7 is not None
        
        # print('hello')
        
        util_child_list = get_child_list(t7)
        assert len(util_child_list) == 13
        
        
import os

if __name__=="__main__":

    #生成测试报告json

    pytest.main(["-s", "-q", '--alluredir', 'report/result', 'test_file_pipe.py'])

    #将测试报告转为html格式

    split='allure '+'generate '+'./report/result '+'-o '+'./report/html '+'--clean'
    os.system('cd ./report')
    os.system(split)
    print(split)