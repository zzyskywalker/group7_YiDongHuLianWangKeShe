# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:41:09 2020

提取特征
函数参数
path是清洗之后数据的文件夹，to_path是提取特征之后的文件夹，size是时间窗的大小

每一列提取了45个特征。

@author: 33578
"""

import pywt
import pandas as pd
import os
import numpy as np
from scipy import stats,fftpack
import traceback

def featureget(path,to_path,size):

    filenames=os.listdir(path)
    for filename in filenames:
        if os.path.splitext(filename)[1] !='.csv': #目录下包含.csv的文件
            filenames.remove(filename)
    print(filenames)
    print(type(filenames))
    columns_list = ['time_mean','time_std','time_max','time_min','time_rms','time_ptp','time_median','time_iqr','time_pr','time_skew','time_kurtosis','time_var','time_amp',
                        'time_smr','time_wavefactor','time_peakfactor','time_pulse','time_margin',
                        'freq_mean','freq_std','freq_max','freq_min','freq_rms','freq_median',
                        'freq_iqr','freq_pr','freq_f2','freq_f3','freq_f4','freq_f5','freq_f6','freq_f7','freq_f8','ener_cA5','ener_cD1','ener_cD2','ener_cD3','ener_cD4',
                        'ener_cD5','ratio_cA5','ratio_cD1','ratio_cD2','ratio_cD3','ratio_cD4','ratio_cD5']
    columns_list1 = ['DE_'+a for a in columns_list]
    columns_list2 = ['FE_'+a for a in columns_list]
    
    Windowsize=size
    try:
        for file in filenames:
            pd_data=pd.read_csv(path+"/"+file)
            result_list=[]
            for j in range(2):
                feature_list=[]
                for i in range(pd_data.shape[0]//Windowsize):
                    de_data=pd_data.iloc[i*Windowsize:i*Windowsize+Windowsize,j].values
            #       print(de_data)
                    #----------  time-domain feature,18
                    #依次为均值，标准差，最大值，最小值，均方根，峰峰值，中位数，四分位差，百分位差，偏度，峰度，方差，整流平均值，方根幅值，波形因子，峰值因子，脉冲值，裕度
                    time_mean = de_data.mean()
                    time_std = de_data.std()
                    time_max = de_data.max()
                    time_min = de_data.min()
                    time_rms = np.sqrt(np.square(de_data).mean())
                    time_ptp = de_data.ptp()
                    time_median = np.median(de_data)
                    time_iqr = np.percentile(de_data,75)-np.percentile(de_data,25)
                    time_pr = np.percentile(de_data,90)-np.percentile(de_data,10)
                    time_skew = stats.skew(de_data)
                    time_kurtosis = stats.kurtosis(de_data)
                    time_var = np.var(de_data)
                    time_amp = np.abs(de_data).mean()
                    time_smr = np.square(np.sqrt(np.abs(de_data)).mean())
                    #下面四个特征需要注意分母为0或接近0问题，可能会发生报错
                    time_wavefactor = time_rms/time_amp
                    time_peakfactor = time_max/time_rms
                    time_pulse = time_max/time_amp
                    time_margin = time_max/time_smr
                    #----------  freq-domain feature,15
                    #采样频率25600Hz
                    df_fftline = fftpack.fft(de_data)
                    freq_fftline = fftpack.fftfreq(len(de_data),1/25600)
                    df_fftline = abs(df_fftline[freq_fftline>=0])
                    freq_fftline = freq_fftline[freq_fftline>=0]
                    #基本特征,依次为均值，标准差，最大值，最小值，均方根，中位数，四分位差，百分位差
                    freq_mean = df_fftline.mean()
                    freq_std = df_fftline.std()
                    freq_max = df_fftline.max()
                    freq_min = df_fftline.min()
                    freq_rms = np.sqrt(np.square(df_fftline).mean())
                    freq_median = np.median(df_fftline)
                    freq_iqr = np.percentile(df_fftline,75)-np.percentile(df_fftline,25)
                    freq_pr = np.percentile(df_fftline,90)-np.percentile(df_fftline,10)
                    #f2 f3 f4反映频谱集中程度
                    freq_f2 = np.square((df_fftline-freq_mean)).sum()/(len(df_fftline)-1)
                    freq_f3 = pow((df_fftline-freq_mean),3).sum()/(len(df_fftline)*pow(freq_f2,1.5))
                    freq_f4 = pow((df_fftline-freq_mean),4).sum()/(len(df_fftline)*pow(freq_f2,2))
                    #f5 f6 f7 f8反映主频带位置
                    freq_f5 = np.multiply(freq_fftline,df_fftline).sum()/df_fftline.sum()
                    freq_f6 = np.sqrt(np.multiply(np.square(freq_fftline),df_fftline).sum())/df_fftline.sum()
                    freq_f7 = np.sqrt(np.multiply(pow(freq_fftline,4),df_fftline).sum())/np.multiply(np.square(freq_fftline),df_fftline).sum()
                    freq_f8 = np.multiply(np.square(freq_fftline),df_fftline).sum()/np.sqrt(np.multiply(pow(freq_fftline,4),df_fftline).sum()*df_fftline.sum())
                    #----------  timefreq-domain feature,12
                    #5级小波变换，最后输出6个能量特征和其归一化能量特征
                    cA5, cD5, cD4, cD3, cD2, cD1 =pywt.wavedec(de_data, 'db10', level=5)
                    ener_cA5 = np.square(cA5).sum()
                    ener_cD5 = np.square(cD5).sum()
                    ener_cD4 = np.square(cD4).sum()
                    ener_cD3 = np.square(cD3).sum()
                    ener_cD2 = np.square(cD2).sum()
                    ener_cD1 = np.square(cD1).sum()
                    ener = ener_cA5 + ener_cD1 + ener_cD2 + ener_cD3 + ener_cD4 + ener_cD5
                    ratio_cA5 = ener_cA5/ener
                    ratio_cD5 = ener_cD5/ener
                    ratio_cD4 = ener_cD4/ener
                    ratio_cD3 = ener_cD3/ener
                    ratio_cD2 = ener_cD2/ener
                    ratio_cD1 = ener_cD1/ener
                    feature_list.append([time_mean,time_std,time_max,time_min,time_rms,time_ptp,time_median,time_iqr,time_pr,time_skew,time_kurtosis,time_var,time_amp,
                                             time_smr,time_wavefactor,time_peakfactor,time_pulse,time_margin,
                                             freq_mean,freq_std,freq_max,freq_min,freq_rms,freq_median,
                                             freq_iqr,freq_pr,freq_f2,freq_f3,freq_f4,freq_f5,freq_f6,freq_f7,freq_f8,ener_cA5,ener_cD1,ener_cD2,ener_cD3,ener_cD4,ener_cD5,
                                             ratio_cA5,ratio_cD1,ratio_cD2,ratio_cD3,ratio_cD4,ratio_cD5])
                print(file+"第"+str(j)+"列完成")
                result_list.append(feature_list)
            result_frame1=pd.DataFrame(np.array(result_list)[0],columns=columns_list1)
            result_frame2=pd.DataFrame(np.array(result_list)[1],columns=columns_list2)
            # RPM_array=np.array(pd_data.iloc[0:result_frame1.shape[0],2])
            # RPM_frame=pd.DataFrame(RPM_array,columns={"RPM"})
            result_frame=pd.concat([result_frame1,result_frame2],axis=1,ignore_index=False)
            result_frame.to_csv(to_path+"/"+file,index=False)
            print(file+"已完成")
    except Exception as e:
        traceback.print_exc()

if __name__ == "__main__":
    featureget("../train/datacleaned","../train/featured",250)
    featureget("../test2/datacleaned","../test2/featured",250)