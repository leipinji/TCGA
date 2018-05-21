#!/usr/bin/python
import sys
import re

input_file = sys.argv[1]
input_file_fh = open(input_file,'r')
title = input_file_fh.readline()

for line in input_file_fh.readlines():
	line = line.strip("\n")

	line_list = line.split("\t")
	sample_type = line_list[0]
	file_name = line_list[2]
	tumor_stage = line_list[5]

	file_name_list = file_name.split("-")
	file_name_list.insert(0,"TCGA")
	file_name_string = ".".join(file_name_list)

	file_match = re.match(r".*.FPKM.txt.gz",file_name_string)
	if (file_match):
		file_name_string = re.sub(r".txt.gz",".txt",file_name_string)
		print "\t".join((file_name_string,sample_type,tumor_stage))


