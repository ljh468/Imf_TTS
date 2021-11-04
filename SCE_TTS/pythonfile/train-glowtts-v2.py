# 할당된 GPU 확인
import os
GPU_NAME = os.popen('nvidia-smi --query-gpu=name --format=csv,noheader').read().strip()
os.environ['GPU_NAME'] = GPU_NAME
print(f'GPU: {GPU_NAME}')

# 필수 라이브러리 및 함수 불러오기
import sys
from pathlib import Path

# test_sentences.txt 파일 생성
with open("C:/Users/User/Desktop/SCE_TTS/TTS/test_sentences.txt", mode="w") as f:
    f.write("""아래 문장들은 모델 학습을 위해 사용하지 않은 문장들입니다.
서울특별시 특허허가과 허가과장 허과장.
경찰청 철창살은 외철창살이고 검찰청 철창살은 쌍철창살이다.
지향을 지양으로 오기하는 일을 지양하는 언어 습관을 지향해야 한다.
그러니까 외계인이 우리 생각을 읽고 우리 생각을 우리가 다시 생각토록 해서 그 생각이 마치 우리가 생각한 것인 것처럼 속였다는 거냐?""")

# 처음 돌릴때
# cd C:/Users/User/Desktop/SCE_TTS
# python TTS/TTS/bin/train_glow_tts.py ^
# --config_path "C:/Users/User/Desktop/SCE_TTS/data/glowtts-v2/config.json" ^
# --coqpit.datasets.0.path "C:/Users/User/Desktop/SCE_TTS/data/filelists" ^
# --coqpit.audio.stats_path "C:/Users/User/Desktop/SCE_TTS/data/glowtts-v2/scale_stats.npy" ^
# --coqpit.test_sentences_file "C:/Users/User/Desktop/SCE_TTS/TTS/test_sentences.txt" ^
# --coqpit.output_path "C:/Users/User/Desktop/SCE_TTS/data/glowtts-v2/" ^
# --coqpit.num_loader_workers 2 ^
# --coqpit.num_val_loader_workers 2 ^
# --restore_path "C:/Users/User/Desktop/SCE_TTS/data/glowtts-v2/model_file.pth.tar"

# 이어서 돌릴때
# python TTS/TTS/bin/train_glow_tts.py ^
#     --continue_path "C:/Users/User/Desktop/SCE_TTS/data/glowtts-v2/glowtts-v2-October-13-2021_09+09AM-3aa165a"