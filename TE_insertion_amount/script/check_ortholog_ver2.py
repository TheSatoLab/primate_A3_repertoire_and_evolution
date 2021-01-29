#!/usr/bin/env python

import sys
argvs = sys.argv

original_f = open(argvs[1])
liftover_dir = argvs[2]

genome_l = ["PanTro6","GorGor5","PonAbe3","NomLeu3","ChlSab1","MacFas5","RheMac8","PapAnu2","CalJac3","SaiBol1","TarSyr1","MicMur1","OtoGar1","Mm10","CavPor3","SpeTri2","OryCun2","TupBel1"]


original_ERV_d = {}
for line in original_f:
  line = line.strip().split()
  start = int(line[1])
  end = int(line[2])
  ERV = line[3]
  length = end - start
  if ERV not in original_ERV_d:
    original_ERV_d[ERV] = 0
  original_ERV_d[ERV] += length

orhtolog_d = {}
for ERV in original_ERV_d:
  orhtolog_d[ERV] = []


for genome in genome_l:
  liftover_f_name = liftover_dir + "hg19_hg19To%s.over.chain.bed" % genome
  liftover_f = open(liftover_f_name)

  liftover_ERV_l = []
  for line in liftover_f:
    ERV = line.strip().split()[3]
    liftover_ERV_l.append(ERV)

  liftover_ERV_s = set(liftover_ERV_l)

  for ERV in original_ERV_d:
    ortholog = 0
    if ERV in liftover_ERV_s:
      ortholog = 1
    orhtolog_d[ERV].append(ortholog)



print "ERV_locus\tlength\tInsertion_date\t" + "\t".join(genome_l)

for ERV in orhtolog_d:
  all_l = orhtolog_d[ERV]

  primate = sum(all_l[:13])
  haplorhini = sum(all_l[:11])
  simiformes = sum(all_l[:10])
  catarrhini = sum(all_l[:8])
  hominoidea = sum(all_l[:4])
  hominidae = sum(all_l[:3])

  not_primate = sum(all_l[13:])
  not_haplorhini = sum(all_l[11:])
  not_simiformes = sum(all_l[10:])
  not_catarrhini = sum(all_l[8:])
  not_hominoidea = sum(all_l[4:])
  not_hominidae = sum(all_l[3:])

  
  insertion_date = "NA"
  if (not_hominidae == 0):
    insertion_date = "After_Hominidae"
  elif (not_hominoidea == 0):
    insertion_date = "Hominoidea"
  elif (not_catarrhini == 0):
    insertion_date = "Catarrhini"
  elif (not_simiformes == 0):
    insertion_date = "Simiformes"
  elif (not_haplorhini == 0):
    insertion_date = "Haplorhini"
  elif (not_primate == 0):
    insertion_date = "Primate"
  elif (not_primate > 0):
    insertion_date = "Before_Primate"
  length = original_ERV_d[ERV]
  res_l = [ERV,length,insertion_date] + all_l
  print "\t".join([str(c) for c in res_l])
