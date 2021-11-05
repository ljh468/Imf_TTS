# -*- coding: utf-8 -*-
import numpy as np
data = np.load('./data/hifi_scale_stats.npy', allow_pickle=True)
print(data)
# print(data)
list = data.tolist()
# print(list['mel_mean'].shape)
# print(list['mel_std'].shape)
# print(list['linear_mean'].shape)
# print(list['linear_std'].shape)
#
n1 = list['mel_mean']
n2 = list['mel_std']
n3 = list['linear_mean']
n4 = list['linear_std']

# n1 = np.random.randn(80,)
# n2 = np.random.randn(80,)
# n3 = np.random.randn(513,)
# n4 = np.random.randn(513,)
# list['audio_config']['stats_path'] = 'C:/Users/User/Desktop/SCE_TTS/data/glowtts-v2/scale_stats.npy'
list['audio_config']['stats_path'] = 'C:/Users/User/Desktop/SCE_TTS/data/hifigan-v2/scale_stats.npy'
# list['audio_config']['stats_path'] = '/content/drive/My Drive/Colab Notebooks/data/hifigan-v2/scale_stats.npy'
# print(list['audio_config']['stats_path'])
n5 = list['audio_config']
#
data0 = {}
data0['mel_mean'] = n1
data0['mel_std'] = n2
data0['linear_mean'] = n3
data0['linear_std'] = n4
data0['audio_config'] = n5
# print(data0)
result = np.array(data0)
print(result)
np.save('./data/hifi.npy', result)