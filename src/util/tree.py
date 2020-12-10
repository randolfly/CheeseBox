#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:44:51
# LastEditors  : randolf
# LastEditTime : 2020-12-10 17:00:33
# FilePath     : /CheeseBox/src/util/tree.py
# 

import sys
import os
from os import path

src_path =  path.dirname(path.dirname(path.abspath(__file__)))
util_path =  path.join(src_path, 'util')
pipe_path =  path.join(src_path, 'pipe')

sys.path.append(src_path)
sys.path.append(util_path)
sys.path.append(pipe_path)

    
from node import Node


class Tree():
    """定义逻辑上的树
    """
    
    def __init__(self, node):
        """初始化Tree类
        
        认为Tree根节点file_name为'.'
        
        Args:
            node (Node): 根节点
        """
        self.root_node = node
        self.root_node.file_name = '.'
        # TODO: 需要一个node_list不?存放所有的node列表
        
    def get_subtree_node(self, relative_dir):
        """给定相对路径，返回相对路径下的子节点

        Args:
            relative_dir (String): 相对根目录的路径
        
        Returns:
            Node: 相对根目录下的子树节点
        """
        if(relative_dir == '.'):
            return self.root_node
        dir_list = os.path.split(relative_dir)
        subtree_node = self.root_node
        for dir_item in dir_list:
            #TODO 是否应该这么写?
            if(dir_item=='.'):
                pass
            pos = subtree_node.binary_search(dir_item)
            if pos == -1:
                #TODO 错误处理类
                print("Search Error! node "+dir_item+' Search failed!')
            else:
                subtree_node = subtree_node.child_node[pos]
        return subtree_node

    def print_tree(self):
        """打印整棵树
        """
        self.root_node.show()
