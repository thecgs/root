#!/usr/bin/env python3
# coding: utf-8

"""
2020/10/09
author:guisen chen
email:thecgs001@foxmail.com
"""

import re
import sys
import csv
from collections import defaultdict

def parse_gff(file_gff):
    
    gene_ID_dict = defaultdict(list) # all mRNA id corresponding to gene id 
    ID_info_dict = defaultdict(list) # info of gene, mRNA, CDS and exon
    CDS_length_dict = defaultdict(list) # all CDS length corresponding to mRNA id 
    the_longest_mRNA_ID_dict = defaultdict(str)
    
    for line in open(file_gff,'r'):
        
        if line.startswith('#') or line == "\n": #remove '#' and '\n'
            continue
        line_list = line.split("\t")
        
        if line_list[2] == "gene": 
            gene_ID = re.search("ID=(.*?);",line_list[8]).group(1).strip()
            ID_info_dict[gene_ID] = line_list[0:8] + [f'ID={gene_ID};']
        
        if line_list[2] == "mRNA" or line_list[2] == "transcript": 
            mRNA_ID = re.search("ID=(.*?);",line_list[8]).group(1)
            gene_ID = re.search("Parent=(.*?);",line_list[8]).group(1).strip()
            if gene_ID in gene_ID_dict:
                gene_ID_dict[gene_ID].append(mRNA_ID)
            else:
                gene_ID_dict[gene_ID] = [mRNA_ID]
            ID_info_dict[mRNA_ID].append(line_list[0:8] + [f'ID={mRNA_ID};Parent={gene_ID};'])
            
        if line_list[2] == "CDS": 
            CDS_ID = re.search("ID=(.*?);",line_list[8]).group(1)
            mRNA_ID = re.search("Parent=(.*?);",line_list[8]).group(1).strip()
            ID_info_dict[mRNA_ID].append(line_list[0:8] + [f'ID={CDS_ID};Parent={mRNA_ID};'])
            CDS_length = int(line_list[4]) - int(line_list[3]) + 1
            CDS_length_dict[mRNA_ID].append(CDS_length)
        
        if line_list[2] == "exon":
            exon_ID = re.search("ID=(.*?);",line_list[8]).group(1)
            mRNA_ID = re.search("Parent=(.*?);",line_list[8]).group(1).strip()
            ID_info_dict[mRNA_ID].append(line_list[0:8] + [f'ID={exon_ID};Parent={mRNA_ID};'])
    
    for gene_ID,mRNA_ID_list in gene_ID_dict.items():
        i = 0
        for mRNA_ID in mRNA_ID_list:
            CDS_length = sum(CDS_length_dict[mRNA_ID])
            if CDS_length > i:
                i = CDS_length
                the_longest_mRNA_ID_dict[gene_ID] = mRNA_ID
    
    gff_file = open('./the_longest_transcription.gff','a')
    gff = csv.writer(gff_file,delimiter='\t')
    for gene_ID, mRNA_ID in the_longest_mRNA_ID_dict.items():
        for line in ([ID_info_dict[gene_ID]]+ID_info_dict[mRNA_ID]):
            gff.writerow(line)
    gff_file.close()
    return print('--------finished--------')

parse_gff(sys.argv[1])
