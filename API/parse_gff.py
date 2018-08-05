#!/usr/bin/python
import sys
import re

gff = sys.argv[1]
file = open(gff,'r')
print "\t".join(("Ensembl_Gene_ID","Gene_Name"))

for line in file.readlines():
	line = line.strip("\n")
	line_match = re.match(r"^#",line)
	if line_match:
		continue
	line_col = line.split("\t")
	if line_col[2] == 'gene':
		# attibute column
		attr = line_col[8]
		attr_list = attr.split(";")
		gene_id = attr_list[1]
		gene_name = attr_list[4]
		gene_type = attr_list[2]
		gene_status = attr_list[3]
		# split gene_id and gene_name value
		gene_id_list = gene_id.split("=")
		gene_name_list = gene_name.split("=")
		gene_type_list = gene_type.split("=")
		gene_status_list = gene_status.split("=")
		# gene_id and gene_name
		gene_id_value = gene_id_list[1]
		gene_name_value = gene_name_list[1]
		gene_type_value = gene_type_list[1]
		gene_status_value = gene_status_list[1]
		#print "\t".join((gene_id_value,gene_name_value,gene_type_value,gene_status_value))
		print "\t".join((gene_id_value,gene_name_value))

	




