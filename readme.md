第七组_移动互联网课程设计
===
## 项目概述
## 目录结构
|---group7_houtai<br>
| > |---code                     #本地需要运行的代码<br>
| > |---model                   #训练好的模型<br>
| > |---train	       #训练集的训练数据和中间数据<br>
| > | > |---datasets          #训练集<br>
| > | > |---datacleaned    #训练集清洗过后<br>
| > | > |---featured         #清洗后的数据提取特征<br>
| > | > |---datacsv           #提取特征后的数据合并<br>
| > | > |---labeld             #合并后的打标签<br>
| > |---test1	       #第一次测试集的测试数据、中间数据和结果<br>
| > | > |---datacleaned<br>
| > | > |---datasets<br>
| > | > |---featured<br>
| > | > |---result<br>
| > |---test2	       #第二次测试集的测试数据、中间数据和结果<br>
| > | > |---datacleaned<br>
| > | > |---datasets<br>
| > | > |---featured<br>
| > | > |---result<br>
| > |---upcode	       #上传到平台的代码<br>

## 版本管理<br>
2020.5.13 第一次上传<br>

## 依赖配置<br>
后台：
	软件：spyder  也可使用其它<br>
	运行环境：python3.7<br>
	库：sklearn pandas numpy os pywt scipy traceback re joblib collections 		matplotlib<br>
	环境部署：可通过安装anaconda一键部署，也可从官网下载python3<br>

## 部署说明
此文件附有代码和训练集、两个测试集，都已经放在想要的文件夹中，尽量不要改动。
## 运行说明
后台本地代码运行说明：<br>
		所有文件夹位置不要动，也不要改名。<br>
		(1)   运行/group7_houtai/code/datacleaned.py  对数据进行清洗<br>
		(2)   运行/group7_houtai/code/featuredget.py  进行特征提取<br>
		(3)   运行/group7_houtai/code/datagena.py  合并数据集<br>
		(4)   运行/group7_houtai/code/datalable.py  给数据集打标签<br>
		(4)   运行/group7_houtai/code/train.py         训练<br>
		(4)   运行/group7_houtai/code/judge.py       利用模型对测试集判断
每个代码中有简单的注释<br>
