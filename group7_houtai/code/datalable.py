# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 21:47:53 2020
给合并后的数据集分别打上标签，然后再合并到一整个训练集中
@author: 33578
"""

#lables
import pandas as pd

def labled(path,to_path):
    data_B = pd.read_csv(path+"/"+"B.csv")
    data_IR = pd.read_csv(path+"/"+'IR.csv')
    data_NOR = pd.read_csv(path+"/"+'NORMAL.csv')
    data_OR = pd.read_csv(path+"/"+'OR.csv')
    #print(data_B.shape)
    #print(data_NOR.shape)
    data_NOR["label"]=0
    
    data_B["label"]=1
    
    data_OR["label"]=2
    data_IR["label"]=3
    
    data_labled=pd.concat([data_NOR,data_B,data_IR,data_OR],ignore_index=True)
    #print(data_labled.shape)
    #print(data_labled)
    data_NOR.to_csv(to_path+"/"+"NOR_labeld.csv",index=False)
    print("NORMAL标签完成",data_NOR.shape,to_path)
    data_B.to_csv(to_path+"/"+"B_labeld.csv",index=False)
    print("BALL标签完成",data_B.shape,to_path)
    data_IR.to_csv(to_path+"/"+"IR_labeld.csv",index=False)
    print("INNER RACE标签完成",data_IR.shape,to_path)
    data_OR.to_csv(to_path+"/"+"OR_labeld.csv",index=False)
    print("OUTER RACE标签完成",data_OR.shape,to_path)
    data_labled.to_csv(to_path+"/"+"train_labeld.csv",index=False)
    print("train标签完成",data_labled.shape,to_path)

if __name__ == "__main__":
    labled("../train/datacsv","../train/labeld")