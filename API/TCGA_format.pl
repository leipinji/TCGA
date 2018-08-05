#!/usr/bin/perl
# File name : TCGA_format.pl
#Author: Lei Pinji
#Mail: LPJ@whu.edu.cn
###############################
use warnings;
use strict;
use Cwd;
use Getopt::Long;

my $help;

GetOptions (	
		'help'	=> \$help
		);

if (defined $help) {
	print<<EOF;
	Usage:	$0	>	<output>
	Description:
	######################################
	transfer TCGA file to standard foramt for next step analysis
	TCGA file	<UN*>
	Ensembl_Gene_ID	sample1	sample2	sample3	sample4	...(FPKM)
	######################################
EOF
exit(0);
}

my $current_work_dir = cwd();

my %gene_name;
my @gene_name_order = ();
my @file_name = <*FPKM.txt>;

for (@file_name) {
	my $tmp_file = $_;
	open my $input_fh, "<", $tmp_file or die;
	while (<$input_fh>) {
		chomp;
		my @tmp = split/\t/;
       	my $fpkm = $tmp[1];
		my $geneSymbol = $tmp[0];
		$gene_name{$geneSymbol}{$tmp_file} = $fpkm;
		}
	close $input_fh;
	}

my @new_file_name = <*FPKM.txt>;

my @TCGA_file_name = ();
for (@new_file_name){
	my $TCGA_file = "TCGA-".$_;
	push @TCGA_file_name, $TCGA_file;
}

@gene_name_order = sort {$a cmp $b} keys %gene_name;

print join("\t","Ensembl_Gene_ID",@TCGA_file_name),"\n";

for my $gene (@gene_name_order) {
	my @value = ();
	for my $file (@new_file_name) {
		my $fpkm_each_file = $gene_name{$gene}{$file};
		push @value, $fpkm_each_file;
	}
	print join("\t",$gene,@value),"\n";
}

