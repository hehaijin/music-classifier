import numpy as np
import csv
import math
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import normalize
from sklearn import svm
from sklearn.metrics import confusion_matrix
np.seterr(divide='ignore', invalid='ignore')
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict


def mynormalize(dataarray,testdata):
	
	(h,w)=dataarray.shape

	removeinfnan(dataarray)		
	result=np.zeros((h,w))
	ave=np.nanmean(dataarray,axis=0)  #ignore nan. hiphop 36 37 gives nan result
	var=np.nanvar(dataarray,axis=0)   #ignore nan 
	for i in range(h):
		for j in range(w):
			if var[j]!=0:
				result[i,j]= (dataarray[i,j]-ave[j])/var[j]
			else:
				 result[i,j]= dataarray[i,j]
	
	h2=testdata.shape[0]
	testresult=np.zeros((h2,w))
	for i in range(h2):
		for j in range(w):		 
			if var[j]!=0:
				testresult[i,j]= (testdata[i,j]-ave[j])/var[j]
			else:
				testresult[i,j]= testdata[i,j]
	return (result,testresult)
	
def removeinfnan(dataarray):
	(h,w)=dataarray.shape
	for i in range(h):
		for j in range(w):
			if np.isinf(dataarray[i,j]) or math.isnan(dataarray[i,j]):
				dataarray[i,j]=0
	return dataarray
	
	
def answergenerate(clf,data,target,testdata,clfname,featurename):
	#feature is the name, like "fft" "mfcc" "dw"
	print clfname+" "+featurename
	clf.fit(data, target)
	correct = 0;
	predict=[]
	for i in range(len(target)):
	  y_pred = clf.predict([data[i]])
	  predict.append(y_pred[0])
	  if (y_pred[0]==target[i]):
		  correct+=1
	print float(correct)/len(target)
	
	scores = cross_val_score(clf, data,target, cv=10)
	print("10 fold Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))
	
	y_pred = cross_val_predict(clf,data,target,cv=10)
	cfmatrix = confusion_matrix(target,y_pred)
	
	
	#cfmatrix=confusion_matrix(target,predict)
	f="./newresults/"+"confusionmatrix_"+clfname+"_"+featurename+".csv"
	outfile = open(f, 'wb')
	outputWriter = csv.writer(outfile)
	for i in range(cfmatrix.shape[0]):
		outputWriter.writerow(cfmatrix[i])
	
	
	
	# start classify testing data
	data_test = []
	name = []
	out=open('list_validation.txt', 'rU')
	outfile = csv.reader(out)
	
	for row in outfile:
		name.append(row[0])
	f="./newresults/"+clfname+"_"+featurename+".csv"
	outfile = open(f, 'wb')
	outputWriter = csv.writer(outfile)
	outputWriter.writerow(["id","class"])
	#print testdata.shape
	for i in range(len(testdata)):
	  y_pred = clf.predict([testdata[i]])
	  outputWriter.writerow([name[i],y_pred[0]])
	
	
	
	
	
	
	


#execution
for i in range(1,4):
	features=["fft","mfcc","dw"]
	trainingfile="training"+str(i)+".csv"
	testingfile="testing"+str(i)+".csv"
	f1 = open(trainingfile, 'rb')
	csvtrainingreader = csv.reader(f1)
	f2 = open(testingfile, 'rb')
	csvtestingreader = csv.reader(f2)
	
	data=[]
	labels=[]
	for row in csvtrainingreader:
		l=len(row)
		data.append(row[0:l-1])
		labels.append(row[l-1])
	data=np.array(data,dtype='float32')
	
	
	testdata=[]
	for row in csvtestingreader:
		l=len(row)
		testdata.append(row[0:l])
	testdata=np.array(testdata,dtype='float32')
	data=removeinfnan(data)
	
	testdata=removeinfnan(testdata)
	
	
	
	#2 normalize methods
	(data,testdata)=mynormalize(data,testdata)
	
	#library normalize
	#data=normalize(data)
	#testdata=normalize(testdata)
	
	target = np.array(labels)
	
	gnb = GaussianNB()
	sv = svm.SVC(kernel='linear', C=1, degree=3)
	
	answergenerate(gnb,data,target,testdata,"gnb",features[i-1])
	answergenerate(sv,data,target,testdata,"svm",features[i-1])	
		
