# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:09:36 2020

函数参数说明：
            path：数据集的存放位置，文件夹的名字
            to_path:清洗之后存放的位置

主要算法说明
孤立森林算法，进行异常点检测。
关键参数 n_estimators ：森林中的树的个数
        contamination ：异常点的数量

@author: 33578
"""

from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np
import os

def datacleaned(path,to_path):
    filenames=os.listdir(path)
    print(filenames)
    for file in filenames:
        pd_data=pd.read_csv(path+"/"+file,usecols={"DE_time","FE_time"})
        read_data=pd_data.iloc[:,0:2]
        read_array=np.array(read_data)
        clf = IsolationForest(n_estimators=400, 
                              max_samples="auto", 
                              contamination=0.001, 
                              max_features=1.0, 
                              bootstrap=False, n_jobs=1, random_state=None, 
                              verbose=0).fit(read_array)
        pred =clf.predict(read_array)
        array_normal=read_array[pred == 1]
        frame_normal=pd.DataFrame(array_normal,columns=["DE_time","FE_time"])
       # frame_normal=pd.concat([frame_normal,pd_data.loc[0:frame_normal.shape[0]-1,"RPM"]],ignore_index=True,axis=1)
        frame_normal.to_csv(to_path+"/"+file,index=False)
        print(file+"finished")
    
if __name__ == "__main__":
    datacleaned("../train/datasets","../train/datacleaned")#train set
    print("all finished")
    datacleaned("../test2/datasets","../test2/datacleaned")#test2 set 
    print("all finished")