#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""
2021/07/06
author:guisen chen
email:thecgs001@foxmail.com
"""
import re
import argparse
import pandas as pd
from collections import defaultdict

parser = argparse.ArgumentParser(description='将readcounts标准化为FPKM or TPM',usage='python3 readcounts2FPKM_and_TPM.py -r [readcounts] -g [file.gff3]',add_help=False,epilog='date:2021/07/06 author:guisen chen email:thecgs001@foxmail.com')
required = parser.add_argument_group('required arguments')
optional = parser.add_argument_group('optional arguments')
required.add_argument('-r','--readcounts',metavar='[readcounts file]',help='readcounts file',required=True)
required.add_argument('-g','--gff',metavar='[file.gff3]',help='gff3 file',required=True)
optional.add_argument('-h','--help',action='help',help='show this help message and exit')
optional.add_argument('-v','--version',action='version',version='v1.00')
args = parser.parse_args()

exon_length_dict = defaultdict(list)
with open(args.gff,'r') as f:
    for line in f:
        if line.startswith('#') or line == "\n": #remove '#' and '\n'
            continue
        line = line.rstrip().split("\t")
        if line[2] == "exon":
            mrna_id = re.search("Parent=(.*?);",line[8]+";").group(1)
            per_gene_per_exon_length = int(line[4]) - int(line[3]) + 1
            exon_length_dict[mrna_id].append(per_gene_per_exon_length)

exon_length = defaultdict(list)
for gene_id,exon_length_list in exon_length_dict.items():
    count = sum(exon_length_list)
    exon_length[gene_id].append(count)
    
exon_length = pd.DataFrame(exon_length).T.sort_index()
exon_length = exon_length.rename(columns={0:'gene_len'})

read_counts = pd.read_csv(args.readcounts,sep='\t', index_col="gene_id").sort_index()

FPKM_matrix = pd.DataFrame()
for sample_name in read_counts:
    FPKM = read_counts[sample_name]*1000*1000000/(read_counts[sample_name].sum()*exon_length['gene_len'])
    FPKM_matrix[sample_name] = FPKM
#print(FPKM_matrix)

TPM_matrix = pd.DataFrame()
for sample_name in read_counts:
    RPK=read_counts[sample_name]*1000/exon_length['gene_len']
    TPM = RPK*1000000/RPK.sum()
    TPM_matrix[sample_name] = TPM
#print(TPM_matrix)

#exon_length.to_csv('exon_length.xls',sep='\t')
FPKM_matrix.to_csv('FPKM.xls',sep='\t')
TPM_matrix.to_csv('TPM.xls',sep='\t')

print('finished')
