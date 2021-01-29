#!/usr/bin/env python

import sys,re

argvs = sys.argv

min_len = 0

f = open(argvs[1])
Class_of_interest = argvs[2]

for i in range(3):
  f.next()

for line in f:
  line = line.strip()
  line = re.sub(r'\s+',' ',line)
  line = line.split(" ")
  score = line[0]
  chrm,start,end = line[4:7]
  Id = line[14]
  start = str(int(start)-1)
  strand = line[8]
  span = int(end) - int(start)
  if strand == "C":
    strand = "-"
  Type,Class = line[9:11]
  if '/' in Class:
    Class = Class.split('/')[1]
  if (Class == Class_of_interest) and (span > min_len):
    name = Type + "|" + Id
    print "\t".join([str(c) for c in [chrm,start,end,name,score,strand]])
