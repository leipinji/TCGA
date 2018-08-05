#!/usr/bin/python
# File name : ANOVA.py
#Author: Lei Pinji
#Mail: LPJ@whu.edu.cn
################################
from scipy import stats
import numpy as np
import sys
import math
# normal sample
normal_file = sys.argv[1]
# cancer sample
cancer_file = sys.argv[2]

normal_fh = open(normal_file, 'r')
cancer_fh = open(cancer_file, 'r')
normal_hash = {}
cancer_hash = {}

normal_headline = normal_fh.readline()
normal_headline = normal_headline.strip("\n")
normal_col_list = normal_headline.split("\t")
#normal_col_list.pop(0)

cancer_headline = cancer_fh.readline()
cancer_headline = cancer_headline.strip("\n")
cancer_col_list = cancer_headline.split("\t")
#cancer_col_list.pop(0)

title = normal_col_list + cancer_col_list
title.insert(0,"Gene_Name")

print "\t".join(title)

normal_len = 0
cancer_len = 0
for line in normal_fh.readlines():
    line = line.strip('\n')
    tmp = line.split("\t")
    normal_len = len(tmp) - 1
    gene_name = tmp[0]
    fpkm = tmp[1:]
    normal_hash[gene_name] = fpkm


for line in cancer_fh.readlines():
    line = line.strip('\n')
    tmp = line.split("\t")
    cancer_len = len(tmp) - 1
    gene_name = tmp[0]
    fpkm = tmp[1:]
    cancer_hash[gene_name] = fpkm
	
#print "\t".join(("#","normal sample length",str(normal_len)))
#print "\t".join(("#","cancer sample length",str(cancer_len)))

up_file = open('up_regulated_genes.txt','w')
down_file = open('down_regulated_genes.txt','w')

output_title = "Gene_Name\tNormal\tTumor\tfoldChange\n"
up_file.write(output_title)
down_file.write(output_title)

for key in cancer_hash:
    nor = map(float,normal_hash[key])
    can = map(float,cancer_hash[key])
    nor_array = np.array(nor)
    can_array = np.array(can)
    
    nor_array_mean = np.average(nor)
    cancer_array_mean = np.average(can)
    foldChange = math.log((cancer_array_mean+0.001)/(nor_array_mean+0.001),2)

    fpkm = nor+can
    fpkm_max = max(fpkm)
    
    f,p = stats.f_oneway(nor_array,can_array)
    if (p <= 0.001 and (foldChange >= 2 or foldChange <= -2) and fpkm_max >= 5 ):
		nor.insert(0,key)
		nor.extend(can)
		print "\t".join(map(str,nor))
		
		output_list = [key,(nor_array_mean+0.001),(cancer_array_mean+0.001),foldChange,"\n"]
		
		if (foldChange >= 2):
			up_file.write("\t".join(map(str,output_list)))
		if (foldChange <= -2):
			down_file.write("\t".join(map(str,output_list)))

normal_fh.close()
cancer_fh.close()



