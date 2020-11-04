## Code Style

- 变量命名

  采用下划线命名,变量名字母全部小写，各个单词之间用下划线隔开。所有单词**不允许**缩写

  举例： ~~x_pos_stream~~(单词缩写了，应为:x_position_stream

  此外，变量中不要出现无意义的名称,比如 x_location_data 中 data 无意义，应该删去。

  变量中单词组合时，名词放在动词前面，比如: user_login, file_save;

  变量中名词只出现单数，比如 file_save 而不是~~files_save~~

  注意：这里面**get, set**单独成类，比如有 get_data()

- 类命名

  - 首字母大写

- 避免命名

  - 单独的字母，除了某些特定允许的情况：

    - 用于计数(i,j,k,v...)
    - 用于 try/catch 中断(e)
    - 用于 file handle(f)

      总之建议不要用这么简单的单字母作为名字，对于简单程序还好，对于长的程序会出现误解

  - 避免在任何包名/类名使用 dash(-)
  - 双下划线(\_\_)
  - offensive terms

- 命名实例

| Type                       | Public             | Internal                         |
| -------------------------- | ------------------ | -------------------------------- |
| Packages                   | lower_with_under   |                                  |
| Modules                    | lower_with_under   | \_lower_with_under               |
| Classes                    | CapWords           | \_Capwords                       |
| Exceptions                 | CapWords           |
| Functions                  | lower_with_under() | \_lower_with_under()             |
| Global/Class Constants     | CAPS_WITH_UNDER    | \_CAPS_WITH_UNDER                |
| Global/Class Variables     | lower_with_under   | \_lower_with_under               |
| Instance Variables         | lower_with_under   | \_lower_with_under (protected)   |
| Method Names               | lower_with_under() | \_lower_with_under() (protected) |
| Function/Method Parameters | lower_with_under   |                                  |
| Local Variables            | lower_with_under   |                                  |
