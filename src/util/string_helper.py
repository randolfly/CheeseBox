#!/usr/bin/env python
# coding=utf-8
# 
# Author       : randolf
# Date         : 2020-11-19 19:47:10
# LastEditors  : randolf
# LastEditTime : 2020-12-04 13:50:17
# FilePath     : /CheeseBox/src/util/string_helper.py
# 



from pypinyin import lazy_pinyin


class StringHelper():
    """辅助操作字符串的类

        提供字符串排序功能等等

        Attributes:

    """

    def __init__(self):
        self.chinese_string_list = ['']

    def chinese_string_sort(self, chinese_string_list):
        """对于中文字符串按照拼音顺序进行排序

        Args:
            chinese_string_list (List[String]): 
                待排序的中文字符串列表

        Returns:
            chinese_string_list_sorted (List[String]): 
                排序后的中文字符串列表
        """
        chinese_string_list_sorted = sorted(
            chinese_string_list, key=lambda x: ''.join(lazy_pinyin(x)))
        # TODO: 写对应的测试
        # 一组排序结果
        # chinese_string_list = ['阿斯顿','太过分','而','234','asa','之日起','Randolf','bvc']
        # 结果: ['234', 'Randolf', 'asa', '阿斯顿', 'bvc', '而', '太过分', '之日起']
        return chinese_string_list_sorted

    def get_string_pinyin(self, string):
        """获取一个字符串的拼音表示字符串
        
        如果是中文，比如'张荣侨'，返回'zhangrongqiao';
        如果是英文或者数字，比如'randolf0210ppp', 返回原值，'randolf0210ppp'
        如果中英文夹杂，返回对应的排列，如'randolf0210张荣侨ppp'，返回值，'randolf0210zhangrongqiaoppp'
        如果含有特殊字符，比如'_'，比如'rand_olf张荣侨ppp', 返回: 'rand_olfzhangrongqiaoppp'

        Args:
            string ([type]): [description]

        Returns:
            [type]: [description]
        """
        return ''.join(lazy_pinyin(string))