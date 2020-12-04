#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:46:35
# LastEditors  : randolf
# LastEditTime : 2020-12-05 00:35:07
# FilePath     : /CheeseBox/src/pipe/pipe.py
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
    
from file_tree import FileTree
from file_node import FileNode


class Pipe():
    """管道抽象类
    #TODO: 仔细思考Pipe设计
    """
    
    def __init__(self, file_destination):
        """管道基类，给定管道相关的存储位置(可以是本地的，也可以是网络的)

        Args:
            file_destination (String): 管道出口(本地/网络)的存储位置，可以用来备份文件树等等
        """
        self.file_destination = file_destination
        
    # def file_system_scan(self, file_system_root_path):
    #     """给定扫描文件系统的根目录，扫描出一个文件树

    #     Args:
    #         file_system_root_path (String): 文件系统根目录

    #     Returns:
    #         FileTree: [description]
    #     """
    #     file_tree = None
    #     return file_tree