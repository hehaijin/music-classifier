import soundfile as sf
import csv
import os

outfile = open("testing.csv", 'wb')
outputWriter = csv.writer(outfile) 

path = "./testing/"
dirs = os.listdir(path)
for f in dirs:
	if f !='.DS_Store':
		data, samplerate = sf.read(path+f)
		outputWriter.writerow(data)