#!/usr/bin/python
import sys, os,re
files = sys.argv[1]
files_r=open(files,"r")
os.system("mkdir Tumor-FPKM Normal-FPKM Tumor-htseq-count Normal-htseq-count")

for line in files_r.readlines():
	line = line.rstrip()
#	print (line)
	fpkm_match = re.search(r".*FPKM.txt.gz.*",line)
	htseqCount_match = re.search(r".*htseq.counts.gz.*",line)

	if fpkm_match:
		col = line.split("\t")
		sample_type = col[0]
		file_name = col[2]
		file_id = col[7]
		url = "/".join(("https://api.gdc.cancer.gov/data",file_id))

		if (sample_type == "Primary Tumor" or sample_type == "Recurrent Tumor"):
			output_file = "/".join(("Tumor-FPKM",file_name)) 
			command = " ".join(("curl","--output",output_file,url))
			print command
			os.system(command)

		elif (sample_type == "Solid Tissue Normal"):
			output_file = "/".join(("Normal-FPKM",file_name))
			command = " ".join(("curl","--output",output_file,url))
			print command
			os.system(command)
			
	elif htseqCount_match:
		col = line.split("\t")
		sample_type = col[0]
		file_name = col[2]
		file_id = col[7]
		url = "/".join(("https://api.gdc.cancer.gov/data",file_id))

		if (sample_type == "Primary Tumor" or sample_type == "Recurrent Tumor"):
			output_file = "/".join(("Tumor-htseq-count",file_name)) 
			command = " ".join(("curl","--output",output_file,url))
			print command
			os.system(command)

		elif (sample_type == "Solid Tissue Normal"):
			output_file = "/".join(("Normal-htseq-count",file_name))
			command = " ".join(("curl","--output",output_file,url))
			print command
			os.system(command)
			

