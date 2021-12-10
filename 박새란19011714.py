import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import soundfile as sf

#audio recording from mic
fs = 8000

seconds = 16

#load speech data by reading the wave file

filename = 'output2.wav'
data, fs = sf.read(filename)  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing