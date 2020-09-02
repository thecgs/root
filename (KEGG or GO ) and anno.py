""""
2019/10/29
陈桂森
用于 KEGG or GO 的注释结果文档中 gene id 与 注释文档的注释信息拼接
"""

a = input('请输入KEGG or GO文件名(包括拓展名)：')
b = input('请输入基因注释文件：')
f = open(a, 'a+')
f1 = open(b, 'a+')
f2 = open('result.xls', 'a+')
f1.seek(0)
f1_list = f1.readlines()
f.seek(0)
f.readline()
"""
准备阶段：输入文档的读取，以及结果文档的建立
"""

j = int(input('请输入基因集行数：'))
"""
Bug:暂时采用手动输入的方案(原方案：j = len(f.readlines()))
"""
print(f)
i = 1
while i <= j:
    str1 = f.readline()
    i += 1
    f_num = str1.find('evm.model')
    str2 = str1[f_num:]
    if 'merg' == a[-4:]:
        list1 = str2.split(',')
    else:
        list1 = str2.split(' ')
        """
        提取gene id
        """
    list1[len(list1)-1] = list1[len(list1)-1][0:len(list1[len(list1)-1])-1]
    """
    去掉最后一个gene id 的换行符
    """

    for gene in list1:
        f1_num = [x for i, x in enumerate(f1_list) if x.find(f'{gene}') != -1]
        all1 = str1[:f_num] + f1_num[0]
        """
        以gene id 查询注释文档的注释信息，及结果信息的拼接 
        """

        f2.write(all1)
        print(all1)
        """
        储存及显示结果
        """
"""
版权声明：
遵循
CC
4.0
BY - SA
版权协议
"""