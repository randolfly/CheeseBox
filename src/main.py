from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import sys
from os import path

src_path =  path.dirname(path.abspath(__file__))
util_path =  path.join(src_path, 'util')
pipe_path =  path.join(src_path, 'pipe')
ui_path =  path.join(src_path, 'ui')

sys.path.append(src_path)
sys.path.append(util_path)
sys.path.append(pipe_path)
sys.path.append(ui_path)

from file_tree import FileTree
from file_node import FileNode
from file_pipe import FilePipe
from mainwindow import MainWindow
from Component import *
from main_panel import Ui_MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('MyXind')

    settings = QSettings(SETTINGS_PATH, QSettings.IniFormat)
    if not settings.value('lastpath'):
        settings.setValue('lastpath', [])

    window = MainWindow(settings)
    # window = Ui_MainWindow()
    
    # NoteWindow = Note()
    # LinkWindow = Link()
    # 测试
    file_pipe = FilePipe(os.getcwd(), (os.getcwd()))
    print(os.getcwd())
    print('=='*10)
    
    file_tree = file_pipe.read_file_system()
    file_tree.print_tree()
    print('=='*10)
    # print_all_path(file_tree.root_node)
    print('item total number of this file tree: ', file_pipe.item_number)
    
    window.show_file_tree(file_tree)
    
    # window.addNote.connect(NoteWindow.handle_addnote)
    # window.close_signal.connect(NoteWindow.handle_close)
    # window.scene.press_close.connect(NoteWindow.handle_close)

    # NoteWindow.note.connect(window.getNote)
    # NoteWindow.noteChange.connect(window.contentChanged)

    # window.addLink.connect(LinkWindow.handle_addLink)
    # window.close_signal.connect(LinkWindow.handle_close)
    # window.scene.press_close.connect(LinkWindow.handle_close)

    # LinkWindow.link.connect(window.getLink)
    # LinkWindow.linkChange.connect(window.contentChanged)

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()