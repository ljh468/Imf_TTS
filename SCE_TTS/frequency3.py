# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('./word_count.csv')
print(df['count'])