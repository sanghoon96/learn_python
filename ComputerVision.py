import os
os.getcwd()

import pandas as pd
df1 = pd.read_excel('cd /home/sanghoon/사진/2image.xlsx')
import matplotlib.pyplot as plt
plt.imshow(df1.values, cmap='gray')
# df1.shape
# df1.values[0:26,0:26]

df2 = pd.read_excel('cd /home/sanghoon/사진/대각선.xlsx')
plt.imshow(df2.values, cmap='gray')
# df2.shape

import numpy as np
np.matmul(df1.values, df2.values)