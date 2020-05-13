# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 16:54:48 2020

@author: 33578
"""
import pandas as pd
import numpy as np
import joblib
import sys
import traceback
from collections import Counter
from sklearn.metrics import accuracy_score,recall_score,precision_score,f1_score,roc_auc_score
argvs = sys.argv
class Result:
    accuracy = 0
    recall = 0
    precision = 0
    fMeasure = 0
    rocArea = 0
params={}
params["test"]="C:/Users/33578/Desktop/TEST1_feature.csv"
params["opath"]="C:/Users/33578/Desktop/result.csv"
params["model"]="C:/Users/33578/Desktop/clf6.model"
try:
    for i in range(len(argvs)):
        if i < 1:
            continue
        if argvs[i].split('=')[1] == 'None':
            params[argvs[i].split('=')[0]] = None
        else:
            Type = type(params[argvs[i].split('=')[0]])
            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])   
            
    clf=joblib.load(params["model"])
    
    test_data=pd.read_csv(params["test"])
    test_data=np.array(test_data)
    predict=clf.predict(test_data)
    predict[:]=Counter(predict).most_common(1)[0][0]#把出现次数最多的当成该测试集的最终结果
    predict_frame = pd.DataFrame(predict,columns={"predict"})
    predict_frame.to_csv(params["opath"],index=False)
except Exception as e:
    traceback.print_exc()
