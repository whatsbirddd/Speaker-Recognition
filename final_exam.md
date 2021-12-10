# 8. Speech Signal

## 1.발성은 어떤 과정으로 발생하는가?

폐에서 나온 공기가 성대를 울리고 성도(vocal track)를 따라서 구강까지 연결

구강안의 혀,치아, 입술의 상대적 위치에 따라서 특정한 소리가 만들어짐

## 2.Formants

- 성도의 음향 공명에 의해서 발생
- 주파수 스펙트럼에서 진폭 피크로 측정(저주파부터 f1,f2,...)
- 주로 모음에서 만들어짐(유성음) 
  - f1,f2의 조합으로 모음 특정하기 충분함
  - 동일한 모음도 사람마댜 포먼트의 조합이 조금씩 다름
  - 예를 들어, 여성의 주파수가 남성의 주파수보다 평균적으로 높다는 거 !!
- **vocal track models** : 복잡한 실제 모양을 단순화된 모양으로 모델링하여 소리가 발생하는 것을 추적하고자 하였으나 실패함..
- 인간의 음성으로 구별되거나 의미있는 주파수 구성요소
- 모음 소리의 주파수 내용에 의해 정량적으로 표현
- 스펙트럼 그래프를 보면 모음부분에서 가로의 띠를 관측가능, 에너지도 많이 사용

## 3.Spectrogram

- 시간에 따라서 변화하는 주파수 스펙트럼을 시각화
- x축 : 시간, y축 : 주파수, z축 : 주파수 스펙트럼의 크기
- 선형 스케일 : 주파수의 하모닉스 관계
- 로그 스케일 : 음악적인 톤의 관계
  - 로그는 어떤 구간을 확대해서 보기에 좋은 수단
  - 저주파 : 현미경의 역할(확대)
  - 고주파 : 망원경의 역할(축소)
- window를 사용해서 짧게 자르는 과정 : **trade-off관계**
  - window를 크게하면(wide) : 주파수 해상도가 높아진다. 시간 해상도는 떨어진다.
  - window를 작게하면(narrow) : 시간 해상도는 좋지만 주파수 해상도가 떨어진다

## 4. Speech Processing
1. speech recognition : speech -> text
2. speaker recognition : identification/verification
3. speech synthesis : text -> speech
4. speech enhancement


# 9. Speaker recognition
- speaker identification
  - speaker 마다 모델 생성 필요
  - 화자가 n명이면 n개의 모델이 필요하다.
  - decision : softmax로 가장 높은 점수를 가진 모델
- speaker verification/authentification
  - speaker model
  - imposter model
  - decision : 가설검증, threshold보다 크면 accept
- text independent / dependent
  - independent : 어떤 말을 하는지 상관없음(dependent보다 어려운 태스크 -> 확률통계적 접근을 해보자!)
  - dependent : 주어진 말만 인식 가능

## 🎯Process
1. front-end processing
   1. 정규화
   2. 특징추출 : **mfcc(mel-frequency Cepstral Coefficient)** ✅
        + mel 주파수 대역 분할을 통한 특징추출
        + simple하여 light한 시스템에 적합
2. speaker modeling
   1. 추출된 특징 기반으로 확률 통계 모델
   2. GMM, HMM, NN등
   3. **GMM** ✅
      * gaussian mixture model
      * 데이터의 분포를 여러개의 가우시안의 혼합을 통해서 표현
      * 특정 샘플의 확률(P(x|m,c)) : gaussian들을 weighted sum
      * EM algorithm
        * 최적의 파라미터를 구하는 최적화 알고리즘
        * E,M-step을 계속 반복
        * E-step : gmm의파라미터 (mean, covariance, weight)기반으로 데이터 샘플들이 각 gaussian mixture에 assign될 확률 계산(로그우도)
        * M-step : 로그우도를 이용하여 새로운 GMM파라미터 계산
3. decision
   1. 확률적 판단
      1. identification : 가장 높은 확률
      2. verification : 정해진 수치 이상의 확률
         1. H0: The speaker is an imposter
         2. H1 : The speaker is the claimed speaker
         3. threshold를 보다 크면 accept
4. 성능 측정
   1. identification : error rate
   2. verification : 1종오류, 2종오류 (trade-off관계)
      1. EER : false alarm, false rejection 최적의 경우에 달성할 수 있는 최소 오류율
      2. DET curve
5. In practice
   1. front-end processing
      1. 묵음 구간 제거 : 모든 사람들에게 공통된 부분, 100msec이상의 묵음은 제거
      2. 소리의 크기 : 음량이 작거나 잡음대비 음량의 비율이 작으면 잡음을 최대한 없애고 정규화
   2. feature extraction 
      1. 몇차원의 벡터를 사용할 건지는 실험적, 경험적으로 알 수 있음
   3. speaker model : 당연히 데이터가 많을수록 성능이 좋아짐
   4. decision making : detection trade off를 고려해서 목적에 맞게 셋팅



# 10. MFCC 
- frame size(n_fft) : frame개수가 달라짐 - mfcc의 행을 결정
- filter size(filter) : mfcc의 차원을 결정 - mfcc의 열
- process : frame signal -> window frame -> FFT -> Mel Filterbank -> Log -> DCT -> Lifter
## 1. Frame
- window가 크면 : 주파수 해상도가 높음. 시간 해상도가 낮음. 그래프 -> 가로 띠모양
- window가 작으면 : 주파수 해상도가 낮음. 시간 해상도가 높음. 시각화 -> 세로 띠모양
## 2. Fourier Transform
## 3. mel frequency filter bank
## 4. log & DCT 
- quefrency 구하는 과정

## 5. Liftering
높은 큐프런시를 제거함으로써 주파수 스펙트럼의 윗부분만 남길 수 있음. 결과적으로 smoothing하는 것
