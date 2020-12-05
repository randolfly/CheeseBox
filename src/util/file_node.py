#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:46:02
# LastEditors  : randolf
# LastEditTime : 2020-12-05 15:51:25
# FilePath     : /CheeseBox/src/util/file_node.py
# 

import sys
import os
# sys.path.append(os.getcwd())
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/util')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/pipe')

    
from node import Node

class FileNode(Node):
    """继承Node，作为FileNode的节点

    Args:
        Node ([type]): [description]
    """
    
    def __init__(self, file_name):
        """初始化一个文件节点，给定根节点的文件名

        Args:
            file_name (String): 根节点的文件名
        """
        Node.__init__(self, file_name)
        self.tag_list = []
        
    def get_relative_path(self):
        """获取文件node的路径，在当前文件系统下的相对路径，可以是磁盘上的，也可以是网络上的

        Returns:
            String: 相对于文件系统下的相对路径("./A/B/C/")
        """
        cur_node = self
        cur_path = ''
        while(cur_node.father_node):
            cur_path = os.path.sep + cur_node.file_name + cur_path
            cur_node = cur_node.father_node
        return cur_path
    
    def get_tag(self):
        """获取当前文件node的tag列表

        Returns:
            List: node的tag列表
        """
        return self.tag_list
    
    
if __name__ == "__main__":
    # 简单测试环节
    a = FileNode('hello')
    test_list = [FileNode(x) for x in ['胖嘟嘟', '老干妈', '123',
                                   '12', '1', '张荣侨', '张荣Randolf', '配方法','sin']]
    for item in test_list:
        a.add_child(item)
    
    for item in a.child_node:
        print(item.file_name)
    print('#'*15)
    a.delete_child('胖嘟嘟')
    for item in a.child_node:
        print(item.file_name)