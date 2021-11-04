# HiFi-GAN 학습

# 데모에 대한 더 자세한 정보는 아래 링크에서 확인하실 수 있습니다.
# https://sce-tts.github.io/

# 1. 할당된 GPU 확인
import os
GPU_NAME = os.popen('nvidia-smi --query-gpu=name --format=csv,noheader').read().strip()
os.environ['GPU_NAME'] = GPU_NAME
print(f'GPU: {GPU_NAME}')

import sys
from pathlib import Path

# cd C:/Users/User/Desktop/SCE_TTS/TTS
# python TTS/bin/train_vocoder_gan.py ^
#     --config_path "C:/Users/User/Desktop/SCE_TTS/data/hifigan-v2/config.json" ^
#     --coqpit.data_path "C:/Users/User/Desktop/SCE_TTS/data/filelists/wavs"  ^
#     --coqpit.audio.stats_path "C:/Users/User/Desktop/SCE_TTS/data/hifigan-v2/scale_stats.npy"  ^
#     --coqpit.output_path "C:/Users/User/Desktop/SCE_TTS/data/hifigan-v2/"  ^
#     --coqpit.num_loader_workers 2  ^
#     --coqpit.num_val_loader_workers 2  ^
#     --restore_path "C:/Users/User/Desktop/SCE_TTS/data/hifigan-v2/model_file.pth.tar"
#
# python TTS/bin/train_vocoder_gan.py ^
# --continue_path "C:/Users/User/Desktop/SCE_TTS/data/hifigan-v2/hifigan-v2-October-14-2021_06+32AM-3aa165a"