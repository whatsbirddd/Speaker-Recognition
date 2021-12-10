import librosa
import librosa.display
import matplotlib.pyplot as plt

file = "output.wav"

y, sr = librosa.load(file, sr=8000)
print(y,sr)
print(len(y))

mfcc1 = librosa.feature.mfcc(y=y,sr=sr,n_mfcc = 12)
mfcc2 = librosa.feature.mfcc(y=y,sr=sr,n_mfcc = 24)

fig,ax = plt.subplots()

img = librosa.display.specshow(mfcc2, x_axis='time', ax=ax)
fig.colorbar(img, ax=ax)
ax.set(title="MFCC_24")
plt.show()