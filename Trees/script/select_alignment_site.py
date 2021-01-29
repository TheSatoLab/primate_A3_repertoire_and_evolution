#!/usr/bin/env python

import sys
argvs = sys.argv

aligned_fasta_f = open(argvs[1])
out_f_prefix = argvs[2]
min_prop_site_covarage = float(argvs[3])
min_prop_aligned_seq = float(argvs[4])

seq_d = {}
for line in aligned_fasta_f:
  line = line.strip()
  if '>' in line:
    name = line.replace('>','')
    seq_d[name] = ''
  else:
    seq = line
    seq_d[name] = seq_d[name] + seq

seq_len = len(seq_d[name])
seq_num = len(seq_d)
thresh_min_site_covarage = seq_num * min_prop_site_covarage

pos_count_l = [0] * seq_len
for name in seq_d:
  seq = seq_d[name].lower()
  for i in range(seq_len):
    if seq[i] in ['a','t','g','c']:
      pos_count_l[i] += 1

selected_pos_l = [i for i in range(seq_len) if pos_count_l[i] > thresh_min_site_covarage]

seq_selected_pos_len = len(selected_pos_l)
thresh_aligned_seq_len = seq_selected_pos_len * min_prop_aligned_seq


seq_all_pos_out_f_name = out_f_prefix + '_seq_all_pos.fas'
seq_selected_pos_out_f_name = out_f_prefix + '_seq_selected_pos.fas'

seq_all_pos_out_f = open(seq_all_pos_out_f_name,"w")
seq_selected_pos_out_f = open(seq_selected_pos_out_f_name,"w")


for name in seq_d:
  seq = seq_d[name]
  seq_without_gap = seq.replace('-','')
  seq_selected_pos = "".join([seq[i] for i in range(seq_len) if i in selected_pos_l])
  aligned_seq_len = len([c for c in seq_selected_pos.lower() if c in ['a','t','g','c']])
  if aligned_seq_len > thresh_aligned_seq_len:
    print >> seq_all_pos_out_f, ">" + name + "\n" + seq_without_gap
    print >> seq_selected_pos_out_f, ">" + name + "\n" + seq_selected_pos

