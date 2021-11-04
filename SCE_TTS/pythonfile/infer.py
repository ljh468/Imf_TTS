# -*- coding: utf-8 -*-
import wave

from TTS.tts.utils.text import symbols
from TTS.utils import synthesizer
from TTS.tts.utils import synthesis
from g2pK.g2pk import g2pk
g2p = g2pk.G2p()

import re
import sys
from unicodedata import normalize
import IPython

from TTS.utils.synthesizer import Synthesizer

def normalize_text(text):
    text = text.strip()

    for c in ",;:":
        text = text.replace(c, ".")
    text = remove_duplicated_punctuations(text)

    text = jamo_text(text)

    text = g2p.idioms(text)
    text = g2pk.convert_eng(text, g2p.cmu)
    text = g2pk.annotate(text, g2p.mecab)
    text = g2pk.convert_num(text)
    text = re.sub("/[PJEB]", "", text)

    text = alphabet_text(text)

    # remove unreadable characters
    text = normalize("NFD", text)
    text = "".join(c for c in text if c in symbols)
    text = normalize("NFC", text)

    text = text.strip()
    if len(text) == 0:
        return ""

    # only single punctuation
    if text in '.!?':
        return punctuation_text(text)

    # append punctuation if there is no punctuation at the end of the text
    if text[-1] not in '.!?':
        text += '.'

    return text


def remove_duplicated_punctuations(text):
    text = re.sub(r"[.?!]+\?", "?", text)
    text = re.sub(r"[.?!]+!", "!", text)
    text = re.sub(r"[.?!]+\.", ".", text)
    return text


def split_text(text):
    text = remove_duplicated_punctuations(text)

    texts = []
    for subtext in re.findall(r'[^.!?\n]*[.!?\n]', text):
        texts.append(subtext.strip())

    return texts


def alphabet_text(text):
    text = re.sub(r"(a|A)", "에이", text)
    text = re.sub(r"(b|B)", "비", text)
    text = re.sub(r"(c|C)", "씨", text)
    text = re.sub(r"(d|D)", "디", text)
    text = re.sub(r"(e|E)", "이", text)
    text = re.sub(r"(f|F)", "에프", text)
    text = re.sub(r"(g|G)", "쥐", text)
    text = re.sub(r"(h|H)", "에이치", text)
    text = re.sub(r"(i|I)", "아이", text)
    text = re.sub(r"(j|J)", "제이", text)
    text = re.sub(r"(k|K)", "케이", text)
    text = re.sub(r"(l|L)", "엘", text)
    text = re.sub(r"(m|M)", "엠", text)
    text = re.sub(r"(n|N)", "엔", text)
    text = re.sub(r"(o|O)", "오", text)
    text = re.sub(r"(p|P)", "피", text)
    text = re.sub(r"(q|Q)", "큐", text)
    text = re.sub(r"(r|R)", "알", text)
    text = re.sub(r"(s|S)", "에스", text)
    text = re.sub(r"(t|T)", "티", text)
    text = re.sub(r"(u|U)", "유", text)
    text = re.sub(r"(v|V)", "브이", text)
    text = re.sub(r"(w|W)", "더블유", text)
    text = re.sub(r"(x|X)", "엑스", text)
    text = re.sub(r"(y|Y)", "와이", text)
    text = re.sub(r"(z|Z)", "지", text)

    return text


def punctuation_text(text):
    # 문장부호
    text = re.sub(r"!", "느낌표", text)
    text = re.sub(r"\?", "물음표", text)
    text = re.sub(r"\.", "마침표", text)

    return text


