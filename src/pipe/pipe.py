#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:46:35
# LastEditors  : randolf
# LastEditTime : 2020-12-05 13:49:00
# FilePath     : /CheeseBox/src/pipe/pipe.py
# 

import sys
import os
# sys.path.append(os.getcwd())
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/util')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/pipe')

    
# 实现虚函数，ref: https://blog.csdn.net/tony_wong/article/details/39638887
from abc import ABCMeta, abstractmethod


class Pipe():
    """管道抽象类
    
    Pipe主要功能在于read & write, 而借助linux的思路，考虑虚拟文件系统的路子，屏蔽不同文件系统来源带来的差异(比如
    网络和local的文件存储位置),简单的进行读写操作。

    """
    __metaclass__ = ABCMeta
    
    def __init__(self, file_system_destination, file_system_root_path):
        """管道基类，抽象类，给定管道相关的存储位置(可以是本地的，也可以是网络的)
        
        Pipe主要功能在于read & write, 而借助linux的思路，考虑虚拟文件系统的路子，屏蔽不同文件系统来源带来的差异(比如
        网络和local的文件存储位置),简单的进行读写操作。

        Args:
            file_system_destination (String): 管道出口(本地/网络)的存储路径，可以用来备份文件树等等(write)
            file_system_root_path (String): 管道入口(本地/网络)的需要读操作的根目录，可以用来生成顶层文件树(read)
        """
        self.file_system_destination = file_system_destination
        self.file_system_root_path = file_system_root_path
    
    @abstractmethod
    def read_file_system(self, read_file_system_relative_path=''):
        """给定扫描文件系统的根目录，扫描出一个文件树

        Args:
            read_file_system_relative_path (String):文件系统目录，是一个相对于file_system_root_path的相对路径. Defaults to ''.

        Returns:
            FileTree: 生成的文件树
        """
        file_tree = None
        return file_tree
    
    @abstractmethod
    def write_file_system(self, file_system_name):
        """根据系统中设定的file_system_destination往外写file_system的存储文件

        Args:
            file_system_name (String): 存储文件的名字
        """
        pass