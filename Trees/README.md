# Trees
* Each directory (except for **script**) contains the following subdirectories:
  * **MSA_original**: contains the original sequence fasta (without alignment, trimming, and filtering)
  * **MSA_aligned_filtered**: contains the multiple sequence alignment fasta file used for the tree construction. The the alignment sites with low site-coverage were excluded. The sequences with too-many gapped sites were excluded.
  * **nwk**: contains the newick format tree file.

* **script/select_alignment_site.py**: a script to filter the alignment sites with low site-coverage and the sequences with too-many gapped sites. This program is for nucleotide seuqences.
  * **Requirements:**
    * Python2 (version 2.75)
  * **Usage:**
    * python script/select\_alignment\_site.py **<input file (aligned fasta)>** **<output file prefix>** **<minimum site coverage>** **<minimum proportion of the  non-gapped sites>**
  * **Output:**
    * **<prefix>_seq\_all\_pos.fas**: without removing the alignment sites with low site-coverage
    * **<prefix>_seq\_selected\_pos.fas**: with removing the alignment sites with low site-coverage