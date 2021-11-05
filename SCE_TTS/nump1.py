# -*- coding: utf-8 -*-
import numpy as np
data = np.load('./data/glowtts-v2/scale_stats.npy', allow_pickle=True)
list = data.tolist()
n1 = np.random.randn(80,)
n2 = np.random.randn(80,)
n3 = np.random.randn(513,)
n4 = np.random.randn(513,)
# list['audio_config']['stats_path'] = 'C:/Users/shfkf/Desktop/SCE_TTS/data/glowtts-v2/scale_stats.npy'
list['audio_config']['stats_path'] = '/content/drive/My Drive/Colab Notebooks/data/glowtts-v2/scale_stats.npy'
print(list['audio_config']['stats_path'])
n5 = list['audio_config']


data0 = {}
data0['mel_mean'] = n1
data0['mel_std'] = n2
data0['linear_mean'] = n3
data0['linear_std'] = n4
data0['audio_config'] = n5
print(data0)
# print(type(data0))
result = np.array(data0)

np.save('./data/hifigan-v2/hifigan-v2-October-14-2021_06+32AM-3aa165a/make_scale_stats.npy', result)

# data = np.load('./data/hifigan-v2/hifigan-v2-October-14-2021_06+32AM-3aa165a/make_scale_stats.npy', allow_pickle=True)
# print(data)

# print(result)
# print(list['mel_std'])
# print(list['linear_mean'])
# print(list['linear_std'])
# print(list['audio_config'])

# i = 0
# var = 'data' + str(i)
# print(len(data.item()))
# print(data.shape)
# for i in range(0, 5):
#     print(data[i])
# for i in range(len(data.keys())):
#     print(var)
#     var = i

# data1 = np.ones(data)
# print(data1)

# Pytorch GPU 연결확인
# import torch
# print(torch.cuda.is_available())
# print(torch.version.cuda)
# print(torch.backends.cudnn.enabled)
# print(torch.cuda.get_device_name(0))
# print()

# Tensorflow GPU 연결확인
# from tensorflow.python.client import device_lib
# print(device_lib.list_local_devices())

# import MeCab
# m = MeCab.Tagger()
# out= m.parse("미캅이 잘 설치되었는지 확인중입니다.")
# print(out)