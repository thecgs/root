"""
http协议和Chrome抓包工具
http协议：超文本传输协议，是一种发布和接收HTML页面的方法。服务器端口号是80端端口。
https协议:在HTTP下加入了ssl层。服务器端口是443端口。

"""
f = open('test.txt', 'w')
f.write('hello world')
d = f.readline()
print(d)
f.close()


f = open('test.txt')
d = f.readlines()
print(d)
f.close()

old_name = input('请输入文件名：')
index = old_name.rfind('.')
new_name = old_name[:index] + '[备份]' + old_name[index:]
old_f = open(old_name,'rb')
new_f = open(new_name,'wb')
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        break
    new_f.write(con)
old_f.close()
new_f.close()


import os
os.getcwd()
os.listdir(os.getcwd())
os.mkdir('测试')

import os
import random
num = random.randint(0,9)
for i in num:
    os.mkdir(f'文件夹{i}')

os.rmdir(f'文件夹{random.randint(0,9)}')

import os
flag = 1
dir_name = os.getcwd()
file_list = os.listdir(dir_name)
print(file_list)
for name in file_list:
    if flag == 1:
        new_name = 'python-' + name
    elif flag == 2:
        num = len('python-')
        new_name = name[num:]

