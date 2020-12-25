import sys
import os
from os import path

src_path =  path.dirname(path.dirname(path.abspath(__file__)))
util_path =  path.join(src_path, 'util')
pipe_path =  path.join(src_path, 'pipes')

sys.path.append(src_path)
sys.path.append(util_path)
sys.path.append(pipe_path)

from file_tree import FileTree
from file_node import FileNode
from pipe import Pipe
from net_helper import NetHelper


class NetPipe(Pipe):
    
    def __init__(self,username, password, file_system_destination, file_system_root_path):
        """管道派生类，给定清华网络学堂的用户名，密码等，给定管道相关的存储位置(是网络的)
        
        NetPipe主要功能在于read & write, 对于网络的文件系统简单的进行读写操作。

        Args:
            username (String): 网络学堂的学号(暂时支持清华学堂)
            pass (String): 网络学堂的密码(暂时支持清华学堂)
            file_system_destination (String): 管道出口(本地)的存储路径，可以用来备份文件树等等(write)
            file_system_root_path (String): 管道入口(本地)的需要读操作的根目录，可以用来生成顶层文件树(read)
        """
        Pipe.__init__(self,file_system_destination,file_system_root_path)
        # 计数节点数目
        self.item_number = 0
        #! 注意，默认获取本学期的文件系统，可以之后进行修改
        #TODO: 实际上应该给NetPipe定义一个用户属性类，方便进行初始化操作，这里为了简单直接进行控制
        self.username = username
        self.password = password
        self.net_handler = NetHelper(username, password)

    def read_file_system(self, user_semester_list):
        """给定扫描文件系统的学期，扫描出一个文件树

        Args:
            user_semester_list (List[String]): 用户学期
        
        Returns:
            file_tree (FileTree): 对应的文件树
        """
        #TODO: 这里学期应该定义一个enum，方便用户输入，为了方便...
        # 参考学期:['2017-2018-1', '2017-2018-2', '2017-2018-3', '2018-2019-1', '2018-2019-2', '2018-2019-3', '2019-2020-1', '2019-2020-2', '2019-2020-3', '2020-2021-1', '2020-2021-2']
        ideal_list = ['2017-2018-1', '2017-2018-2', '2017-2018-3', '2018-2019-1', '2018-2019-2', '2018-2019-3', '2019-2020-1', '2019-2020-2', '2019-2020-3', '2020-2021-1', '2020-2021-2']
        for semester in user_semester_list:
            if semester not in ideal_list:
                print('Wrong semester!')
                return None
        self.net_handler.get_courses(user_semester_list)
        root_node = self.net_handler.get_course_file_tree_node()
        src_path = self.file_system_root_path
        file_tree = FileTree(root_node, src_path)
        
        return file_tree

if __name__ == '__main__':
    net_pipe = NetPipe(username, password ,os.getcwd(), path.dirname(os.getcwd()))
    file_tree = net_pipe.read_file_system(['2018-2019-1','2018-2019-1', '2019-2020-1'])
    file_tree.print_tree()