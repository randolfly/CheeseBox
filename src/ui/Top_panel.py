# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from os import path
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import os
import sys
from os import path

src_path =  path.dirname(path.dirname(path.abspath(__file__)))
util_path =  path.join(src_path, 'util')
pipe_path =  path.join(src_path, 'pipes')
ui_path =  path.join(src_path, 'ui')

sys.path.append(src_path)
sys.path.append(util_path)
sys.path.append(pipe_path)
sys.path.append(ui_path)

from file_tree import FileTree
from file_node import FileNode
from file_pipe import FilePipe
from net_pipe import NetPipe


class Top_panel(object):
    def setupUi(self, MainWindow):
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 26))
        self.menubar.setObjectName("menubar")
        self.menu_1 = QtWidgets.QMenu(self.menubar)
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.action2_sub = QtWidgets.QAction(MainWindow)
        self.action2_sub.setObjectName("action2_sub")
        self.action2_after = QtWidgets.QAction(MainWindow)
        self.action2_after.setObjectName("action2_after")
        self.action2_cut = QtWidgets.QAction(MainWindow)
        self.action2_cut.setObjectName("action2_cut")
        self.action2_copy = QtWidgets.QAction(MainWindow)
        self.action2_copy.setObjectName("action2_copy")
        self.action2_paste = QtWidgets.QAction(MainWindow)
        self.action2_paste.setObjectName("action2_paste")
        self.action3_project = QtWidgets.QAction(MainWindow)
        self.action3_project.setObjectName("action3_project")
        self.action3_version = QtWidgets.QAction(MainWindow)
        self.action3_version.setObjectName("action3_version")
        self.action4_drawingsetting = QtWidgets.QAction(MainWindow)
        self.action4_drawingsetting.setObjectName("action4_drawingsetting")
        self.action4_displaysetting = QtWidgets.QAction(MainWindow)
        self.action4_displaysetting.setObjectName("action4_displaysetting")
        self.action1_new = QtWidgets.QAction(MainWindow)
        self.action1_new.setObjectName("action1_new")
        self.action1_open = QtWidgets.QAction(MainWindow)
        self.action1_open.setObjectName("action1_open")
        self.action1_save = QtWidgets.QAction(MainWindow)
        self.action1_save.setObjectName("action1_save")
        self.action1_delete = QtWidgets.QAction(MainWindow)
        self.action1_delete.setObjectName("action1_delete")
        self.action2_delete = QtWidgets.QAction(MainWindow)
        self.action2_delete.setObjectName("action2_delete")
        self.action2_print = QtWidgets.QAction(MainWindow)
        self.action2_print.setObjectName("action2_print")
        self.action2_quit = QtWidgets.QAction(MainWindow)
        self.action2_quit.setObjectName("action2_quit")
        self.menu_1.addAction(self.action1_new)
        self.menu_1.addAction(self.action1_open)
        self.menu_1.addAction(self.action1_save)
        self.menu_1.addAction(self.action1_delete)
        self.menu_2.addAction(self.action2_sub)
        self.menu_2.addAction(self.action2_after)
        self.menu_2.addAction(self.action2_cut)
        self.menu_2.addAction(self.action2_copy)
        self.menu_2.addAction(self.action2_paste)
        self.menu_2.addAction(self.action2_delete)
        self.menu_2.addAction(self.action2_print)
        self.menu_2.addAction(self.action2_quit)
        self.menu_4.addAction(self.action4_drawingsetting)
        self.menu_4.addAction(self.action4_displaysetting)
        self.menu_3.addAction(self.action3_project)
        self.menu_3.addAction(self.action3_version)
        self.menubar.addAction(self.menu_1.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu_1.setTitle(_translate("MainWindow", "文件系统"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_4.setTitle(_translate("MainWindow", "设置"))
        self.menu_3.setTitle(_translate("MainWindow", "说明"))
        self.action2_sub.setText(_translate("MainWindow", "子节点"))
        self.action2_after.setText(_translate("MainWindow", "并列节点"))
        self.action2_cut.setText(_translate("MainWindow", "剪切"))
        self.action2_copy.setText(_translate("MainWindow", "复制"))
        self.action2_paste.setText(_translate("MainWindow", "粘贴"))
        self.action3_project.setText(_translate("MainWindow", "项目说明"))
        self.action3_version.setText(_translate("MainWindow", "版本说明"))
        self.action4_drawingsetting.setText(_translate("MainWindow", "绘图设置"))
        self.action4_displaysetting.setText(_translate("MainWindow", "显示设置"))
        self.action1_new.setText(_translate("MainWindow", "新建"))
        self.action1_open.setText(_translate("MainWindow", "打开"))
        self.action1_save.setText(_translate("MainWindow", "保存"))
        self.action1_delete.setText(_translate("MainWindow", "删除"))
        self.action2_delete.setText(_translate("MainWindow", "删除"))
        self.action2_print.setText(_translate("MainWindow", "打印"))
        self.action2_quit.setText(_translate("MainWindow", "退出"))

        # slot
        self.action1_delete.triggered.connect(self.slot1)
        self.action1_new.triggered.connect(self.slot1)
        self.action1_save.triggered.connect(MainWindow.file_saveas)
        self.action1_open.triggered.connect(lambda: self.open(MainWindow))
        self.action2_sub.triggered.connect(MainWindow.scene.addSonNode)
        self.action2_after.triggered.connect(MainWindow.scene.addSiblingNode)
        self.action2_cut.triggered.connect(MainWindow.scene.cut)
        self.action2_copy.triggered.connect(MainWindow.scene.copy)
        self.action2_paste.triggered.connect(MainWindow.scene.paste)
        self.action2_delete.triggered.connect(MainWindow.scene.removeNode)
        self.action2_print.triggered.connect(MainWindow.file_print)
        self.action2_quit.triggered.connect(MainWindow.quit)
        self.action3_project.triggered.connect(self.slot1)
        self.action3_version.triggered.connect(self.slot1)
        self.action4_drawingsetting.triggered.connect(self.slot1)
        self.action4_displaysetting.triggered.connect(self.slot1)

    def slot1(self):
        print("slot test")

    def open(self, MainWindow):
        MainWindow.renew()
        reply = QtWidgets.QMessageBox.question(MainWindow,"文件系统选择","选择本地文件系统？",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            file_path = QtWidgets.QFileDialog.getExistingDirectory(MainWindow, "选择文件夹", "./")
            # print(file_path)
            file_pipe = FilePipe(os.getcwd(), file_path)
            # print(os.getcwd())
            # print('=='*10)

            file_tree = file_pipe.read_file_system()
            MainWindow.show_file_tree(file_tree)
            # file_tree.print_tree()
        else:
            user, u_ok = QInputDialog.getText(MainWindow, "网络学堂登陆", "用户名")
            password, p_ok = QInputDialog.getText(MainWindow, "网络学堂登陆", "密码")
            # print(user,password,u_ok,p_ok)
            if u_ok and p_ok:
                net_pipe = NetPipe(user, password ,os.getcwd(), (os.getcwd()))
                file_tree = net_pipe.read_file_system(['2019-2020-1'])
                MainWindow.show_file_tree(file_tree)



