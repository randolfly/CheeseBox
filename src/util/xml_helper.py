#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-11-20 20:00:10
# LastEditors  : randolf
# LastEditTime : 2020-12-05 15:59:07
# FilePath     : \CatInBox\src\util\xml_helper.py
# ref: https://blog.csdn.net/weixin_36279318/article/details/79176475


import os
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
        
    def parse_xml(self, file_path, file_name):
        """给定xml文件地址以及xml文件名，解析这个文件为一棵树

        Args:
            file_path (String): xml文件的地址
            file_name (String): xml文件的文件名
        
        Returns:
            ElementTree: xml树(未处理为文件树)
        """
        #TODO Error类型处理
        self.xml_tree = ET.parse(os.path.join(file_path,file_name))
        return self.xml_tree