import os
 
import win32api
import win32com
import win32print
from win32com.client import Dispatch
abs_path = os.path.abspath(__file__)
abs_path=abs_path.replace("a.py","")
# --------------------------------------------------------
# -- 需要修改的参数
# --------------------------------------------------------
# 获取当前工作目录(仅在测试中使用，具体使用可以注释掉，并修改open_file为要打开的word文档地址即可)
path = abs_path + r'my.docx'
# 要打开的文件
open_file = path
 
 
# 方法一，通过命令行的方式进行打印
def printer_loading(filename):
    open(filename, "r")
    win32api.ShellExecute(
        0,
        "print",
        filename,
        '/d:"%s"' % win32print.GetDefaultPrinter(),
        ".",
        0
    )
 
 

 
 
# 方法一调用并进行打印
