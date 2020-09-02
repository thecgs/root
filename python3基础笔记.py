# 单行：输出 hello world
print("hello world")
print("hello python")  # 简单注释内容

# 单行注释
""""
第一行注释
第二行注释
第三行注释
"""

#语法： 变量=值
"""
标识符规则
1.由数字、字母、下划线组成
2.不能数字开头
3.不能使用内置关键词
False None True and as assert break class
continue def del elif else except finally for
from global if import in is lambda nonlocal
not or pass raise return try while with yield
4.严格区分大小写
命名习惯
1.见名知义
2.大驼峰：即每一个单词字母都大写，例如：MyName
3.小驼峰：第二个（含）以后的单词首字母大写，例如：myName
4.下划线：例如：my_name
"""

""""
1.定义变量
2.使用变量
3.看变量的特点
"""
# 定义变量:储存数据 TOM
my_name ='TOM'
print(my_name)

#定义变量：储存数据 黑马程序员
schoolName = '我是黑马程序员，我爱python'
print(schoolName)

""" 
数据类型
1.数值：int(整型) float(浮点型)
2.布尔型 True False
3.str （字符串）
4.list（列表）
5.tuple（元组）
6.set（集合）
7.dict（字典）
"""
num1 = 1
num2 = 1.1
print(type(num1))
print(type(num2))

b = True
print(type(b))

c = [10,20,30]
print(type(c))

d = (10,20,30)
print(type(d))

e = {10,20,30}
print(type(e))

f = {'name':'Tom','age':18}
print(type(f))
print(f)

#格式化输出
"""
格式符号    转换
%s         字符串
%d         有符号的十进制整数
%f         浮点数
%c         字符
%u         无符号的十进制整数
%o         八进制整数
%x         十六进制整数（小写ox）
%X         十六进制整数（大写OX）
%e         科学计数法（小写e）
%E         科学计数法（大写E）
%g         %f和%e的简写
%G         %f和%E的简写
"""
age = 18
name = 'TOM'
weight = 75.5
stu_id = 1

print('今年我的年龄是%d岁' % age)
print('我的名字是%s' % name)
print('我的体重是%.2f' % weight)
print('我的学号是%010d' % stu_id)
print('我的名字是%s,今年%d岁了' % (name,age))
print('我的名字是%s,明年%d岁了,体重公斤%.1f,学号是%03d' % (name,age+1,weight,stu_id))
print('今年我的年龄是%s岁,我的名字是%s,我的体重是%s' % (age,name,weight))
print(f'今年我的年龄是{age}岁,我的名字是{name },我的体重是{weight}')  #f'{表达式}'   是python3.6的特性

#转义字符
#\n 换行
#\t 制表符，一个tab键（4个空格）的距离

print('hello')
print('world')
print('hello\nworld')
print('\tabcd')

#结束符
#print('输出的内容',end ="\n")
#在python中 ，print（），默认自带end="\n"这个换行结束符，所以导致每两个print直接会换行展示，用户可以按需求更改结束符。

print('hello',end="\n")
print('world',end="\t")
print('hello',end="...")
print('python')

#输入
#input("提示信息")
#输入的特点
#1.当程序执行到input，等待用户输入，输入完成之后才继续向下执行。
#2.在python中，input接受用户输入后，一般存储到变量，方便使用。
#3.在python中，input会把接受到的任意用户输入的数据都当做字符串处理。

passwd = input('请输入您的密码：')
print(f'您输入的密码是{passwd}')
print(type(passwd))

#转换数据类型的函数
"""
函数                            说明
int(x[,base])                  将x转换为一个整数
float(x)                       将X转换为一个浮点数
complex(real[,imag])           创建一个复数，real为实部，imag为虚部
str(x)                         将对象X转换为字符串
repr(x)                        将对象X转换为表达式字符串
eval(str)                      用来计算在字符串中的有效python表达式，并返回一个对象
tuple(s)                       将序列S转换为一个元组
list(s)                        将序列S转换为一个列表
chr(x)                         将一个整数转换为一个Unicode字符
ord(d)                         将一个字符转换为它的ASCII整数值
hex()                          将一个整数转换为一个十六进制字符串

"""
num3 = input('请输入数字')
print(type(num3))   #str
print(type(int(num3)))  #int

