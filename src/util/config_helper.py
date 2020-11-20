#!/usr/bin/env python
# coding=utf-8
#
# Author       : randolf
# Date         : 2020-11-20 20:01:21
# LastEditors  : randolf
# LastEditTime : 2020-11-20 20:52:12
# FilePath     : \CatInBox\src\util\config_helper.py
#


class ConfigHelper():
    """处理软件系统设置相关的文件存储与读取类
    """

    def __init__(self, config_path, username, password, system_root_path):
        """初始化ConfigHelper类

        Args:
            config_path (String): 存储配置文件的绝对路径
            username (String): 登录网络学堂的用户名
            password (String): 登录网络学堂的密码
            system_root_path (Dict): 软件中文件系统对应的地址字典，文件系统名字为键，文件系统根目录绝对路径为值
        """
        
    def data_load(self):
        """从本地的配置文件加载数据
        """
        
    def data_write(self):
        """向给定的配置文件地址写入数据
        """
    
    def get_username(self):
        """获取网络学堂的的用户名
        """
    
    def get_password(self):
        """获取网络学堂的的密码
        """
        
    def get_root_path(self):
        """获取软件中文件系统对应的地址字典，文件系统名字为键，文件系统根目录绝对路径为值
        """
