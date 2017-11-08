import scipy.io.wavfile as wv
from matplotlib.pyplot import specgram
import soundfile as sf
import scipy
from scikits.talkbox.features import mfcc
import os
import csv
import numpy as np

outfile = open("testing1.csv", 'wb')
outputWriter = csv.writer(outfile) 
outfile2 = open("testing2.csv", 'wb')
outputWriter2 = csv.writer(outfile2)

path = "./testing/"
dirs = os.listdir(path)
for f in dirs:
	if f !='.DS_Store':
		data, samplerate = sf.read(path+f)
		x=abs(scipy.fft(data)[:1000])
		outputWriter.writerow(x[:1000])
		ceps,mspec,spec=mfcc(data)
		num_ceps=ceps.shape[0]
		y=np.mean(ceps[int(num_ceps/10): int(num_ceps*9/10)],axis=0)
		outputWriter2.writerow(y)
