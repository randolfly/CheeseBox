#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-12-03 15:46:12
# LastEditors  : randolf
# LastEditTime : 2020-12-10 16:57:24
# FilePath     : /CheeseBox/src/util/ui_node.py
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

    
from node import Node
from config import *

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class UINode(Node, QGraphicsTextItem):
    """继承Node, 作为视图上Node的节点，用于显示UI的文件系统树

    Args:
        Node (Node): [description]
        
    Attributes:
        TODO
        x_position (float): 
        
    Signals:
        nodeChanged: node content change
        nodeMoved: node moved
        nodeEdited: dobleclick edit node
        nodeSelected: click select node
        nodeLostFocus: node lost focus
    """
    
    node_changed = pyqtSignal()
    node_moved = pyqtSignal(int, int)
    node_edited = pyqtSignal()
    node_selected = pyqtSignal()
    node_lost_focus = pyqtSignal()
    
    def __init__(self, file_name):
        """初始化一个文件节点，给定根节点的文件名

        Args:
            file_name (String): 根节点的文件名
        """
        Node.__init__(self, file_name)
        QGraphicsTextItem.__init__(self)
        
        self.x_position = 0
        self.y_position = 0
        self.width = 0
        
        self.default_text = ''
        self.m_size = (60, 30)
        self.m_margin = 30
        self.m_border = False
        self.m_color = QColor(Qt.white)
        self.m_level = -1
        self.m_textColor = QColor(Qt.black)
        self.m_editable = False
        
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)
        
    def setBorder(self, hasBorder):
        self.m_border = hasBorder
        self.update()

    def setColor(self, color):
        self.m_color = color
        self.update()

    def setTextColor(self, textColor):
        self.m_textColor = textColor
        self.update()

    def setMargin(self, margin):
        self.margin = margin
        self.update()

    def setEditable(self, editable):
        if not editable:
            self.setTextInteractionFlags(Qt.NoTextInteraction)
            self.setTextInteractionFlags(Qt.TextBrowserInteraction)
            return
        
        self.setTextInteractionFlags(Qt.TextEditorInteraction)

    def setNodeLevel(self, level):
        self.m_level = level

        if level == MainThemeLevel:
            self.setMargin((5, 4))
            self.setColor(QColor(Qt.red))
            self.setTextColor(QColor(Qt.white))
            self.setPlainText('中心主题')
        elif level == SecondThemeLevel:
            self.setMargin((3, 2))
            self.setColor(QColor(Qt.gray))
            self.setTextColor(QColor(Qt.black))
            self.setPlainText('分支主题')
        elif level == ThirdThemeLevel:
            self.setMargin((2, 1))
            self.setColor(QColor(Qt.white))
            self.setTextColor(QColor(Qt.black))
            self.setPlainText('子主题')
        elif level == FreeThemeLevel:
            self.setColor(QColor(Qt.black))
            self.setTextColor(QColor(Qt.wwhite))
            self.setPlainText('自由主题')
    
    def paint(self, painter, option, w):
        if self.m_border:
            painter.setPen(QPen(QBrush(Qt.black), 1))
        else:
            painter.setPen(Qt.transparent)

        painter.setBrush(self.m_color)
        '''rect = QRectF(self.boundingRect().x() - self.margin[0], 
                        self.boundingRect().y() - self.margin[1],
                        self.boundingRect().width() + self.margin[0]*2, 
                        self.boundingRect().height() + self.margin[1]*2)
        painter.drawRoundedRect(rect, 10.0, 5.0)
        painter.drawRoundedRect(QRectF(*self.size), 10.0, 5.0)'''
        painter.drawRoundedRect(self.boundingRect(), 10.0, 5.0)

        painter.setBrush(Qt.NoBrush)
        self.setDefaultTextColor(self.m_textColor)

        super().paint(painter, option, w)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionHasChanged and self.scene():
            self.nodeChanged.emit()

        return super().itemChange(change, value)
    
    def mousePressEvent(self, e):
        self.nodeSelected.emit()
        super().mousePressEvent(e)

    def mouseDoubleClickEvent(self, e):
        self.width = self.boundingRect().width()
        self.height = self.boundingRect().height()
        self.nodeEdited.emit()

    def mouseMoveEvent(self, e):
        if not self.father_node:
            diff = QPointF(e.scenePos() - e.lastScenePos())
            self.nodeMoved.emit(diff.x(), diff.y())

    def focusOutEvent(self, e):
        self.nodeLostFocus.emit()