def jamo_text(text):
    # 기본 자모음
    text = re.sub(r"ㄱ", "기역", text)
    text = re.sub(r"ㄴ", "니은", text)
    text = re.sub(r"ㄷ", "디귿", text)
    text = re.sub(r"ㄹ", "리을", text)
    text = re.sub(r"ㅁ", "미음", text)
    text = re.sub(r"ㅂ", "비읍", text)
    text = re.sub(r"ㅅ", "시옷", text)
    text = re.sub(r"ㅇ", "이응", text)
    text = re.sub(r"ㅈ", "지읒", text)
    text = re.sub(r"ㅊ", "치읓", text)
    text = re.sub(r"ㅋ", "키읔", text)
    text = re.sub(r"ㅌ", "티읕", text)
    text = re.sub(r"ㅍ", "피읖", text)
    text = re.sub(r"ㅎ", "히읗", text)
    text = re.sub(r"ㄲ", "쌍기역", text)
    text = re.sub(r"ㄸ", "쌍디귿", text)
    text = re.sub(r"ㅃ", "쌍비읍", text)
    text = re.sub(r"ㅆ", "쌍시옷", text)
    text = re.sub(r"ㅉ", "쌍지읒", text)
    text = re.sub(r"ㄳ", "기역시옷", text)
    text = re.sub(r"ㄵ", "니은지읒", text)
    text = re.sub(r"ㄶ", "니은히읗", text)
    text = re.sub(r"ㄺ", "리을기역", text)
    text = re.sub(r"ㄻ", "리을미음", text)
    text = re.sub(r"ㄼ", "리을비읍", text)
    text = re.sub(r"ㄽ", "리을시옷", text)
    text = re.sub(r"ㄾ", "리을티읕", text)
    text = re.sub(r"ㄿ", "리을피읍", text)
    text = re.sub(r"ㅀ", "리을히읗", text)
    text = re.sub(r"ㅄ", "비읍시옷", text)
    text = re.sub(r"ㅏ", "아", text)
    text = re.sub(r"ㅑ", "야", text)
    text = re.sub(r"ㅓ", "어", text)
    text = re.sub(r"ㅕ", "여", text)
    text = re.sub(r"ㅗ", "오", text)
    text = re.sub(r"ㅛ", "요", text)
    text = re.sub(r"ㅜ", "우", text)
    text = re.sub(r"ㅠ", "유", text)
    text = re.sub(r"ㅡ", "으", text)
    text = re.sub(r"ㅣ", "이", text)
    text = re.sub(r"ㅐ", "애", text)
    text = re.sub(r"ㅒ", "얘", text)
    text = re.sub(r"ㅔ", "에", text)
    text = re.sub(r"ㅖ", "예", text)
    text = re.sub(r"ㅘ", "와", text)
    text = re.sub(r"ㅙ", "왜", text)
    text = re.sub(r"ㅚ", "외", text)
    text = re.sub(r"ㅝ", "워", text)
    text = re.sub(r"ㅞ", "웨", text)
    text = re.sub(r"ㅟ", "위", text)
    text = re.sub(r"ㅢ", "의", text)

    return text


def normalize_multiline_text(long_text):
    texts = split_text(long_text)
    normalized_texts = [normalize_text(text).strip() for text in texts]
    return [text for text in normalized_texts if len(text) > 0]

def synthesize(text):
    wavs = synthesizer.tts(text, None, None)
    return wavs

import os
os.chdir("C:/Users/User/Desktop/SCE_TTS")
synthesizer = Synthesizer(
    "C:/Users/User/Desktop/SCE_TTS/data/glowtts-v2/glowtts-v2-November-04-2021_04+19AM-3aa165a/checkpoint_48000.pth.tar",
    "C:/Users/User/Desktop/SCE_TTS/data/glowtts-v2/config.json",
    None,
    "C:/Users/User/Desktop/SCE_TTS/data/hifigan-v2/hifigan-v2-November-04-2021_03+10PM-3aa165a/checkpoint_20000.pth.tar",
    "C:/Users/User/Desktop/SCE_TTS/data/hifigan-v2/config.json",
    None,
    None,
    False,
)
symbols = synthesizer.tts_config.characters.characters

texts = """
300만원 주세요
300 만원 주세요
서울특별시 특허허가과 허가과장 허과장.
경찰청 철창살은 외철창살이고 검찰청 철창살은 쌍철창살이다.
지향을 지양으로 오기하는 일을 지양하는 언어 습관을 지향해야 한다.
그러니까 외계인이 우리 생각을 읽고 우리 생각을 우리가 다시 생각토록 해서 그 생각이 마치 우리가 생각한 것인 것처럼 속였다는 거냐?
"""
def play_wav(np_audio,fs):
    import sounddevice as sd
    sd.play(np_audio, fs)
    sd.wait()

def write2wav(np_audio, filename):
    from scipy.io.wavfile import write
    write(filename, 22050, np_audio)


from scipy.io.wavfile import write
name = "test"
num = 0
for text in normalize_multiline_text(texts):
    num = num + 1
    file_name = name + str(num) + ".wav"
    wav = synthesizer.tts(text, None, None)
    # IPython.display.display(IPython.display.Audio(wavs, rate=22050))
    # wav 파일 저장 (wav 파일의 type은 list)
    synthesizer.save_wav(wav=wav, path=file_name)

    # wav 재생
    play_wav(wav, 22050)
    # wav 저장 (단일 파일인 경우 저장)
    # write2wav(wav, file_name)

print('len : ',len(wav))
print('dtype : ', type(wav))