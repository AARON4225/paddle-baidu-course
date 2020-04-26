# 利用pandas库绘制饼状图(another_way)

import matplotlib.pyplot as plt
import numpy as np
import json
import matplotlib.font_manager as font_manager

#显示matplotlib生成的图形
#%matplotlib inline

with open('data/data31557/20200422.json', 'r', encoding='UTF-8') as file:
         json_array = json.loads(file.read())

weights=[]
counts=[]

for star in json_array:
    weight=float(star['weight'].replace('kg',''))
    weights.append(weight)
#    print(weight)

size_list=[]
count_list=[]

size1=0
size2=0
size3=0
size4=0

for weight in weights:
    if weight <= 45:
        size1+=1
    elif 45<weight<=50:
        size2+=1
    elif 50<weight<=55:
        size3+=1
    else:
        size4+=1
labels='<=45kg','45~50kg','50~55kg','>55kg'
sizes=[size1,size2,size3,size4]

explode=(0.1,0.05,0,0)

fig1,ax1=plt.subplots()
ax1.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax1.axis('equal')
plt.savefig('work/result/pie_result01.jpg')
plt.show()