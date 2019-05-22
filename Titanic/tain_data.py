import os
import numpy as np # 科学计算
import pandas as pd # 数据分析
import matplotlib.pyplot as plt # 制图

# 设置字体
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/Library/Fonts/Songti.ttc')

print(os.getcwd())
data_train = pd.read_csv("/Users/hongliang/Desktop/Kaggle/Titanic/dataset/train.csv")

print(data_train)

data_train.describe() # 数据的描述性统计

# 1、乘客的属性分布
# fig = plt.figure()
# fig.set_size_inches(12, 12)     #设置画布尺寸

# 获救人数
# plt.subplot2grid((2,2),(0,0))   # 展示的图表在一个2x2的网格中，它的位置是左上，因为坐标是(0,0)
data_train.Survived.value_counts().plot(kind='bar')
plt.title("获救情况 (1为获救)", fontproperties=font)
plt.ylabel("人数",fontproperties=font)
plt.show()


# 乘客等级人数分布
# plt.subplot2grid((2,2),(0,1))  # 图表的位置在右上，因为坐标是(0,1)
# data_train.Pclass.value_counts().plot(kind='bar')
# plt.title("乘客等级人数分布情况",fontproperties=font)
# plt.ylabel("人数",fontproperties=font)

# 乘客性别的人数分布
# plt.subplot2grid((2,2),(1,0))
# data_train.Sex.value_counts().plot(kind='bar')
# plt.title("乘客性别人数分布情况",fontproperties=font)
# plt.ylabel("人数",fontproperties=font)

#
# plt.subplot2grid((2,2),(1,1))
# data_train.Age[data_train.Pclass == 1].plot(kind='kde')   
# data_train.Age[data_train.Pclass == 2].plot(kind='kde')
# data_train.Age[data_train.Pclass == 3].plot(kind='kde')
# plt.xlabel(u"年龄")# plots an axis lable
# plt.ylabel(u"密度") 
# plt.title(u"各等级的乘客年龄分布")
# plt.legend((u'头等舱', u'2等舱',u'3等舱'),loc='best')