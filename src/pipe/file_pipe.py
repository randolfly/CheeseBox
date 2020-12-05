#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:46:57
# LastEditors  : randolf
# LastEditTime : 2020-12-05 13:49:44
# FilePath     : /CheeseBox/src/pipe/file_pipe.py
# 

import sys
import os
sys.path.append(os.getcwd())
try:
    sys.path.append(os.getcwd()+'/src')
    sys.path.append(os.getcwd()+'/src/util')
    sys.path.append(os.getcwd()+'/src/pipe')
except Exception as e:
    # 访问异常的错误编号和详细信息
    print(e.args)
    
from file_tree import FileTree
from file_node import FileNode
from pipe import Pipe


class FilePipe(Pipe):
    
    def __init__(self,file_system_destination, file_system_root_path):
        """管道派生类，给定管道相关的存储位置(可以是本地的，也可以是网络的)
        
        FilePipe主要功能在于read & write, 对于本地的文件系统简单的进行读写操作。

        Args:
            file_system_destination (String): 管道出口(本地)的存储路径，可以用来备份文件树等等(write)
            file_system_root_path (String): 管道入口(本地)的需要读操作的根目录，可以用来生成顶层文件树(read)
        """
        Pipe.__init__(self,file_system_destination,file_system_root_path)
        
    def read_file_system(self, read_file_system_relative_path=''):
        """给定扫描文件系统的根目录，扫描出一个文件树

        Args:
            read_file_system_relative_path (String):文件系统目录，是一个相对于file_system_root_path的相对路径. Defaults to ''.

        Returns:
            FileTree: 生成的文件树
        """
        file_tree = None
        return file_tree
    
    def write_file_system(self, file_system_name):
        """根据系统中设定的file_system_destination往外写file_system的存储文件

        Args:
            file_system_name (String): 存储文件的名字
        """
        pass
        