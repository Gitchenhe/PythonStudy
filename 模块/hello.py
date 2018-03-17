# 编写一个模考
# !/usr/bin/env python
# -*- coding: utf-8 -*-

'这是文档的注释'
__author__ = '陈贺'

import sys  # 导入sys模块


# 导入sys模块之后,我们就有了变量sys指向该模块,利用sys这个变量,就可以访问sys模块的所有功能
# sys模块有一个argv变量,用list存储了命令行的所有参数. argv至少有一个元素,因为第一个参数永远是该.py文件的名称,例如
# 运行python hello.py 获得的sys,argv 就是['hello.py']

def test():
    args = sys.argv
    print('args = ',args)
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print("hello,%s" % args[1])
    else:
        print("too many arguments!")

# 当我们在命令行运行hello模块文件时,Python解释器把一个特殊变量 __name__置为__main__,而如果在其它地方导入该hello模块时,if判断将失败,因此,这种if测试可以让一个
# 模块通过命令运行时,执行一些额外的代码,最常见的就是运行测试
if __name__ == '__main__':
    test()


    # 分析
    # 第2行是标准注释,为了程序能在Unix/Linux/Mac上运行,第3行注释表示.py文件本身使用标准UTF-8编码;
    # 第五行是一个字符串,表示文档的注释,任何模块代码的第一个字符串都被视为模块的文档注释
    # 第六行使用'__author__'变量把作者写进去,这样公开源代码的时候,读者就能知道作者的信息
    # 以上就是Python模块的标准文件模版,当然可以全部删掉不用,但是,按照标准办事肯定没错.