import numpy as np
import csv
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import normalize
from sklearn import svm
np.seterr(divide='ignore', invalid='ignore')

# load training data to train classifier
target = []
data = []
with open('output3.csv', 'rb') as out:
    outfile = csv.reader(out)
    for row in outfile:
        row = np.array(row)
        row1 = row[:-1].astype(float)
        data.append(row1)
        target.append(row[-1])
data = np.array(data)
data = np.nan_to_num(data)
data = normalize(data)
target = np.array(target)

# train classifier
gnb = GaussianNB()
sv = svm.SVC(kernel='linear', C=1, degree=3)
clf = gnb # select classifier
clf.fit(data, target)

# use training data to test classifier
correct = 0;
for i in range(len(target)):
  y_pred = clf.predict([data[i]])
  if (y_pred[0]==target[i]):
      correct+=1
print float(correct)/len(target)

# start classify testing data
data_test = []
name = []
with open('testing5.csv', 'rb') as out:
    outfile = csv.reader(out)
    for row in outfile:
        row = np.array(row)
        row1 = row[:-1].astype(float)
        data_test.append(row1)
        name.append(row[-1])
data_test = np.array(data_test)
data_test = np.nan_to_num(data_test)
data_test = normalize(data_test)
name = np.array(name)
outfile = open("answer.csv", 'wb')
outputWriter = csv.writer(outfile)
outputWriter.writerow(["id","class"])
for i in range(len(data_test)):
  y_pred = clf.predict([data_test[i]])
  outputWriter.writerow([name[i],y_pred[0]])
