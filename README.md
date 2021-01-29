# Elucidation of the complicated scenario of primate APOBEC3 gene evolution

## Description
APOBEC3 proteins play pivotal roles in defenses against retroviruses, including HIV-1, as well as retrotransposons. Presumably due to the evolutionary arms race between the hosts and these retroelements, APOBEC3 genes have rapidly evolved in primate lineages through sequence diversification, gene amplification and loss, and gene fusion. Consequently, modern primates possess a unique set or “repertoire” of APOBEC3 genes. The APOBEC3 gene repertoire of humans has been well investigated. There are three types of catalytic domains (Z domain; A3Z1, A3Z2, and A3Z3), 11 Z domains, and 7 independent genes, including 4 genes encoding double Z domains. However, the APOBEC3 gene repertoires of nonhuman primates remain largely unclear. Here, we characterize APOBEC3 gene repertoires among primates and investigated the evolutionary scenario of primate APOBEC3 genes using phylogenetic and comparative genomics approaches. In this study, we systematically reannotated primate A3 genes using the coding sequence (CDS) dataset provided by the RefSeq database. Since the CDS annotation in RefSeq is based on transcriptomic information (i.e., mRNA sequences) as well as genomic information, we can investigate whether respective A3 Z domains are expressed as single- or double-domain-type genes by splicing. Moreover, we examined the prevalence, age, and origin of each A3 gene in primates in depth.

This directory contains:
* **Table_suppl.xlsx** includes the infomation of the identified AID/APOBEC-related genes inprimates.
* **TE_insertion_amount** includes the raw data (i.e., the RepeatMasker output) and script to estimate the insertion dates of respective TE loci according to the distribution of the orthologous copies. 
* **Trees** includes the multiple sequence alignments and the phylogenetic trees constructed in the present study.
  * **/script/select_alignment_site.py** a script to filter the alignment sites with low site-coverage and the sequences with many gapped sites.
  

