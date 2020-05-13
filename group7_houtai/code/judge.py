# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:51:47 2020
结果判断

tips：我这里是将每一个测试集出现次数最多的故障当成了本测试集的故障。

@author: 33578
"""

import pandas as pd
import os
from collections import Counter
import numpy as np
import joblib
def judge(path,to_path,model):#无RPM
    # with open(model, 'rb') as file:
    #     clf=pickle.load(file)
    clf=joblib.load(model)
    filenames = os.listdir(path)
    for filename in filenames:
        if os.path.splitext(filename)[1] !='.csv': #目录下包含.csv的文件
            filenames.remove(filename)
    print(filenames)
    
    result=pd.DataFrame(columns=["label","filename"])
    for file in filenames:
        test_data=pd.read_csv(path+"/"+file)
        print("文件名: ",file)
    #     print(test_data.shape)
        test_data=np.array(test_data)
        print("文件行列数: ",test_data.shape)
        predict=clf.predict(test_data)
        #print("文件预测结果: ",predict)
        print("各个结果比例:",Counter(predict))
        print("most_common:",Counter(predict).most_common(1)[0][0])
        print("修改之后")
        predict[:]=Counter(predict).most_common(1)[0][0]
        print("各个结果比例:",Counter(predict),"\n")
        predict_frame = pd.DataFrame(predict,columns={"label"})
        
        
        predict_frame["filename"]=file.strip(".csv")
        result=pd.concat([result,predict_frame],ignore_index=True)
    print(result.shape)
    result.to_csv(to_path,index=False)

    
if __name__ == "__main__":
    judge("../test2/featured","../test2/result/"+"result1.csv",'../model/clf1.model')