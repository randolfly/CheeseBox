 # ref:https://www.jb51.net/article/183904.htm
 # ref:https://docs.qameta.io/allure/#_pytest

import pytest
import allure

@allure.step('加法操作')
def add(x):
    return x + 2;

@allure.step("步骤1:点xxx")
def step_1():
    print("111")

@allure.step("步骤2:点xxx")
def step_2():
    print("222")

@allure.feature('熟悉框架功能')# 用feature说明产品需求
class TestClass(object):
    @allure.story('测试加法') # 用story说明用户场景
    def test_add(self):
        assert add(2) == 4

    @allure.story('测试包含') # 用story说明用户场景
    def test_in(self):
        a = 'hello world'
        b = 'he'
        step_1()
        
        assert b in a

    @allure.story('测试不包含') # 用story说明用户场景
    def test_not_in(self):
        a = 'Hello'
        b = 'hi'
        step_2()
        assert b not in a

import os

if __name__=="__main__":

    #生成测试报告json

    pytest.main(["-s", "-q", '--alluredir', 'report/result', 'test_sample.py'])

    #将测试报告转为html格式

    split='allure '+'generate '+'./report/result '+'-o '+'./report/html '+'--clean'

    os.system('cd ./report')

    os.system(split)

    print(split)