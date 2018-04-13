import os
os.chdir("d:")
print(os.name)#查看当前操作系统的名称。windows平台下返回‘nt’，Linux则返回‘posix’
print(os.environ)#获取系统环境变量
print(os.sep)#当前平台的路径分隔符。在windows下，为‘\’，在POSIX系统中，为‘/’
print(os.getcwd())

