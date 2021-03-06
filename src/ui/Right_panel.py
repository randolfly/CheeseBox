# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'left_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sqlite3
import os


class Right_panel(object):
    def setupUi(self, MainWindow):
        self.dock = QtWidgets.QDockWidget('Tag', MainWindow)
        self.dock.setObjectName("Tag")
        self.dock.resize(200, 800)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.dockWidgetContents)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.button_search = QtWidgets.QPushButton(self.dockWidgetContents)
        self.button_search.setObjectName("button_search")
        self.horizontalLayout.addWidget(self.button_search)
        self.button_addtag = QtWidgets.QPushButton(self.dockWidgetContents)
        self.button_addtag.setObjectName("button_deletetag")
        self.horizontalLayout.addWidget(self.button_addtag)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.dock.setWidget(self.dockWidgetContents)
        self.retranslateUi()
        # menu
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.listWidget.customContextMenuRequested.connect(lambda: self.myListWidgetContext(self.listWidget.pos(),MainWindow))
        self.menu = QtWidgets.QMenu(self.listWidget)
        # self.action_change = QtWidgets.QAction("修改TAG",self.listWidget)
        # self.action_delete = QtWidgets.QAction("删除TAG",self.listWidget)
        # self.menu.addAction(self.action_change)
        # self.menu.addAction(self.action_delete)

        QtCore.QMetaObject.connectSlotsByName(self.dock)
        # slot
        self.button_addtag.clicked.connect(lambda: self.add_tag(MainWindow))
        self.button_search.clicked.connect(lambda: self.search_through_tag(MainWindow))
        MainWindow.addDockWidget(Qt.RightDockWidgetArea, self.dock)

        # sqlite
        # self.create_tag()
        # self.delete_tag()
        # self.show_table()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.dock.setWindowTitle(_translate("DockWidget", "DockWidget"))
        self.button_search.setText(_translate("DockWidget", "搜索TAG"))
        self.button_addtag.setText(_translate("DockWidget", "添加TAG"))

    def create_tag(self):
        conn = sqlite3.connect("tag.db")
        cur = conn.cursor()
        sql_text = '''CREATE TABLE tag 
                   (路径 TEXT, 
                    标签 TEXT);'''
        cur.execute(sql_text)
        conn.commit()
        cur.close()
        conn.close()

    def delete_tag(self):
        conn = sqlite3.connect("tag.db")
        cur = conn.cursor()
        sql_text = "DROP TABLE tag"
        cur.execute(sql_text)
        conn.commit()
        cur.close()
        conn.close()

    def add_tag(self, MainWindow):
        print('add tag selected')
        tag = self.lineEdit.text()
        if (not tag):
            return
        print(tag)
        cur_node = MainWindow.scene.m_activateNode
        if (not cur_node):
            QtWidgets.QMessageBox.Critical(MainWindow, "错误", "未选中节点")
        # TODO:选中空白时 Active Node 应该清除

        path_list = []
        while cur_node:
            # print(cur_node.toPlainText())
            path_list.append(cur_node.toPlainText())
            cur_node = cur_node.parentNode
        print(path_list)
        relative_path = ''
        path_list.reverse()
        for path in path_list:
            relative_path = relative_path + path + os.sep

        conn = sqlite3.connect("tag.db")
        cur = conn.cursor()
        data = (relative_path, tag)
        sql_text = "INSERT INTO tag VALUES" + str(data)
        print(sql_text)
        cur.execute(sql_text)
        conn.commit()
        cur.close()
        conn.close()
        self.updateTag(MainWindow)

    def search_through_tag(self, MainWindow):

        print("search through tag")
        tag = self.lineEdit.text()
        if (not tag):
            return
        conn = sqlite3.connect("tag.db")
        cur = conn.cursor()
        sql_text = "SELECT * FROM tag WHERE 标签='" + str(tag) + "'"
        print(sql_text)
        cur.execute(sql_text)
        result = cur.fetchall()
        self.listWidget.clear()
        for item in result:
            path = item[0]
            print(path)
            path_list = path.split(os.sep)
            print(path_list)
            cur_node = MainWindow.scene.NodeList[0]
            for path_rel in path_list:
                if path_rel != '' and path_rel != '.':
                    for node in cur_node.sonNode:
                        if node.toPlainText() == path_rel:
                            cur_node = node
                            continue

            cur_node.setColor(QColor(Qt.yellow))
            self.listWidget.addItem(path)

        self.listWidget.show()

    def show_table(self):
        conn = sqlite3.connect("tag.db")
        cur = conn.cursor()
        sql_text = "SELECT * FROM tag WHERE 标签='数学'"
        print(sql_text)
        cur.execute(sql_text)
        result = cur.fetchall()
        print(result)
        for item in result:
            self.listWidget.addItem(item[0])
        self.listWidget.show()

    def updateTag(self, MainWindow):
        self.listWidget.clear()
        print("press")
        cur_node = MainWindow.scene.m_activateNode
        if not cur_node:
            return

        path_list = []
        while cur_node:
            # print(cur_node.toPlainText())
            path_list.append(cur_node.toPlainText())
            cur_node = cur_node.parentNode
        print(path_list)
        relative_path = ''
        path_list.reverse()
        for path in path_list:
            relative_path = relative_path + path + os.sep

        conn = sqlite3.connect("tag.db")
        cur = conn.cursor()
        sql_text = "SELECT * FROM tag WHERE 路径="+repr(relative_path)
        print(sql_text)
        cur.execute(sql_text)
        result = cur.fetchall()
        print(result)
        for item in result:
            self.listWidget.addItem(item[1])
        self.listWidget.show()

    def myListWidgetContext(self,position,MainWindow):
        #弹出菜单
        popMenu = QtWidgets.QMenu()
        delAct =QtWidgets.QAction("删除",self.listWidget)
        renameAct =QtWidgets.QAction('修改', self.listWidget)
        #查看右键时是否在item上面,如果不在.就不显示删除和修改.
        if self.listWidget.itemAt(position):
            popMenu.addAction(delAct)
            popMenu.addAction(renameAct)

        renameAct.triggered.connect(lambda: self.rename_item(MainWindow))
        delAct.triggered.connect(lambda: self.delete_item(MainWindow))
        popMenu.exec_(self.listWidget.mapToGlobal(position))

    def rename_item(self,MainWindow):
        curRow = self.listWidget.currentRow()
        item = self.listWidget.item(curRow)
        curtag = item.text()
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.listWidget.editItem(item)
        self.listWidget.itemChanged.connect(lambda: self.change_item(MainWindow, curtag, curRow, item.text()))
    def delete_item(self, MainWindow):
        item = self.listWidget.item(self.listWidget.currentRow())
        tag = item.text()
        cur_node = MainWindow.scene.m_activateNode
        if not cur_node:
            return

        path_list = []
        while cur_node:
            # print(cur_node.toPlainText())
            path_list.append(cur_node.toPlainText())
            cur_node = cur_node.parentNode
        print(path_list)
        relative_path = ''
        path_list.reverse()
        for path in path_list:
            relative_path = relative_path + path + os.sep

        conn = sqlite3.connect("tag.db")
        cur = conn.cursor()
        sql_text = "DELETE FROM tag WHERE 路径=" + repr(relative_path)+" AND 标签="+ repr(tag)
        cur.execute(sql_text)
        conn.commit()
        cur.close()
        conn.close()
        self.updateTag(MainWindow)

    def change_item(self, MainWindow, tag, curRow, curtag):
        print("change")
        print(curtag)
        print(tag)
        cur_node = MainWindow.scene.m_activateNode
        if not cur_node:
            return

        path_list = []
        while cur_node:
            # print(cur_node.toPlainText())
            path_list.append(cur_node.toPlainText())
            cur_node = cur_node.parentNode
        print(path_list)
        relative_path = ''
        path_list.reverse()
        for path in path_list:
            relative_path = relative_path + path + os.sep

        conn = sqlite3.connect("tag.db")
        cur = conn.cursor()
        sql_text = "DELETE FROM tag WHERE 路径=" + repr(relative_path) + " AND 标签=" + repr(tag)
        cur.execute(sql_text)
        conn.commit()
        cur.close()
        conn.close()
        conn = sqlite3.connect("tag.db")
        cur = conn.cursor()
        data = (relative_path, curtag)
        sql_text = "INSERT INTO tag VALUES" + str(data)
        print(sql_text)
        cur.execute(sql_text)
        conn.commit()
        cur.close()
        conn.close()