num4 = 1
str1 = '10'
print(type(float(num4)))
print(float(num4))
print(float(str1))

print(type(str(num4)))

list1 = [10,20,30]
print(tuple(list1))

t1 = (100,200,300)
print(list(t1))

str2 = '1'
str3 = '1.1'
str4 = '(1000,2000,3000)'
str5 = '[1000,2000,3000]'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))

#运算符
#分类：算数运算符、赋值运算符、复合赋值运算符、比较运算符、逻辑运算符

"""
1.算术运算符

运算符     描述           实例
+          加            1+1 输出结果为2
-          减            1-1 输出结果为0
*          乘            2*2 输出结果为4
/          除            10/2 输出结果为5
//         整除          9//4 输出结果为2
%          取余          9%4 输出结果为1
**         指数          2**4 输出结果为16
()         小括号         小括号用来提高运算优先级，即（1+2）*3输出结果为9

"""
"""
2.赋值运算符

单个变量赋值
num = 1
print(num)

多个变量赋值
num1, float,str1 = 10,0.5,'hello world'

多个变量赋相同值
a=b=10
print(a)
print(b)

"""
"""
3.复合赋值运算符

运算符     描述                实例
+=        加法赋值运算符       c+=a 等价于 c=c+a
-=        减法赋值运算符       c-=a 等价于 c=c-a
*=        乘法赋值运算符       c*=a 等价于 c=c*a
/=        除法赋值运算符       c/=a 等价于 c=c/a
//=       整除赋值运算符       c//=a 等价于 c=c//a
%=        取余赋值运算符       c%=a 等价于 c=c%a
**=       幂赋值运算符         c**=a 等价于 c=c**a
"""
"""
4.比较运算符

运算符     描述                实例
==        判断相等             如a=3，b=3，则（a==b）为True
!=        不等于               如a=1，b=3，则（a!=b）为True
>         大于                 如a=7，b=3，则（a>b）为True  如a=7，b=3，则（a<b）为False
<         小于                 如a=7，b=3，则（a<b）为True 如a=7，b=3，则（a>b）为False
>=        大于等于             如a=3，b=3，则（a>=b）为True
<=        小于等于             如a=3，b=3，则（a<=b）为True
"""
"""
5.逻辑运算符

运算符  逻辑表达式    描述   
and     x and y     布尔"与"：如果x为False，x and y 返回Flase,否则它返回y的值。
or      x or y      布尔"或"：如果x为True，它返回True,否则它返回y的值。
not     not x       布尔"非"：如果x为True，返回False。如果x为Flase,它返回True。

#习惯用法
a = 1
b = 2
c = 3
print((a < b) and (b < c))    #True
print((a > b) and (b < c))    #False
print((a > b) or (b < c))     #True
print(not (a > b))            #True

#数字之间的逻辑运算
# and 运算符，只要有一个值为0，则结果为0，否则结果为最后一个非0数字
# or 运算符，只有所有值为0结果才为0，否则结果为第一个非0数字
"""

"""
条件判断 if语法:
 if 条件:
     条件成立执行的代码1
     ......
 elif 条件:
      条件成立执行的代码1
      ......
......
 else:
     条件不成立执行代码1
     ......
 
"""
#网吧上网
if True:
    print('条件成立执行的代码1')
    print('条件成立执行的代码2')

age = int(input('输入你的年龄：'))
if age >= 18:
    print('允许上网')
else:
    print('不允许上网')
print('系统关闭')

#工龄判断
age = int(input('请输入你的年龄：'))
if age < 18:
    print('童工，不合法')
elif 18 <= age <= 60:
    print('合法工龄')
else:
    print('退休年龄')

#if 嵌套
#坐公交
money = int(input('请输入"1"或"0":'))
seat = int(input('请输入"1"或"0":'))
if money == 1:
    print('上车')
    if seat == 1:
        print('可以坐下')
    else:
        print('无空坐，站着')
else:
    print('不能上车')

