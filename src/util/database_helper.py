#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-11-20 20:00:30
# LastEditors  : randolf
# LastEditTime : 2020-11-20 20:50:38
# FilePath     : \CatInBox\src\util\database_helper.py
# 


class DatabaseHelper():
    """数据库操作类，用于存储tag信息
    """
    
    def __init__(self, datapath_path):
        """DatabaseHelper初始化类

        Args:
            datapath_path (String): 数据库存储的全局路径
        """
        self.database_path = dict()
        self.sql_database = NotImplemented
        
    def node_tag_write(self, node):
        """指定节点，将其tag存储至数据库中

        Args:
            node (FileNode): 需要存储的文件节点
        """
        
    def tree_tag_write(self, tree):
        """指定文件树，将其tag存储至数据库中

        Args:
            tree (FileTree): 需要存储的文件树
        """
        
    def tag_search(self, tag):
        """指定需要搜索的tag, 在数据库中进行搜索并返回搜索结果列表

        Args:
            tag (String): 给定的搜索tag名称
        """
        