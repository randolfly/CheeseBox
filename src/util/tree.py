#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:44:51
# LastEditors  : randolf
# LastEditTime : 2020-12-05 15:37:06
# FilePath     : /CheeseBox/src/util/tree.py
# 

import sys
import os
# sys.path.append(os.getcwd())
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/util')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/pipe')

    
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