#猜拳游戏
player = int(input('请出拳：0==石头；1==剪刀；2==布'))
import random
computer = random.randint(0,2)
if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')

#三目运算符
#语法：条件成立执行的表达式if条件else条件不成立执行得表达式
a = 1
b = 2
c = a if a > b else b
print(c)

aa = 10
bb = 6
cc = aa - bb if aa > bb else bb - aa
print(cc)

#while循环
"""
while语法：
while 条件:
    条件成立重复执行的代码1
    条件成立重复执行的代码1
    ......

"""
#打印5次
i = 1
while i <= 5:
    print('媳妇儿，我错了')
    i += 1
#计数器习惯书写
i = 0
while i < 5:
    print('媳妇儿，我错了')
    i += 1

#1-100数字累加
i = 1
result = 0
while i <= 100:
    result = result + i
    i = i + 1
print(result)

#1-100偶数累加
#方法一：
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result = result + i
    i = i + 1
print(result)
#方法二：
i = 0
result = 0
while i <= 100:
    result = result + i
    i = i + 2
print(result)

#break 终止循环
i = 1
while i <= 5:
    if i == 4:
        print('吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1
#continue 退出当前一次循环续而执行下一次循环代码
i = 1
while i <= 5:
    if i == 3:
        print('有虫子，不吃了')
        i +=1
        continue
    print(f'吃了第{i}个苹果')
    i += 1

#while循环嵌套
day = 1
while day <= 3:
    i = 1
    while i <= 3:
        print('媳妇儿，我错了')
        i += 1
    print('刷晚饭的碗')
    print('一套惩罚结束----------')
    day += 1

#矩形*****
j = 0
while j < 5:
    #一行星星开始
    i = 0
    while i < 5:
        print('*', end='')
        i += 1
    #一行星星结束：换行显示下一行
     print()
    j += 1
#阶梯*****
j = 0
while j < 5:
    #一行星星开始
    i = 0
    while i <= j:
        print('*', end='')
        i += 1
    #一行星星结束：换行显示下一行
     print()
    j += 1

#乘法表达式
j = 1
while j <= 9:
    i = 1
    while i <= j:
        print(f'{i} * {j} = {i*j}',end='\t')
        i += 1
    print()
    j += 1

#for循环
"""
for循环语法：
for临时变量in序列;
   重复执行的代码1
   重复执行的代码2
......
"""

#案例一
str = 'ithemachenxuyuan'
for i in str:
    print(i)
#break for ... in ...
str = 'ithemachenxuyuan'
for i in str:
    if i == 'e':
        break
    print(i)
#continue for ... in ...
str = 'ithemachenxuyuan'
for i in str:
    if i == 'e':
        continue
    print(i)

# while ... else
"""
语法：
while 条件：
    条件成立重复执行的代码
else:
    循环正常结束之后要执行的代码
"""
#案例一
i = 1
while i <= 5:
    print('媳妇儿，我错了')
    i += 1
else:
    print('媳妇儿原谅我了...')

#案例三
i = 1
while i <= 5:
    if i == 3:
        i += 1
        print('这遍说的不真诚')
        continue
    print('媳妇儿，我错了')
    i += 1
else:
    print('我原谅你了')

#for...else
#案例一
str1 = 'itheima'
for i in str1 :
    print(i)
else:
    print('代码执行结束')
#案例二
str1 = 'itheima'
for i in str1:
    if i == "e":
        break
    print(i)
#案例三
str1 = 'itheima'
for i in str1:
    if i == "e":
        continue
    print(i)


#字符串

#单引号
a = 'hello world'
print(a)
print(type(a))

#三引号
e ='''i am tom'''
print(type(e))

f = """i am tom"""
print(type(f))

c = "i'm tom"
print(c)
print(type(c))

d = 'i\'m tom'
print(d)
print(type(d))

#字符串输出
name = 'TOM'
print('我的名字是%s' % name)
print(f'我的名字是{name}')

#字符串输入
password = input('请输入您的密码：')
print(f'你输入的密码是{password}')
print(type(password))

#下标or索引
str1 = 'abcdefg'
print(str1)
#数据在程序运行过程中储存在内存
#？得到数字a字符，得到数据b字符-- 使用字符串中某个特定的数据
#这些字符数据从0开始顺序分配一个编号-- 使用这个编号精确找到某个字符数据-- 下标或索引或索引值
str1 = 'abcdefg'
print(str1[0])
print(str1[1])
print(str1[2])

#切片
#语法：序列[开始位置下标：结束位置下标:步长]
str1 = 'abcdefg'
print(str1[1:3])

str = '0123456789'
print(str [2:5:1])
print(str [2:5:2])
print(str [:5])
print(str [5:])
print(str [:])
print(str [::-1])#倒序
print(str [-4:-1])
print(str [-4:-1:1])
print(str [-4:-1:-1])#报错，从-4开始到-1结束，选取方向为从左到右，但是-1步长：从右到左选取，方向不一致，报错。
        #查找!```````
#find
#语法：字符串序列.find（子串，开始位置下标，结束位置下标）
mystr = "hello world and itcast and itheima and python"
print(mystr.find('and'))
print(mystr.find('and',15,30))
print(mystr.find('ands',15,30))#子串不存在，返回-1

#rfind
#语法：字符串序列.rfind（子串，开始位置下标，结束位置下标）
#从右侧开始查找

#index
#语法：字符串序列.index（子串，开始位置下标 ,结束位置下标）
mystr = "hello world and itcast and itheima and python"
print(mystr.index('and'))
print(mystr.index('and',15,30))
print(mystr.index('ands',15,30))#子串不存在，报错

#rindex
#语法：字符串序列.rindex（子串，开始位置下标 ,结束位置下标）
#从右侧开始查找

#count
#语法：字符串序列.count（子串，开始位置下标 ,结束位置下标）
mystr = "hello world and itcast and itheima and python"
print(mystr.count('and'))
print(mystr.count('and',15,30))
print(mystr.count('ands'))#返回0

#修改
#replace 替换
#语法：字符串序列.replace（旧子串，新子串，替换次数）
mystr = "hello world and itcast and itheima and python"
new_str = print(mystr.replace('and','he'))
print(new_str)

#split 按照指定字符分割字符串
#语法:字符串序列.split(分割字符，num)
mystr = "hello world and itcast and itheima and python"
list = mystr.split('and')
print(list)
list = mystr.split('and',2)
print(list)

#join 用一个字符或子串合并字符串，既是将多个字符串合并为一个新的字符串。
#语法：字符串或子串.join(多字符串组成的序列)
mystr = ['aa','bb','cc']
new_str = '...'.join(mystr)
print(new_str)

#大小写转换
#capitalize 将字符串第一个字符转换成大写
mystr = "hello world and itcast and itheima and python"
new_str = mystr.capitalize()
print(new_str)

#title 将字符串每一个单词字母转换成大写
mystr = "hello world and itcast and itheima and python"
new_str = mystr.title()
print(new_str)


#lower 将字符串中大写转小写
mystr = "hello world and itcast and itheima and python"
new_str = mystr.lower()
print(new_str)

#upper 将字符串中的小写转大写
mystr = "hello world and itcast and itheima and python"
new_str = mystr.upper()
print(new_str)

#删除空白字符
#lstrip 删除字符串左侧空白字符
mystr = "     hello world and itcast and itheima and python   "
new_str = mystr.lstrip()
print(new_str)

#rstrip 删除字符串右侧空白字符
mystr = "     hello world and itcast and itheima and python   "
new_str = mystr.rstrip()
print(new_str)

#strip 删除字符串两侧空白字符
mystr = "     hello world and itcast and itheima and python   "
new_str = mystr.strip()
print(new_str)

#字符串对齐
#ljust 返回一个原字符串左对齐，并使用指定字符（默认空格）填充至对应长度的新字符串。
#语法:字符串序列.liust(长度，填充字符)
mystr = 'hello'
print(mystr)
str1 = mystr.ljust(10)
print(str1)
str2 = mystr.ljust(10,'.')
print(str2)

#rjust 返回一个原字符串右对齐，并使用指定字符（默认空格）填充至对应长度的新字符串。
#语法:字符串序列.riust(长度，填充字符)
mystr = 'hello'
print(mystr)
str1 = mystr.rjust(10)
print(str1)
str2 = mystr.rjust(10, '.')
print(str2)

# center返回一个原字符串居中，并使用指定字符（默认空格）填充至对应长度的新字符串。
#语法:字符串序列.center(长度，填充字符)
mystr = 'hello'
print(mystr)
str1 = mystr.center(10)
print(str1)
str2 = mystr.center(10, '.')
print(str2)

#字符串判断
#startwith 检查字符串是否是以指定子串开头，是则返回True，否则返回False。如果设置开始和结束位置的下标，则在指定范围内检查。
#语法：字符串序列.startwith（子串，开始位置下标，结束位置下标）
mystr = "hello world and itcast and itheima and python"
print(mystr.startswith('hell'))

#endwith 检查字符串是否是以指定子串结尾，是则返回True，否则返回False。如果设置开始和结束位置的下标，则在指定范围内检查。
#语法：字符串序列.endwith（子串，开始位置下标，结束位置下标）
mystr = "hello world and itcast and itheima and python"
print(mystr.endswith('thon'))

#isalpha 如果字符串至少有一个字符并且所有字符都是字母则返回Ture，否则返回False。
mystr = "hello world and itcast and itheima and python"
print(mystr.isalpha())#有空格，所以False

#isdigit 如果字符串只包含数字则返回Ture否则返回False。
mystr = "hello world and itcast and itheima and python"
print(mystr.isdigit())

#isalnum 如果字符串至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False。
mystr = "hello world and itcast and itheima and python"
print(mystr.isalnum())

#isspace 如果字符串只包含空白，则返回Ture，否则返回False。
mystr = "hello world and itcast and itheima and python"
print(mystr.isspace())

#列表
#列表的格式
#[数据1，数据2，数据3，数据4......]

#列表的常用操作
#查找
#下标
name_list = ['Tom','Lily','ROSE']
print(name_list[0])
print(name_list[1])

#函数
#index 查找
name_list = ['Tom','Lily','ROSE']
print(name_list.index('Tom'))
print(name_list.index('Toms'))

#count 统计
name_list = ['Tom','Lily','ROSE']
print(name_list.count('Tom'))
print(name_list.count('Toms'))

#len 公共统计
name_list = ['Tom','Lily','ROSE']
print(len(name_list))

#in 判断在/not in 判断不在
name_list = ['Tom','Lily','ROSE']
print('Tom' in name_list)
print('tom' not in name_list)

#案例
name_list = ['Tom','Lily','ROSE']
name = input('请输入您的邮箱账户名：')
if name in name_list:
    print(f'您输入的名字是{name}，此用户已经存在')
else:
    print(f'您输入的名字是{name},注册成功')

#增加
#append 列表结尾追加数据
#语法:列表序列.append(数据)
name_list = ['Tom','Lily','ROSE']
name_list.append('xiaoming')
name_list.append([11,22])
name_list.append(['zhangsan','lisi'])
print(name_list)

#extend 列表结尾追加数据，如果数据是一个序列，则将这个序列的数据注意添加到列表。
#语法：列表序列.extend()数据

name_list = ['Tom','Lily','ROSE']
name_list.extend('xiaoming')
name_list.extend(['xiaoming','xiaohong'])
print(name_list)

#insert 指定位置新增数据
#语法：列表序列.insert(位置下标，数据)
name_list = ['Tom','Lily','ROSE']
name_list.insert(1,'aaa')
name_list.insert(1,[11,22])
print(name_list)

#删除
#del
#语法: del 目标
name_list = ['Tom','Lily','ROSE']
del name_list[0]
#del name_list
del (name_list)
print(name_list)

#pop 删除指定下标的数据（默认为最后一个），并返回该数据。
#语法：列表序列.pop(下标)
name_list = ['Tom','Lily','ROSE']
del_name = name_list.pop()
print(name_list)
print(del_name)

#remove 移除列表中某一个数据的第一个匹配项。
#语法：列表序列.remove(数据)
name_list = ['Tom','Lily','ROSE']
name_list.remove('ROSE')
print(name_list)

#clear 清空列表
name_list = ['Tom','Lily','ROSE']
name_list.clear()
print(name_list)

#修改指定下标的数据
name_list = ['Tom','Lily','ROSE']
name_list [0] = 'aaa'
print(name_list)

#reverse 逆置
list = [1,3,2,5,4,6]
list.reverse()
print(list)

#sort 排序
#语法：列表序列.sort(key=None,reverse=False)
list = [1,3,2,5,4,6]
list.sort()
list.sort(reverse=False)#reverse=False 升序 /reverse=True 降序
print(list)#默认升序

#copy 复制
name_list = ['Tom','Lily','ROSE']
list1 = name_list.copy()
print(name_list)
print(list1)

#列表的循环遍历
#while
name_list = ['Tom','Lily','ROSE']
i=0
while i < len(name_list):
    print(name_list[i])
    i += 1

#for in
name_list = ['Tom','Lily','ROSE']
for i in name_list:
    print(i)

#列表的嵌套使用
name_list = [['小明','小红','小绿'],['Tom','Lily','Rose'],['张三','李四','王五']]
#列表嵌套的时候的数据查询
print(name_list[0])
print(name_list[0][1])

#案例一
import random
teachers = ['A','B','C','D','E','F','G','H']
offices = [[],[],[]]
for name in teachers:
    num = random.randint(0,2)
    offices[num].append(name)
print(offices)
i = 1
for office in offices:
    print(f'办公室{i}的人数是{len(office)}。老师分别是：')
    for name in office:
        print(name)
    i += 1

#元组 元组不支持修改
#定义元组：使用小括号，且逗号隔开各个数据，数据可以是不同的数据类型。
tuple1 = (10,20,30)
print(type(tuple1))
#单个数据的元组
tuple2 = (10,)#逗号不能丢

#按下标查找数据
tuple1 = ('aa','bb','cc','dd')
print(tuple1[0])

#index
tuple1 = ('aa','bb','cc','dd')
print(tuple1.index('bb'))

#conut
tuple1 = ('aa','bb','cc','dd')
print(tuple1.count('aa'))

#len
tuple1 = ('aa','bb','cc','dd')
print(len(tuple1))

#特定的修改
tuple1 = ('aa','bb',['cc','dd'])
tuple1[2][0]='ff'
print(tuple1)

#字典
dict = {'name':'TOM','age':20,'gender':'男'}
print(dict)
print(type(dict))

#增或修
#语法：字典序列[key]=值
dict = {'name':'TOM','age':20,'gender':'男'}
dict['id'] = 110
print(dict)
dict ['name']='Rose'
print(dict)

#删
dict = {'name':'TOM','age':20,'gender':'男'}
del dict['name']
print(dict)
del(dict)
print(dict)

dict1 = {'name':'TOM','age':20,'gender':'男'}
dict1.clear()
print(dict1)

#查
dict = {'name':'TOM','age':20,'gender':'男'}
#[key]查找
print(dict['name'])
print(dict['names'])

#get语法：字典序列.get(key,默认值)
#注意:如果当前查找的key不存在则返回第二个参数（默认值），如果省略第二个参数，则返回None。
dict = {'name':'TOM','age':20,'gender':'男'}
print(dict.get('name'))
print(dict.get('id',110))
print(dict.get('id'))

#keys()
dict = {'name':'TOM','age':20,'gender':'男'}
print(dict.keys())#返回值可遍历，是迭代对象

#values()
dict = {'name':'TOM','age':20,'gender':'男'}
print(dict.values())#返回值可遍历，是迭代对象

#items()
dict = {'name':'TOM','age':20,'gender':'男'}
print(dict.items())#查找字典中所有的键值对，返回可迭代对象，里面的数据是元组

#字典的循环遍历
#遍历字典的key
dict = {'name':'TOM','age':20,'gender':'男'}
for key in dict.keys():
    print(key)

#遍历字典的values()
dict = {'name':'TOM','age':20,'gender':'男'}
for value in dict.values():
    print(value)

#遍历字典items（）
dict = {'name':'TOM','age':20,'gender':'男'}
for item in dict.items():
    print(item)

#遍历字典键值对之拆包
dict = {'name':'TOM','age':20,'gender':'男'}
for key,value in dict1.items():
    print(f'{key} = {value}')

import numpy as np
import pandas as pd
import matplotlib
"""
一元ufunc
"""
#创建数组
list1 = [(-1.23, 12, 0.27, -8)]
arr1 = np.array(list1)
print(arr1)
#整数绝对值
abs1 = np.abs(arr1)
print(abs1)
#复数，浮点数
fabs1 = np.fabs(arr1)
print(fabs1)
#平方根
sqrt1 = np.abs(arr1)
sqrt2 = np.sqrt(sqrt1)
print(sqrt2)
#以e为底的指数
exp1 = np.exp(arr1)
print(exp1)
#log,log10,log2,log1p
data = np.abs(arr1)
log_1 = np.log(data)
log_2 = np.log10(data)
log_3 = np.log2(data)
log_4 = np.log1p(data)
print(log_1), print(log_2), print(log_3), print(log_4)
#计算正负值
sign1 = np.sign(arr1)
print(sign1)
#ceil值，大于等于该值的最小整数
ceil1 = np.ceil(arr1)
print(ceil1)
#floor值，小于等于该值的最小整数
floor1 = np.floor(arr1)
print(floor1)
#rint四舍五入
rint1 = np.rint(arr1)
print(rint1)
#将数组的小数和整数部分以两个独立数组的形式返回
modf1 = np.modf(arr1)
print(modf1)
#返回一个‘哪些值是NaN’的布尔型数组
isnan1 = np.isnan(arr1)
print(isnan1)
#isfinite(哪些数是有穷的),isinf(哪些数是无穷的)
isfinite1 = np.isfinite(arr1)
isinf1 = np.isinf(arr1)
print(isfinite1), print(isinf1)
#cos,cosh,sin,sinh,tan,tanh(普通和双曲型三角函数)

print('---------------------------------------------------------------------------------')
list2 = [(1.23, -12, -0.27, 8), (-2.35, 3.52, 5, -8)]
arr2 = np.array(list2)
print(arr2)












































#文件操作
#打开文件，语法：f = open(name,mode)
f = open('test.txt','w+')
#写，语法：文件对象.write（内容）
f = open('test.txt','w+')
f.write('aaa')
#关闭，语法：文件对象.close()
f = open('test.txt','w+')
f.close()
#读，语法：文件对象.read(num)#nun表示从文件中读取的数据的长度（单位是字节），如果没有传入num，那么就表示读取文件中所有的数据。
f = open('test.txt','r')
print(f.read())
#读，语法:文件对象.readines()#按照行读取，并返回一个列表，每一行的数据为一个元素。
f = open('test.txt')
list = f.readlines()
print(list)
f.close()
#读，语法：文件对象.readline()#一行一行的读，每次读一行。
f = open('test.txt')
list = f.readline()#打印第1行
print(list)
list = f.readline()
print(list)
list = f.readline(5)#打印第3行前5个字符
print(list)
f.close()
#移动文件指针，语法：文件对象.seek(偏移量，起始位置)
"""
起始位置
0：文件开头
1：当前位置
2：文件结尾
"""
#001
f = open('test.txt','r+')
f.seek(2,0)
print(f.read())
#002
f = open('test.txt','a+')
f.seek(0,0)#or write: f.seek(0)
print(f.read())



"""
模式     描述
r        以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb       以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+       打开一个文件用于读写。文件指针将会放在文件的开头。
rb+      以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w        打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
wb       以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
w+       打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不不存在，创建新⽂文件。
wb+      以二进制格式打开一个文件用于读写。如果该文件已存在则打开⽂文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a        打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab       以二进制格式打开一个文件用于追加。如果该文件已存在，⽂文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该⽂文件不存在，创建新文件进行写入。
a+       打开一个文件⽤用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+      以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""

import subprocess
listfile = subprocess.getoutput('cd /home/guisen/IL/; cat HumIL.tblastn')
print(listfile)
