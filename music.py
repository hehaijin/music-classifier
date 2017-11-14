import scipy.io.wavfile as wv
from matplotlib.pyplot import specgram
import soundfile as sf
import scipy
from scikits.talkbox.features import mfcc
import os
import csv
import numpy as np


outfile = open("output.csv", 'wb')
outputWriter = csv.writer(outfile)
outfile2 = open("output2.csv", 'wb')
outputWriter2 = csv.writer(outfile2)
outfile3 = open("output3.csv", 'wb')
outputWriter3 = csv.writer(outfile3)




current, dirs, files = os.walk('./genres/').next()
for dir in dirs:
	current, dirs2, files2 = os.walk('./genres/'+dir).next()
	print dir
	for f in files2:
		if f !='.DS_Store':
			print f
			data, samplerate = sf.read('./genres/'+dir+'/'+f)
			x=abs(scipy.fft(data)[:1000])
			outputWriter.writerow(np.append(x[:1000],dir))
			ceps,mspec,spec=mfcc(data)
			num_ceps=ceps.shape[0]
			y=np.mean(ceps[int(num_ceps/10): int(num_ceps*9/10)],axis=0)
			outputWriter2.writerow(np.append(y,dir))
			# raw data for method 3 normalize3.py
			outputWriter3.writerow(np.append(data,dir))
			












