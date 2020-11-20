# -*- coding: utf-8 -*-
# @Author: Randolf
# @Date:   2020-11-06 21:17:20
# @Last Modified by:   Randolf
# @Last Modified time: 2020-11-17 19:16:23

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