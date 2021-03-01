#! /usr/bin/env python

import sys, os, re

def convert(lines):
	with open('AUGUSTUS.gff3', 'w') as out:
		for line in lines:
			each = line.strip().split()
			if each[2] == 'gene':
				out.write('\t'.join(each) + '\n')
			elif each[2] == 'mRNA':
				mrna = line.strip().split()
				out.write('\t'.join(each) + '\n')
				n = 0
			elif each[2] == 'CDS':
				n += 1
				line = each.copy()
				each[2] = 'exon'
				each[7] = '.'
				id = re.search(r'ID=(.*?);', mrna[8]).group(1) + '.exon' + str(n)
				each[8] = 'ID=' + id + ';' + 'Parent=' + re.search(r'ID=(.*?);', mrna[8]).group(1)
				out.write('\t'.join(each) + '\n')
				out.write('\t'.join(line) + '\n')


def main():
	with open(sys.argv[1], 'r') as inputfile:
		convert(inputfile)

if __name__ == '__main__':
	main()
