# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:22:56 2017
as the program test for the agricuture program of Dr. du

自适应加权融合算法-
Adaptive weighted fusion algorithm

@author: Jon Zang，杭州，15168307480，zangzelin@gmail.com

"""

import numpy as np

datawsd = np.array(([0.645, 0.103, 0.025, 0.148, 0.075, 0.018],  # 初始化原料矩阵1
                    [0.382, 0.067, 0.460, 0.042, 0.115, 0.027]))
datawgd = np.array(([0.645, 0.103, 0.025, 0.148, 0.075, 0.018],  # 初始化原料矩阵2
                    [0.053, 0.104, 0.019, 0.702, 0.058, 0.001]))

K1 = np.zeros((6, 6))  # 初始化K
for i in range(6):     # 分别计算K
    for j in range(6):
        if i != j:
            K1[i, j] = datawsd[0, i] * datawsd[1, j]
k1sumA = 1-K1.sum()    # 为k求和

K1B = np.zeros((6, 6))  # 初始化分母KB
for i in range(6):      # 分别计算分母
   K1B[i, 0] = datawsd[0, i] * datawsd[1, i]   \
               + datawsd[0, i] * datawsd[1, 5] \
               + datawsd[1, i] * datawsd[0, 5]
k1sumB = K1B.sum()      # KB求和

out1 = np.zeros((1, 6))
for i in range(6):
    out1[0, i] = (   # 计算输出
                     datawsd[0, i] * datawsd[1, i]
                   + datawsd[0, i] * datawsd[1, 5]
                   + datawsd[1, i] * datawsd[0, 5]   ) / k1sumB
print(out1)
