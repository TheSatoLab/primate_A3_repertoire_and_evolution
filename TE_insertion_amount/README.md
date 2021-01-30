# TE_insertion_amount
This directory includes the raw data (i.e., the RepeatMasker output) and the programs to estimate the insertion dates of respective TE loci according to the distribution of the orthologous copies among primates and out group species.

# Contents:
* **GCA_000001405.1_hg19_genomic.fna.tar.xz**: RepeatMasker output file for hg19
* **script/**
* **list_liftover_chain_file.txt:** the list of RepeatMasker output file used for the analysis
  * **batch_liftover.sh:** a shell script to run the pipeline (for estimating L1 insertion amounts)
* **rmOut2bed.TE_family.py:** converts RepeatMasker output file with extracting the information of a TE family of interest
* **rmOut2bed.TE_class.py:** converts RepeatMasker output file with extracting the information of a TE class of interest
* **check_ortholog_ver2.py:** estimates the insertion dates of respective TE loci according to the results of LIftOver

## Requirements:
* Python2 (version 2.75)
* UCSC LiftOver program (https://genome-store.ucsc.edu/)
* The LiftOver chain files listed in the **script/list_liftover_chain_file.txt** (http://hgdownload.soe.ucsc.edu/goldenPath/hg19/liftOver/)