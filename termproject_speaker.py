import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture

"""
-디렉토리 경로 추가
1. train_file = 디렉토리 경로 + 교수님께서 주신 데이터 파일명(speakers 리스트에 저장)
2. test_file = C:/Users/user0425/Desktop/DigitalSound/ ---.wav
3. f = open("C:/Users/user0425/Desktop/DigitalSound/result.txt",'a')

-해당파일과 동일한 디렉토리에 "result.txt"파일을 추가해주세요!

"""

n_mfcc = 24
n_fft =512
train_data = []
train_label = []
models = {}


speakers = ["F1","F2","M1","M2"]

for i,s in enumerate(speakers):
    #1. 파일은 16000Hz, 16bits, mono, wave 파일임
    #2. 파이썬 코드를 이용하여 MFCC 코드를 활용하는데, 입력데이터 y는 512, mfcc 갯수 n은 24로 진행한다. 한개의 파일 당 500개의 프레임으로 분할됨.
    train_file = "C:/Users/user0425/Desktop/DigitalSound/"+s+".wav"
    y, sr = librosa.load(train_file, sr=16000) #y=512 sr=16000
    mfcc = librosa.feature.mfcc(y=y,sr=sr,n_mfcc = 24,n_fft=512).T
    #print("mfcc :",mfcc.shape)
    
    #3. 2번 결과 데이터를 이용하여 GMM 모델을 구축한다. Mixture 갯수는 5로 설정한다.
    train_data = mfcc
    train_label = np.full(len(mfcc),1)
    gmm = GaussianMixture(n_components=5, random_state=42)
    gmm.fit(train_data)
    models[s] = gmm
        
#print("----------------------------")
#print(train_data.shape)
#print(train_label.shape)
#print("----------------------------")

#4. 3번에서 만든 코드를 활용하여 화자인식 테스트 코드를 만든다.
#5. 테스트 파일을 통해 성능을 검증해 본다. 테스트 파일은 GMM 모델 구축을 위해 제공된 각 화자 데이터의 임의의 중간부분의  1.6초 길이의 음성데이터로 만들어 본다.  
test_file = 'C:/Users/user0425/Desktop/DigitalSound/'
f = open("C:/Users/user0425/Desktop/DigitalSound/result.txt",'a')
y, sr = librosa.load(test_file, sr=16000) #y=512 sr=16000
second = len(y)/10 #1.6초
y2 = y[150:150+round(second)] 
test_mfcc = librosa.feature.mfcc(y=y2,sr=sr,n_mfcc = 24,n_fft=512).T

log_likelihood = np.zeros(len(models))
for i,s in enumerate(speakers):
    gmm = models[s]
    scores = np.array(gmm.score(test_mfcc))
    log_likelihood[i] = scores.sum()
 
winner = np.argmax(log_likelihood)
f.write(speakers[winner]+"\n")
print("speaker: ", speakers[winner])
f.close()

