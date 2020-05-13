# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:48:13 2020

@author: 33578
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:43:28 2020
将同一个位置的数据集合并成一个，例如将B01.csv~B06.csv 合并成B.csv
re 是正则表达式，具体可查阅相关资料
@author: 33578
"""

import pandas as pd
import os
import re
def datagena(path,to_path):
    all_filenames= os.listdir(path)
    for filename in all_filenames:
        if os.path.splitext(filename)[1] !='.csv': #目录下包含.csv的文件
            all_filenames.remove(filename)
    #print(all_filenames)
    str_all_filenames=str(all_filenames)
    
    B_filenames=re.finditer(r'B(..).csv',str_all_filenames)
    NORMAL_filenames=re.finditer(r'NORMAL(..).csv',str_all_filenames)
    IR_filenames=re.finditer(r'IR(..).csv',str_all_filenames)
    OR_filenames=re.finditer(r'OR(..).csv',str_all_filenames)
    B_filenames_list=[]
    IR_filenames_list=[]
    OR_filenames_list=[]
    NORMAL_filenames_list=[]

    
    for file in B_filenames:
        B_filenames_list.append(file.group())
    for file in IR_filenames:
        IR_filenames_list.append(file.group())
    for file in OR_filenames:
        OR_filenames_list.append(file.group())
    for file in NORMAL_filenames:
        NORMAL_filenames_list.append(file.group())
        
    print(B_filenames_list)
    print(IR_filenames_list)
    print(OR_filenames_list)
    print(NORMAL_filenames_list)
    
    def hebing(filenames,outname):
        df_output=pd.DataFrame()
        for file in filenames:
            b=pd.read_csv(path+"/"+file)
            print(path+"/"+file,"---",b.shape)
            df_output=pd.concat([df_output,b],ignore_index=True)
        df_output.to_csv(to_path+"/"+outname+".csv",index=False)
        print(outname+"合并完成","---",df_output.shape)
    hebing(B_filenames_list,"B")
    hebing(IR_filenames_list,"IR")
    hebing(OR_filenames_list,"OR")
    hebing(NORMAL_filenames_list,"NORMAL")


if __name__ =="__main__":
    datagena("../train/featured","../train/datacsv")