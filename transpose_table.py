#!/usr/bin/env python
# -*- coding: utf-8 -*-

#########################################
# Mini-Tool to transpose a table writte #
# in LeTeX – requires plain table as a  #
# file for input                        #
#                                       #
# (C) 2021 P. Bielefeldt                #
# Licensed as GPLv3 or, at your wish,   #
# a later version of GPL.               #
#########################################

import argparse

parser=argparse.ArgumentParser()
parser.add_argument("in_name", type=str, help="file path")

args = parser.parse_args()
in_name = args.in_name
out_name = args.in_name+"_trans"

table = []
with open(in_name, "r") as in_file:
	for line in in_file:
		line = line.strip() # strip off any trailing whitespace and the end-of-line
		line = line.replace("\\", "") # remove the 'new line' from LaTeX manually
		table.append(line.split("& ")) # todo: might not perfectly preserve empty spaces at begin/end of line


# todo: test all rows have same number of columns

print("table")
for r in table:
	print(r)

transposed = map(list, zip(*table))
print("transposed")
for r in transposed:
	print(r)


out_file = open(out_name, "w") # caution: overwrites file ...
for row in transposed:
	 line = " & ".join(row)
	 line = line+" \\\\ \n"
	 out_file.write(line)

out_file.close()
print("output name is %s" % out_name)
