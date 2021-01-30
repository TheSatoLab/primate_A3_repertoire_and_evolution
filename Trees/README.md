# Trees
* Each directory (except for script) contains the following subdirectories:
* **MSA_original**: contains the original sequence fasta (without alignment, trimming, and filtering)
* **MSA_aligned_filtered**: contains the multiple sequence alignment fasta file used for the tree construction. The the alignment sites with low site-coverage were excluded. The sequences with too-many gapped sites were excluded.
* **nwk**: contains the newick format tree file.
* **script/select_alignment_site.py**: a script to filter the alignment sites with low site-coverage and the sequences with too-many gapped sites.