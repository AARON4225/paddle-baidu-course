# 利用pandas库绘制饼状图
import matplotlib.pyplot as plt
import numpy as np
import json
import matplotlib.font_manager as font_manager
import pandas as pd

#显示matplotlib生成的图形
# %matplotlib inline
df = pd.read_json('data/data31557/20200422.json')
#print(df)

weights=df['weight']
arrs=weights.values

for i in range(len(arrs)):
    arrs[i]=float(arrs[i][0:2])
bin=[0,45,50,55,100]
sel=pd.cut(arrs,bin)
print(sel)
pd.value_counts(sel)
sizes=pd.value_counts(sel)
print(sizes)
explode=(0.1,0.1,0,0)
labels='45~50kg','<=45kg','50~55kg','>55kg'
fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.savefig('work/result/pie_result02.jpg')
plt.show()
