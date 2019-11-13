# *===================================*
# -*- coding: utf-8 -*-
# * Time : 2019/11/13 15:58
# * Author : zhangsf
# *===================================*
import os
import os.path

def count_code(path, key, fileList):
    #返回指定的文件夹包含的文件或文件夹的名字的列表
    for f in os.listdir(path):
        #把目录和文件名合成一个路径
        f_path = os.path.join(path, f)
        #判断路径是否为目录
        if os.path.isdir(f_path):
            #如果当前路径是目录就会递归调用这个方法
            count_code(f_path, key, fileList)
        #如果路径是文件并且 进行分割路径，返回路径名和文件扩展名的元组获得的后缀名为目标文件后缀名
        elif os.path.isfile(f_path) and os.path.splitext(f_path)[1] == key:
            #将文件追加到mylist中
            fileList.append(f_path)
            #打开文件进行统计每一个文件
            with open(f_path, 'r', encoding='utf-8') as file:
                #变量表示所有的行数
                file_all_count = 0
                # 变量表示去掉空白行的代码行数
                file_blank_line_count = 0
                #变量表示注释行
                file_comment_line_count=0
                for  line in file:
                    file_all_count += 1
                    #对每一行进行去掉空格之后判断如果为''则表示为空白行
                    if line.strip() == '':
                        file_blank_line_count += 1
                         #如果为#开头表示为注释行
                    if line.strip().startswith('#'):
                        file_comment_line_count+=1
                print(f_path + '----' + '总行数=' + str(file_all_count) +
                    '      注释行=' + str(file_comment_line_count)+
                      '       除去空白和注释行之后=' + str(file_all_count-file_blank_line_count-file_comment_line_count))
#统计所有文件的代码行数
def count_all_code(fileList):
    all_count = 0
    blank_line_count = 0
    comment_line_count=0
    for f_path in fileList:
        with open(f_path, 'r', encoding='utf-8') as file:
            for line in file:
                all_count += 1
                if line.strip() == '':
                    blank_line_count += 1
                # 先去空格在判断如果为#开头表示为注释行
                if line.strip().startswith('#'):
                    comment_line_count += 1
    print('该路径下总行数=' + str(all_count) +
                    '      注释行=' + str(comment_line_count)+ '    空白行=' + str(blank_line_count)+'    除去空白行和注释行=' + str(all_count-blank_line_count-comment_line_count))

if __name__ == '__main__':
    code_path = input("Please enter code path: ")
    code_type=input("Please enter code type: ")
    print("你需要检索的文件夹目录为"+ str(code_path)+"----------------------检索的代码类型" + str(code_type))
    fileList = []
    count_code(code_path,code_type, fileList)
    count_all_code(fileList)