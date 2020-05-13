# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:52:24 2020

@author: 33578
"""

from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np
import os
import traceback
import sys
import json
argvs = sys.argv
params = {}
params["path"]="C:/Users/33578/Desktop/TEST1.csv"
params["n_estimators"]=400
params["contamination"]=0.001
params["opath"]="C:/Users/33578/Desktop/TEST1_cleaned.csv"

try:
    for i in range(len(argvs)):
        if i < 1:
            continue
        if argvs[i].split('=')[1] == 'None':
            params[argvs[i].split('=')[0]] = None
        else:
            Type = type(params[argvs[i].split('=')[0]])
            params[argvs[i].split('=')[0]] = Type(argvs[i].split('=')[1])    
    
    pd_data=pd.read_csv(params["path"],usecols={"DE_time","FE_time"})
    read_data=pd_data.iloc[:,0:2]
    read_array=np.array(read_data)
    clf = IsolationForest(n_estimators=params["n_estimators"], 
                           max_samples="auto", 
                           contamination=params["contamination"], 
                           max_features=1.0, 
                           bootstrap=False, n_jobs=1, random_state=None, 
                           verbose=0).fit(read_array)
    pred =clf.predict(read_array)
    array_normal=read_array[pred == 1]
    frame_normal=pd.DataFrame(array_normal,columns=["DE_time","FE_time"])
    frame_normal.to_csv(params["opath"],index=False)
    res = {}
    res["opath"]=params["opath"]
    print(json.dumps(res))
except Exception as e:
    traceback.print_exc()