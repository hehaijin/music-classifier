import csv
import sys
import numpy as np

# the scipts uses 2 parameters, first one is input file, second one is output file.

inputfile=sys.argv[1]
#inputfile='./output.csv'
output=sys.argv[2]

#withlabel=sys.argv[3]

data=[]
labels=[]
with open(inputfile) as csvfile:
		trainreader = csv.reader(csvfile)
		for row in trainreader:
			#For testing files without "class", use line 17 and comment line 18-20
			#data.append(row)
			l=len(row)
			data.append(row[0:l-1])
			labels.append(row[l-1])
dataarray=np.array(data,dtype='float32')
(h,w)=dataarray.shape

#this is to deal with a special case where the result from mfcc is infinity. 
#not sure how it happened.
for i in range(h):
	for j in range(w):
		if np.isinf(dataarray[i,j]):
			dataarray[i,j]=0
			data[i][j]=0


result=np.zeros((h,w))

ave=np.nanmean(dataarray,axis=0)  #ignore nan. hiphop 36 37 gives nan result
var=np.nanvar(dataarray,axis=0)   #ignore nan 
for i in range(w):
	print ave[i]
	#print var[i]
for i in range(h):
	for j in range(w):
		if var[j]!=0:
			result[i,j]= (dataarray[i,j]-ave[j])/var[j]
		else:
			 result[i,j]= dataarray[i,j]
	
#outfile = open("normalized1.csv", 'wb')
outfile = open(output, 'wb')
outputWriter = csv.writer(outfile)

#adding header column

header=[]
for i in range(w):
	header.append("feature"+str(i))
header.append("genre")
	
outputWriter.writerow(header)

for i in range(h):
	#For testing files, use line 54, comment line 55
	#outputWriter.writerow(np.append(result[i],"?"))
	outputWriter.writerow(np.append(result[i],labels[i]))
