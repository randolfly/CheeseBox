#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:46:57
# LastEditors  : randolf
# LastEditTime : 2020-12-05 10:50:11
# FilePath     : \CatInBox\src\pipe\file_pipe.py
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

from file_tree import FileTree
from file_node import FileNode
from pipe import Pipe

# import functools


class FilePipe(Pipe):
    
    def __init__(self,file_system_destination, file_system_root_path):
        """管道派生类，给定管道相关的存储位置(可以是本地的，也可以是网络的)
        
        FilePipe主要功能在于read & write, 对于本地的文件系统简单的进行读写操作。

        Args:
            file_system_destination (String): 管道出口(本地)的存储路径，可以用来备份文件树等等(write)
            file_system_root_path (String): 管道入口(本地)的需要读操作的根目录，可以用来生成顶层文件树(read)
        """
        Pipe.__init__(self,file_system_destination,file_system_root_path)
        # 计数节点数目
        self.item_number = 0
        
    def read_file_system(self, read_file_system_relative_path=''):
        """给定扫描文件系统的根目录，扫描出一个文件树

        Args:
            read_file_system_relative_path (String):文件系统目录，是一个相对于file_system_root_path的相对路径. Defaults to ''.

        Returns:
            FileTree: 生成的文件树
        """
        #TODO: 判定正确路径与否(可以采用UI方式选取)
        if(read_file_system_relative_path==''):
            src_path = self.file_system_root_path
        else:
            src_path = os.path.join(self.file_system_root_path, read_file_system_relative_path)
        file_root_node = FileNode(os.path.split(src_path)[-1])
        file_tree = FileTree(file_root_node, src_path)

        self.get_file_tree(src_path, file_root_node)
        
        return file_tree
    
    def write_file_system(self, file_system_name):
        """根据系统中设定的file_system_destination往外写file_system的存储文件

        Args:
            file_system_name (String): 存储文件的名字
        """
        pass
        
    # @functools.lru_cache()
    def get_file_tree(self, root_path, file_node):
        """递归函数，遍历该文档目录和子目录下的所有文件，获取其path

        Args:
            root_path (String): 根目录
            file_node (FileNode): 根目录文件节点
        """
        file_list = os.listdir(root_path)
        for file_item in file_list:
            cur_path = root_path + os.path.sep + file_item
            # 测试用
            self.item_number += 1
            if not os.path.isdir(cur_path):   # not a dir
                file_node.add_child(FileNode(file_item))
            else:  # is a dir
                dir_file_node = FileNode(file_item)
                file_node.add_child(dir_file_node)
                self.get_file_tree(cur_path, dir_file_node)
                
                
# @functools.lru_cache() # 递归加速，记录递归数据
def print_all_path(root_node):
    """测试用函数
    """
    for node in root_node.get_child():
        if(node.get_child()):
            print_all_path(node)
        else:
            print(node.get_relative_path())
    
if __name__ == "__main__":
    # 简单测试
    # file_pipe = FilePipe(os.getcwd(), os.getcwd()+'/src')
    file_pipe = FilePipe(os.getcwd(), '/home/randolf/Documents/Code/')
    print(os.getcwd())
    print('=='*10)
    
    file_tree = file_pipe.read_file_system()
    file_tree.print_tree()
    print('=='*10)
    # print_all_path(file_tree.root_node)
    print('item total number of this file tree: ', file_pipe.item_number)