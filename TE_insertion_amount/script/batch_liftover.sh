#!/usr/bin/env bash

#liftover=<PATH to liftover>
#liftover_chain_dir=<PATH to the directory containing liftover chain file>

mkdir liftovered_bed

#Convert RepeatMakser out file to bed file with extracting L1
python script/rmOut2bed.TE_family.py \
       GCA_000001405.1_hg19_genomic.fna.out \
       L1 \
       > GCA_000001405.1_hg19_genomic.fna.L1.bed

#Execute LiftOver
cat script/list_liftover_chain_file.txt | while read f; do
  #L1
  ${liftover} \
  GCA_000001405.1_hg19_genomic.fna.L1.bed \
  ${liftover_chain_dir}/${f} \
  liftovered_bed/hg19_${f}.bed \
  /dev/null \
  -minMatch=0.5
done

#estimate insertion date from ortholog distribution
python script/check_ortholog_ver2.py \
       GCA_000001405.1_hg19_genomic.fna.L1.bed \
       liftovered_bed/ \
       > estimated_insertion_dates.L1.txt

