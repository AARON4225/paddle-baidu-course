# 作业二：查找特定名称文件
# 遍历”Day1-homework”目录下文件；
# 找到文件名包含“2020”的文件；
# 将文件名保存到数组result中；
# 按照序号、文件名分行打印输出。

# 导入OS模块
import os
import re
# 待搜索的目录路径
path = "Day1-homework"
# 待搜索的名称
filename = "2020"
# 定义保存结果的数组
result = []
def findfiles():
    for root,dirs,files in os.walk(path):
        for i in files:
            if re.search("2020",i):
                t="%s\%s"%(root,i)
                result.append(t)
    for j in range(len(result)):
        print("[",j+1,",'",result[j],"']")

if __name__ == '__main__':
    findfiles()