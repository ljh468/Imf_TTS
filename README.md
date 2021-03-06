# TTS project
- Imf_TTS -> SCE_TTS -> pythonfile 에 들어가시면 glow_tts학습, hifi_gan 학습 코드를 확인하실 수 있습니다.

## KSS데이터를 활용한 Text to speech service (glow_tts, hifi_gan)

기본 아키텍처 : 
![image](https://user-images.githubusercontent.com/64997253/144811436-6ae110ed-4527-4c81-8585-3f00dcb9253e.png)

Glow_TTS : 
![image](https://user-images.githubusercontent.com/64997253/144811459-11332e19-3105-4210-aa26-508865c917f0.png)
- Glow-TTS: A Generative Flow for Text-to-Speech via Monotonic Alignment Search 논문 참조

## 적용 기술
        - 프레임워크 : flask restAPI
        - 클라우드 환경 : 자체 서버
        - 개발 언어 : Python, pytorch
        - 개발 기술 : Glow_TTS, Hifi_gan 모델
        - 학습데이터 : KSS 데이터 ( https://www.kaggle.com/bryanpark/korean-single-speaker-speech-dataset )
          - 음향파일(문장) 갯수: 12,853
          - 단어 갯수: 5,091
          - Total Running Time: 12+ hours
          - Sample Rate: 44,100 kHz
          - Size: 4.32 GB
        - 에디터 : pycharm, jupyter notebook
        
## 기능

1. 12,853 문장의 한국어 데이터를 Glow_TTS와 Hifi_Gan 모델로 학습하여 텍스트를 음성 wav파일로 보여줌
2. 한국어 기수 및 서수, 자음접변(자음동화), 설측음화, 격음화, 외래어를 자연어처리하여 자연스러운 음성을 보여줌

### 프로젝트 기간
        - 2021-10-01 ~ 2021-11-31  
