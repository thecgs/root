#!/usr/bin/env python3
# coding: utf-8

"""
2020/11/17
author:guisen chen
email:thecgs001@foxmail.com
"""

import re
from Bio import SeqIO

match_seq = [] # result list

record = SeqIO.read("/home/guisen/test.fasta","fasta") # read seq_file
temp = re.compile("GT",re.I).finditer(str(record.seq)) # re_str "GT" 

pos_list = [] # macth position_list
for i in temp:
    pos_list.append(i.span())

i = 0
while i < len(pos_list) - 1:
    if pos_list[i+1][0] - pos_list[i][0] <= 8: # longest 10bp seq
        match_seq.append((str(record.seq)[pos_list[i][0]:int(pos_list[i+1][0])+2])) # print match seq
    i += 1

print(len(match_seq))
print(match_seq)
