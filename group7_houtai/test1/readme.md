# CWRU四分类任务实验

## 一、测试集数据说明
数据中包含一个文件夹，datasets，用作测试集。   
datasets文件夹中包含多个数据文件，文件名并不包含含义，仅用作记号。    
每个数据文件可能包含如下多维信号（部分文件可能其中不包括某些维度的信号）：   
DE_time:驱动端加速度数据   
FE_time:风扇端加速度数据   
BA_time:基本加速度数据   
RPM:每分钟转速数据，在提取时实际上RPM对于每个文件只有一个值，但为了文件格式整齐，扩展成了一列，即实际上这一列都是同一个值，代表该文件的RPM

特别说明：TEST08的原始数据不含RPM，经查，该数据的RPM是1750，有需要的可以使用该数值作为TEST08中RPM的参考值

## 二、测试集答案提交形式
提交答案时，约定normal(NORMAL), ball(B), outer race(OR), inner race(IR)的预测输出标签为0, 1, 2, 3。   
提交csv文件，文件分两列，第一列为按序预测结果(0/1/2/3)，第二列为预测结果所在的测试集文件(字符串形式，例如TEST01)，分别以label和filename作为列名。具体形式参照提供的example.csv。

## 三、评分规则
使用四类的f1-score(precision和recall值的调和平均数)加权和进行评价，按照上面的标签约定，即：   
score = [0.3×f1score(class1) + 0.3×f1score(class2) + 0.3×f1score(class3) + 0.1×f1score(class0)]*100   
满分为100分。

