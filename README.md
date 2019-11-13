Python3统计代码行小工具

# Python3统计代码行小工具
## 初衷：
之前使用过一个工具统计Java的代码行数，工具不支持Python，就正好使用Python简单实现一下

## 输入选项：
 1. **code_path为输入需要检测的代码目录比如** E:\code\python\LinesCount
 2. **ode_type为需要统计的文件的后缀**比如 .py
## 输出选项：
最终的输出就为当前的目录下的所有的.py文件的统计的总行数、注释行数、除去空白行和注释行之后的行数
## 效果图
CSDN链接: [link](https://blog.csdn.net/zhangvalue/article/details/103053805).
![Alt](https://img-blog.csdnimg.cn/20191113174944771.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYW5ndmFsdWU=,size_16,color_FFFFFF,t_70)
## 具体思路
思路：
具体的逻辑就是通过python的os.path() 模块的一些方法
在判断是不是文件夹，如果是文件夹就会进去递归访问，直到找到所有文件目录，并将所有的文件目录都存到fileList。

在每一次访问文件的时候，通过os.path.splitext(f_path)[1]
方法取到文件后缀，和输入的文件类型匹配成功就开始进入文件中，进行判断是否为空行或者#开头的注释行，进而进行判断是否为空白行、注释行，最终统计出来数据，打印出来。


