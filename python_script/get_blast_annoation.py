#!/usr/bin/env python
# coding: utf-8
"""
2020/11/17
author:guisen chen
email:thecgs001@foxmail.com
"""

import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='将blastp(fmtout 6)的结果与swissprot或nr数据库的注释连接',usage='python3 get_blast_annoation.py -d [database.xls] -b [blast.xls] -o [out.xls]',add_help=False,epilog='date:2021/03/06 author:guisen chen email:thecgs001@foxmail.com')
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('-d','--db',metavar='[database.xls]',help='database file',required=True)
required.add_argument('-b','--blast',metavar='[blast.xls]',help='blast result file',required=True)
required.add_argument('-o','--out',metavar='[out.xls]',help='out file',required=True)
optional.add_argument('-h','--help',action='help',help='show this help message and exit')
optional.add_argument('-v','--version',action='version',version='v1.00')
args = parser.parse_args()

df = pd.read_csv(args.blast,sep='\t',names=['qseqid','sseqid','pident','length','mismatch','gapopen','qstart','qend','sstart','send','evalue','bitscore'])
df0 = df.drop_duplicates('qseqid',keep='first')#union
df1 = pd.read_csv(args.db,sep='\t',names=['sseqid','swissprot_annoation'])
df2 = df0.merge(df1, how='left',on='sseqid')
df2[['qseqid','swissprot_annoation']].to_csv(args.out,sep='\t',index=False,header=False)
print('findished')
