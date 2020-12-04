## Test style

> 使用`PyTest`框架


### Reference

1. [PyTest](https://www.jianshu.com/p/f3f13f2e6668)
   1. [参考](https://blog.csdn.net/qq_42610167/article/details/101204066)
2. [allure](https://docs.qameta.io/allure/#_pytest)
   1. [生成html测试报告](https://www.jb51.net/article/183904.htm)
      1. 注意，按照`test_sample.py`生成的报告存在一个问题，直接打开html显示文件一直loading，这是因为html加载js,css是通过相对链接，因此需要创建一个小的服务器打开，这样就行了。
         1. [使用python创建服务器](https://developer.mozilla.org/zh-CN/docs/Learn/Common_questions/set_up_a_local_testing_server)
         2. 因此主要命令：
            1. cd 到test的路径/report/html
            2. python -m http.server 
            3. 此时命令行弹出一个本地链接，应该是http://0.0.0.0:8080/ , 直接用浏览器打开这个链接就ok
            4. 目前看来这个生成的报告比较全面