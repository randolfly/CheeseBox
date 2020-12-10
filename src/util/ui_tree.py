#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:45:41
# LastEditors  : randolf
# LastEditTime : 2020-12-10 16:57:42
# FilePath     : /CheeseBox/src/util/ui_tree.py
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

from ui_node import UINode
from tree import Tree
from config import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtXml import *
from PyQt5.QtPrintSupport import *

import math
import time 
import random


class UITree(Tree, QGraphicsScene):
    """UI显示相关的树

    Args:
        Tree (Tree): 继承于Tree的抽象基类
        
    Signals:
        contentChanged: node content change signal
        nodeNumChange: num od node changed
        messageShow: message show in status bar
        press_close: press scene close subWindow(Note Window and Link Window)
    """
    brachDistance = 80
    contentChanged = pyqtSignal()
    nodeNumChange = pyqtSignal(int)
    messageShow = pyqtSignal(str)
    press_close = pyqtSignal()
    
    def __init__(self, file_node):
        Tree.__init__(self, file_node)
        QGraphicsScene.__init__(self)
        
        self.center_x =  self.sceneRect().x() + self.sceneRect().width()/2
        self.center_y = self.sceneRect().y() + self.sceneRect().height()/2
        self.m_activateNode = None

        self.branch_list = []
        self.m_context = None
        self.m_editingMode = False
        
        self.addFirstNode()
    
    # 生成 Node 并且将 Node 与 Slots 连接
    def nodeFactory(self):
        node = UINode()

        node.nodeChanged.connect(self.nodeChanged)
        node.nodeEdited.connect(self.nodeEdited)
        node.nodeSelected.connect(self.nodeSelected)
        node.nodeMoved.connect(self.nodeMoved)
        node.nodeLostFocus.connect(self.nodeLostFocus)

        return node

    def setUndoStack(self, stack):
        self.m_undoStack = stack

    def addFirstNode(self):
        node = self.nodeFactory()
        node.setPos(self.center_x, self.center_y)
        node.setNodeLevel(MainThemeLevel)

        self.setActivateNode(node)

        self.addItem(node)
        self.NodeList.append(node)
        
    