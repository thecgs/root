#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import subprocess

with open(sys.argv[1], 'r') as f:
    for id in f:
        id = str(id.strip())
        add = 'http://rest.kegg.jp/get/'+id+'/aaseq'
        cline = subprocess.Popen(f'wget -c {add} -O {id}',env = None,shell=True)
        cline.wait()

