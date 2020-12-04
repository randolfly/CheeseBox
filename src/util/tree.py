#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:44:51
# LastEditors  : randolf
# LastEditTime : 2020-12-05 00:13:35
# FilePath     : /CheeseBox/src/util/tree.py
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
    
from node import Node


class Tree():
    """定义逻辑上的树
    """
    
    def __init__(self, root_node):
        """初始化Tree类

        Args:
            root_node (Node): 用于初始化的root节点
        """
        self.root_node = root_node