# -*- coding: utf-8 -*-
# # Pytorch GPU 연결확인
# import torch
# print(torch.cuda_version)
# print(torch.cuda.is_available())
# print(torch.cuda.get_device_name(0))
#
# # Tensorflow GPU 연결확인
# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())

# mecab 설치 확인
# import MeCab
# mecab = MeCab.Tagger()

from konlpy.tag import *
mecab = Mecab(dicpath=r"C:\mecab\mecab-ko-dic")

f = open("C:/Users/User/Desktop/SCE_TTS/origin_sentence.txt", 'r', encoding="UTF-8")
wordCount = {}

while True:
    line = f.readline()
    wordList = mecab.nouns(line)

    for word in wordList:
        # Get 명령어를 통해, Dictionary에 Key가 없으면 0리턴
        wordCount[word] = wordCount.get(word, 0) + 1

    if not line: break
f.close()
keys = sorted(wordCount.keys())
vals = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)

# txt파일 만들기
f2 = open("C:/Users/User/Desktop/SCE_TTS/단어_단어정렬.txt", 'w', encoding="UTF-8")
for word in keys:
    f2.write(word + ' : ' + str(wordCount[word]) + '\n')
f2.close()

f3 = open("C:/Users/User/Desktop/SCE_TTS/단어_빈도수정렬.txt", 'w', encoding="UTF-8")
for word2 in vals:
    f3.write(word2[0] + ' : ' + str(word2[1]) + '\n')
f3.close()

# 데이터 프레임으로 만들기
import pandas as pd
# word_count = pd.DataFrame(index=)
word_list = []
count_list = []
for w, c in vals:
    word_list.append(w)
    count_list.append(c)

korea_df = pd.DataFrame({'word':word_list,
                         'count':count_list})
korea_df.style.hide_index()
print(korea_df)
korea_df.to_csv('./word_count.csv', encoding='utf-8-sig', index = False)