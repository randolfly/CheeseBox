#!/usr/bin/env python
# coding=utf-8
#
# Author       : randolf
# Date         : 2020-12-03 15:44:56
# LastEditors  : randolf
# LastEditTime : 2020-12-04 16:31:01
# FilePath     : /src/util/node.py
#

import sys
import os
# sys.path.append(os.getcwd())
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/util')
sys.path.append('/home/randolf/Documents/Code/Python/Project/CheeseBox/src/pipe')


from string_helper import StringHelper

from bisect import bisect_left
# import functools

class Node():
    """定义逻辑上的树操作的节点

    Attributes:
        file_name: 这个节点文件(文件夹)的名字
        father_node: 这个节点的父亲节点，至多存在一个
        child_node: 这个节点的儿子节点，可以存在多个，因此是一个列表
    """

    def __init__(self, file_name):
        """初始化Node类

        Args:
            file_name (String): 用于初始化的文件夹名字
        """
        self.file_name = file_name
        self.father_node = None
        # 由小到大排序
        self.child_node = []

        # 创建StringHelper 类
        self.string_helper = StringHelper()

    def search_left(self, file_name):
        """给定文件名，查找对应子节点,返回最接近的位置的左边index

        返回的插入点 i 可以将列表分成两部分。左侧是 all(val < x for val in a[lo:i]) ，右侧是 all(val >= x for val in a[i:hi]) 。

        Args:
            file_name (String） 待查找的文件名

        Returns:
            int: 需要查找的文件名index(左边)
        """
        # 获取拼音列表

        node_pinyin = self.string_helper.get_string_pinyin(file_name)
        child_node_pinyin = [self.string_helper.get_string_pinyin(
            node_item.file_name) for node_item in self.child_node]
        if (node_pinyin > child_node_pinyin[-1]):
            return len(child_node_pinyin)
        if(node_pinyin < child_node_pinyin[0]):
            return 0
        pos = bisect_left(child_node_pinyin, node_pinyin)
        return pos

    def binary_search(self, file_name):
        """给定文件名，查找对应子节点,存在返回index，不存在返回-1

        Args:
            file_name (String） 待查找的文件名

        Returns:
            int: 需要查找的文件名index，存在返回index，不存在返回-1
        """
        left_index = 0
        right_index = len(self.child_node)-1
        node_pinyin = self.string_helper.get_string_pinyin(file_name)
        mid_index = (left_index+right_index)//2

        while left_index <= right_index:
            mid_index = (left_index+right_index)//2
            mid_item_pinyin = self.string_helper.get_string_pinyin(
                self.child_node[mid_index].file_name)

            if node_pinyin < mid_item_pinyin:
                right_index = mid_index-1
            elif node_pinyin > mid_item_pinyin:
                left_index = mid_index+1
            else:
                return mid_index
        return -1

    def add_child(self, node):
        """为当前节点添加子节点

        Args:
            node (Node): 子节点
        """
        node.father_node = self
        if self.child_node:
            node_index = self.search_left(node.file_name)
            self.child_node.insert(node_index, node)
        else:
            self.child_node.append(node)

    def delete_child(self, file_name):
        """在当前节点中的子节点里删除file_name对应的子节点

        Args:
            file_name (String): 想要删除的子节点文件名
        """
        pos = self.binary_search(file_name)
        # TODO 定义error类型以及响应，handle这种删除错误
        if pos == -1:
            print('删除操作：未找到该节点')
        else:
            self.child_node.pop(pos)

    def set_father(self, node):
        """给当前节点设置父亲节点

        Args:
            node (Node): 想要设置的父亲节点
        """
        self.father_node = node

    def get_father(self):
        """获取当前节点的父亲节点

        Returns:
            Node: 这个节点的父亲节点
        """
        return self.father_node

    def get_child(self):
        """获取当前节点的子节点

        Returns:
            Node: 这个节点的子节点列表
        """
        return self.child_node

    # @functools.lru_cache()
    def show(self, layer=0):
        """打印当前节点下的子树

        Args:
            layer (int): 首节点前的空格. Defaults to 0.
        """
        print('|'+"--"*layer + self.file_name)
        for child in self.child_node:
            child.show(layer+1)
        # map(lambda child:child.show(layer+1), self.child_node)

if __name__ == "__main__":
    # 简单测试环节
    a = Node('hello')

    test_list = [Node(x) for x in ['胖嘟嘟', '老干妈', '123',
                                   '12', '1', '张荣侨', '张荣Randolf', '配方法','sin']]
    for item in test_list:
        a.add_child(item)

    a.show()
    print('#'*15)
    
    for item in a.child_node:
        print(item.file_name)
    print('#'*15)
    a.delete_child('胖嘟嘟')
    a.show()
    print('#'*15)
    
    for item in a.child_node:
        print(item.file_name)