#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:45:37
# LastEditors  : randolf
# LastEditTime : 2020-12-05 00:34:47
# FilePath     : /CheeseBox/src/util/file_tree.py
# 

import sys
import os
sys.path.append(os.getcwd())
try:
    sys.path.append(os.getcwd()+'/src')
    sys.path.append(os.getcwd()+'/src/util')
except Exception as e:
    # 访问异常的错误编号和详细信息
    print(e.args)
    
from tree import Tree
from file_node import FileNode


class FileTree(Tree):
    """文件系统管理相关的树

    Args:
        Tree (Tree): 继承于Tree的抽象基类
    """
    
    def __init__(self, file_node):
        """给定FileNode，初始化一个FileTree

        Args:
            file_node (FileNode): 用来作为根节点的FileNode
        """
        Tree.__init__(self, file_node)
        self.root_node = file_node
        self.root_path = ""
        self.file_system_type = None
    
    def fetch_file_tree(self):
        """通过Pipe获取文件树，需要依据文件系统类型选取管道

        fetch文件系统存储位置(本地/网上)获取到的文件树
        
        Returns:
            STATUS: fetch操作过程返回的状态 
        """
        # TODO 完成fetch操作
        return None