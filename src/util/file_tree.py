#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:45:37
# LastEditors  : randolf
# LastEditTime : 2020-12-05 15:51:37
# FilePath     : /CheeseBox/src/util/file_tree.py
# 

import sys
import os
# sys.path.append(os.getcwd())
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/util')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/pipe')

    
from tree import Tree
from file_node import FileNode


class FileTree(Tree):
    """文件系统管理相关的树

    Args:
        Tree (Tree): 继承于Tree的抽象基类
    """
    
    def __init__(self, file_node, file_system_path):
        """给定文件系统的根目录地址(可以是网络上的，也可以是本地的)，初始化一个FileTree

        Args:
            file_system_path (String): 用来存储文件系统根目录地址
            file_node (FileNode): 一个文件节点，用于作为该文件树根节点
        """
        Tree.__init__(self, file_node)
        self.root_path = file_system_path
        self.file_system_type = None
    
    def fetch_file_tree(self):
        """通过Pipe获取文件树，需要依据文件系统类型选取管道

        fetch文件系统存储位置(本地/网上)获取到的文件树
        
        Returns:
            STATUS: fetch操作过程返回的状态 
        """
        # TODO 完成fetch操作
        return None