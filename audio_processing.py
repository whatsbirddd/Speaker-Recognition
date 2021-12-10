import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import soundfile as sf

#audio recording from mic
fs = 8000
seconds = 0.5

myrecording = sd.rec(int(seconds*fs), samplerate=fs, channels =1,dtype='int16')
sd.wait()

#write and save a wave file
write('output2.wav', fs, myrecording)

#load speech data by reading the wave file

filename = 'output2.wav'
data, fs = sf.read(filename)  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing


