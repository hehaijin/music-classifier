from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
import numpy as np
import pywt
import sys
import csv
import os
np.seterr(divide='ignore', invalid='ignore')

csvfile = open("training3.csv", 'wb')
output = csv.writer(csvfile)

data = []
label = []
# output3.csv: raw data from .au file
csvfile = open("output3.csv", 'rb')
csvreader = csv.reader(csvfile)

for row in csvreader:
	row = np.array(row)
	row1 = row[:-1].astype(float)
	# discrete wavelet transform the data
	(cA, cD) = pywt.dwt(row1,'haar')
	data.append(abs(cA)[:1000])
	label.append(row[-1])

data = np.asarray(data)
data = np.nan_to_num(data)
# data = normalize(data)

# use PCA to select the top 50 features
pca = PCA(n_components=50)
data = pca.fit_transform(data);

for i in range(len(label)):
	output.writerow(np.append(data[i],label[i]))