#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:46:35
# LastEditors  : randolf
# LastEditTime : 2020-12-05 16:08:47
# FilePath     : \CatInBox\src\pipe\pipe.py
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
    
    @abstractmethod
    def file_system_xml_parse(self, xml_file_path, xml_file_name):
        """给定使用xml格式存储的文件树文件的路径和文件名，解析出这个文件树

        Args:
            xml_file_path (String): xml文件的绝对路径
            xml_file_name (String): xml文件的文件名
        
        Returns:
            FileTree: 解析出的文件树
        """
        file_tree = None
        return file_tree