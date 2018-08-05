#!/usr/bin/Rscript
suppressMessages(library(optparse))
options=OptionParser()
options=add_option(options,
                    opt_str = c('-R','--reference'),
                    action = 'store',
                    type = 'character',
                    help = 'ensembl ID to HGNC gene symbol')

options=add_option(options,
                    opt_str = c('-F','--fpkm'),
                    action = 'store',
                    type = 'character',
                    help = 'fpkm value matrix from TCGA')
options=add_option(options,
                    opt_str = c('-o','--output'),
                    action = 'store',
                    type = 'character',
                    help = 'output file name')
options=parse_args(options)

genelist<-read.table(file=options$reference,header = T,sep = "\t")
fpkm<-read.table(file = options$fpkm,header = T,sep="\t")
# merged fpkm with HGNC geneSymbol
merged_fpkm<-merge(x = genelist,y = fpkm,by.x='Ensembl_Gene_ID',by.y='Ensembl_Gene_ID')
group<-as.vector(merged_fpkm$Gene_Name)
merged_fpkm<-merged_fpkm[,c(3:length(merged_fpkm[1,]))]
merged_fpkm_sum<-rowsum(merged_fpkm,group = group,reorder = T)
group_order<-sort(unique(group))
rownames(merged_fpkm_sum)<-group_order
write.table(merged_fpkm_sum,file = options$output,col.names = T,row.names = T,sep = "\t",quote = F,na = 'NA')
