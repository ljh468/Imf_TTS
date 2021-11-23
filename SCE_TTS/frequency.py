# -*- coding: utf-8 -*-
import re

hangul = re.compile('[^ ㄱ-ㅣ가-힣+]')
f = open("C:/Users/User/Desktop/SCE_TTS/kss.txt", 'r', encoding="UTF-8")
f2 = open("C:/Users/User/Desktop/SCE_TTS/origin_sentence.txt", 'w', encoding="UTF-8")
while True:
    line = f.readline()
    p = hangul.sub('', line)
    f2.write(p + "\n")
    if not line: break

f.close()
f2.close()