# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 18:07:18 2020
随机森林算法。

算法主要参数：n_estimators=400 树的数量
           max_features=70   最多使用的特征数，之前我是一列提取45个特征，共两列，所以一共提取了90个特征
                              但是使用90维的特征时不如70维的结果准确，猜测是过拟合造成的。
@author: 33578
"""

from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import precision_score, recall_score, accuracy_score#, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
import joblib
def train(path,to_path):#没有RPM
    pd_data=pd.read_csv(path)#经过清洗、时频域特征提取、合并、标签之之后训练
    y=np.array(pd_data.loc[:,"label"])
    x=np.array(pd_data.drop(columns={"label"}, inplace=False))
    print(x.shape)
    print(y.shape)
    
    train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.1,random_state=123)
    
    clf = RandomForestClassifier(n_estimators=400,
                                 oob_score=True,
                                 max_features=70,
                                 min_samples_split=5,
                                 ).fit(train_x, train_y)
    
    predict = clf.predict(test_x)
    
    accuracy = accuracy_score(test_y, predict)
    precision = precision_score(test_y, predict, average="weighted")
    recall = recall_score(test_y, predict,average="weighted")
    
    print(accuracy)
    print(precision)
    print(recall)
    
    # with open(to_path, 'wb') as file:##经过清洗（0.1,n=200）、时频域特征提取（250）、合并、标签之之后训练 修改train
    #     pickle.dump(clf, file)
    joblib.dump(clf,to_path)
if __name__ == "__main__":
    train("../train/labeld/train_labeld.csv",'../model/clf1.model')