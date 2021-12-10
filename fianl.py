import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import mode

n_mfcc = 24
n_fft =512
train_data = []
train_label = []


target = ["F1","F2","M1","M2"]

#1. 파일은 16000Hz, 16bits, mono, wave 파일임
#2. 파이썬 코드를 이용하여 MFCC 코드를 활용하는데, 입력데이터 y는 512, mfcc 갯수 n은 24로 진행한다. 한개의 파일 당 500개의 프레임으로 분할됨.
for i,t in enumerate(target):
    train_file = "data/"+t+".wav"
    y, sr = librosa.load(train_file, sr=16000) #y=512 sr=16000
    mfcc = librosa.feature.mfcc(y=y,sr=sr,n_mfcc = 24,n_fft=512).T
    #print("mfcc :",mfcc.shape)
    if(len(train_data)==0):
        train_data = mfcc
        train_label = np.full(len(mfcc),i)
    else:
        train_data = np.concatenate((train_data, mfcc), axis = 0)
        train_label = np.concatenate(train_label, np.full(len(mfcc),i))


print("----------------------------")
print(train_data.shape)
print(train_label.shape)
print("----------------------------")

#3. 2번 결과 데이터를 이용하여 GMM 모델을 구축한다. Mixture 갯수는 5로 설정한다.
from sklearn.mixture import GaussianMixture
gmm = GaussianMixture(n_components=5, random_state=42)
gmm.fit(train_data,train_label)

#4. 3번에서 만든 코드를 활용하여 화자인식 테스트 코드를 만든다.
def test(y,sr,target):
    mfcc = librosa.feature.mfcc(y=y,sr=sr,n_mfcc = 24,n_fft=512).T
    test_predict = gmm.predict(mfcc)
    test_label = np.full(len(mfcc),target)
    #print(test_predict)
    print(pd.value_counts(pd.Series(test_predict)))
    print("prediction: ",mode(test_predict))

#5. 테스트 파일을 통해 성능을 검증해 본다. 테스트 파일은 GMM 모델 구축을 위해 제공된 각 화자 데이터의 임의의 중간부분의  1.6초 길이의 음성데이터로 만들어 본다.  
test_file = 'data/F2.wav'
target = 2

y, sr = librosa.load(test_file, sr=16000) #y=512 sr=16000
second = len(y)/10 #1.6초
y2 = y[150:150+round(second)]
time2 = np.linspace(0, len(y2)/sr, len(y2))
test(y2,sr,target)