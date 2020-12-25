#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:44:51
# LastEditors  : randolf
# LastEditTime : 2020-12-25 18:53:56
# FilePath     : /CheeseBox/src/util/tree.py
# 

import sys
import os
from os import path

src_path =  path.dirname(path.dirname(path.abspath(__file__)))
util_path =  path.join(src_path, 'util')
pipe_path =  path.join(src_path, 'pipes')

sys.path.append(src_path)
sys.path.append(util_path)
sys.path.append(pipe_path)

    
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
        # TODO: 需要一个node_list不?存放所有的node列表
        
    def get_subtree_node(self, relative_dir):
        """给定相对路径，返回相对路径下的子节点

        Args:
            relative_dir (String): 相对根目录的路径
        
        Returns:
            Node: 相对根目录下的子树节点
        """
        if(relative_dir == '.'):
            return self.root_node
        # dir_list = os.path.split(relative_dir)
        dir_list = relative_dir.split(os.sep)
        subtree_node = self.root_node
        for dir_item in dir_list:
            #TODO 是否应该这么写?
            if(dir_item == '.' or dir_item == ''):
                continue
            if(dir_item.startswith('./')):
                dir_item.replace('./', '')
            pos = subtree_node.binary_search(dir_item)
            if pos == -1:
                #TODO 错误处理类
                print("Search Error! node "+dir_item+' Search failed!')
                return None
            else:
                subtree_node = subtree_node.child_node[pos]
        return subtree_node

    def print_tree(self):
        """打印整棵树
        """
        self.root_node.show()


if __name__ == '__main__':
    tree = Tree(Node('hello'))
    root_node = tree.root_node
    first_level_node_list = [Node(x) for x in ['胖嘟嘟', '老干妈', '123']]
    for item in first_level_node_list:
        root_node.add_child(item)
    pdd_node_pos = root_node.binary_search('胖嘟嘟')
    lgm_node_pos = root_node.binary_search('老干妈')
    pdd_node_list = [Node(x) for x in ['12', '1', '张荣侨', '张荣Randolf', '配方法']]
    lgm_node_list = [Node(x) for x in ['沃尔沃','爱人1','怕扫平']]
    
    root_node_child_list = root_node.get_child()
    pdd_node = root_node_child_list[pdd_node_pos]
    lgm_node = root_node_child_list[lgm_node_pos]
    
    for item in pdd_node_list:
        pdd_node.add_child(item)
    for item in lgm_node_list:
        lgm_node.add_child(item)
    temp_node = Node('测试节点{}'.format(0))
    lgm_node.add_child(temp_node)
    # 长链
    for index in range(1,10):
        temp_father_node = temp_node
        temp_node = Node('测试节点{}'.format(index))
        temp_father_node.add_child(temp_node)
        temp_noise_node = Node('噪声')
        temp_father_node.add_child(temp_noise_node)
    
    tree.print_tree()
    
    test_node = tree.get_subtree_node('./老干妈/测试节点0/测试节点1/测试节点2/测试节点3')
    print(test_node.file_name)
    print('节点子树:')
    test_node.show()