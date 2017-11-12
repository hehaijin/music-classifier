
import os
import csv
import numpy as np

outfile = open("testfilename.csv", 'w')
outputWriter = csv.writer(outfile) 


path = "./validate/"
dirs = os.listdir(path)
for f in dirs:
	if f !='.DS_Store':
		print(f)
		r=list()
		r.append(f)
		outputWriter.writerow(r)
		
