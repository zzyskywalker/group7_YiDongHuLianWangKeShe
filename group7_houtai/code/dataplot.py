# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:27:09 2020
这里只是随便看了一下test2里面几个数据集的模样，非必要代码
@author: 33578
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

filepath=os.listdir('../test2/datasets')#读取该文件夹下的所有文件名
filenames=filepath[:4]
print(filenames)

i=1
for file in filenames:
    data=pd.read_csv('../test2/datasets/'+file)
    plt.subplot(2,2,i)#子图
    plt.title(file)#文件名
    plt.plot(data.iloc[:,0])
    i=i+1
plt.show()