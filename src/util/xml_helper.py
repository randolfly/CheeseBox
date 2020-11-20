#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-11-20 20:00:10
# LastEditors  : randolf
# LastEditTime : 2020-11-20 20:34:37
# FilePath     : \CatInBox\src\util\xml_helper.py
# 



import xml.etree.ElementTree as ET

class XmlHelper():
    
    def add_node(self, node, father):
        """给定一个node节点和一个父亲节点，将node插入到父亲节点下

        Args:
            node (Node): 一个需要插入的节点，将在XML文件中其插入到父亲节点(father)下
            father (Node): 文件树中待插入的节点
        """
        
    def xml_generate(self, file_name, file_path):
        """给定文件名生成一个xml文件，用于存储UI树结构或者File 树结构

        Args:
            file_name (String): 生成的XML文件文件名
            file_path (String): 生成的XML文件文件绝对路径
        """