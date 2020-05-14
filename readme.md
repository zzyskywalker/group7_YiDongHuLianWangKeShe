第七组_移动互联网课程设计
===
## 项目概述
前端采用微信小程序进行端到端的app开发，分析工厂运维人员在实际工作中的需求，做出设备工况监测、故障类型监测等核心功能。<br>
后台对数据进行清洗、特征提取、训练模型，对数据进行分类，判断故障类型
## 目录结构
|---bearingDemo<br> &nbsp; 小程序部分
|---group7_houtai<br>&nbsp; 后台部分
| > |---code            &nbsp;         #本地需要运行的代码<br>
| > |---model           &nbsp;        #训练好的模型<br>
| > |---train	    	 &nbsp;  #训练集的训练数据和中间数据<br>
| > | > |---datasets    &nbsp;      #训练集<br>
| > | > |---datacleaned  &nbsp;  #训练集清洗过后<br>
| > | > |---featured      &nbsp;   #清洗后的数据提取特征<br>
| > | > |---datacsv       &nbsp;    #提取特征后的数据合并<br>
| > | > |---labeld       &nbsp;      #合并后的打标签<br>
| > |---test1	      &nbsp; #第一次测试集的测试数据、中间数据和结果<br>
| > | > |---datacleaned<br>
| > | > |---datasets<br>
| > | > |---featured<br>
| > | > |---result<br>
| > |---test2	     &nbsp;  #第二次测试集的测试数据、中间数据和结果<br>
| > | > |---datacleaned<br>
| > | > |---datasets<br>
| > | > |---featured<br>
| > | > |---result<br>
| > |---upcode	     &nbsp;  #上传到平台的代码<br>

## 版本管理<br>
2020.5.13 &nbsp;16：22  第一次上传<br>
2020.5.13 &nbsp;17：41  github不能上传空文件夹，所以我在每一个空文件夹中添加了 .gitkeep 文件，同时在代码中添加了几句，让所有代码只读取.csv文件。<br>
2020.5.14 &nbsp;22：07   将代码部分与数据集拆分，方便下载
2020.5.14 &nbsp;22：39 将小程序部分上传
## 依赖配置<br>
* 前端：
	* 采用微信开发者工具
	* 引用：echars组件、weui库
* 后台：
	* 软件：spyder  也可使用其它<br>
	* 运行环境：python3.7<br>
	* 库：sklearn pandas numpy os pywt scipy traceback re joblib collections 		matplotlib<br>
	* 环境部署：可通过安装anaconda一键部署，也可从官网下载python3<br>

## 部署说明
* 前端
	* 将bearingDemo文件夹直接导入到微信开发者工具中
* 后台
	* 此文件为代码，尽量不要改动。数据集另附在另一个github项目里面。<br>
	* 训练集和测试集为csv格式，不然会报错，或者可以在代码中修改。
	* 为了方便下载，将代码部分与数据集部分分开存放，所以训练集和两个测试集需要另行下载后放在相应的位置。<br>
	* 训练集复制到  /group7_houtai/train/datasets<br>
	* test1测试集复制到 /group7_houtai/test1/datasets<br>
	* test2测试集复制到 /group7_houtai/test2/datasets<br>
	* 只需要复制里面的csv文件，不要复制文件夹

## 运行说明
* 前端
	* 微信小程序导入项目时更换使用自己的appid，在app.js文件中更换使用自己的"access_token"
* 后台本地代码运行说明：<br>
	* 所有文件夹位置不要动，也不要改名。<br>
	* (1)   运行/group7_houtai/code/datacleaned.py  对数据进行清洗<br>
	* (2)   运行/group7_houtai/code/featuredget.py  进行特征提取<br>
	* (3)   运行/group7_houtai/code/datagena.py  合并数据集<br>
	* (4)   运行/group7_houtai/code/datalable.py  给数据集打标签<br>
	* (4)   运行/group7_houtai/code/train.py         训练<br>
	* (4)   运行/group7_houtai/code/judge.py       利用模型对测试集判断
	* 每个代码中有简单的注释<br>
## 注意事项
<br>运行之前确定数据集已经放在相应位置
<br>数据集必须为 .csv格式
<br>文件夹中的.gitkeep文件只是为了上传GitHub方便
<br>运行之前检查各个文件夹的相对位置是否正确，请和上面的目录结构相对应。
<br>在输出结果的时候约定normal(NORMAL), ball(B), outer race(OR), inner race(IR)的预测输出标签为0, 1, 2, 3。