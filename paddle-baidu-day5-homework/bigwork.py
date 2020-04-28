# !pip install jieba
# !pip install wordcloud

 #!wget https://mydueros.cdn.bcebos.com/font/simhei.ttf # 下载中文字体
# #创建字体目录fonts
# !mkdir .fonts
# # 复制字体文件到该路径
#  !cp simhei.ttf .fonts/
#  !rm -rf .cache/matplotlib

# #安装模型
# !hub install porn_detection_lstm==1.1.0
# !pip install --upgrade paddlehub

from __future__ import print_function
import requests
import json
import re #正则匹配
import time #时间处理模块
import jieba #中文分词
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from PIL import Image
import wordcloud  #绘制词云模块
import paddlehub as hub
from collections import Counter

from matplotlib.font_manager import _rebuild
_rebuild()

def crawl_comments():
    last_id = '240737767121'
    comment_num=0
    #arr是所有的comment列表
    arr = []
    for i in range(50):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        url='https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.11.5&authcookie=null&business_type=17&content_id=15068748500&hot_size=0&last_id='+last_id+'&page=&page_size=20&types=time'
        try:
            response = requests.get(url, headers=headers)
            #print(response.status_code)
            html=response.content.decode()
            # print(html)
            results=re.findall(r'"content":"(.*?)"',html)
            # print(results)
            comment_num+=len(results)
            for i in range(len(results)):
                arr.append(results[i])
            id_list=re.findall(r'"id":"(.*?)"',html)
            last_id=id_list[-1]
            #print(last_id)
        except Exception as e:
            print(e)
    print(comment_num)
    #print(arr)
    return arr

#去除文本中特殊字符并保存txt
def clear_special_char(arr1):
    '''
    正则处理特殊字符
    参数 arr1:原文本
    return: 清除后的文本
    '''
    pre_arr=[]
    f1=open('comment.txt','w')
    for j in range(len(arr1)):
        pre_list=re.findall('[\u4e00-\u9fa5]+',arr1[j],re.S)
        pre=''.join(pre_list)
        pre_arr.append(pre)
        f1.write(pre+'\n')
    f1.close()
    return pre_arr

jieba.load_userdict("newdict.txt")

def fenci(arr2):
    '''
    利用jieba进行分词
    参数 text:需要分词的句子或文本
    return：分词结果
    '''
    str1=''.join(arr2)
    fenci_list=jieba.lcut(str1,cut_all=False)
    return fenci_list

def stopwordslist(filepath):
    '''
    创建停用词表
    参数 filepath:停用词文本路径
    return：停用词list
    '''
    f2=open(filepath,'r',encoding='utf-8')
    stopwordstring=f2.read()
    stopwords_list=stopwordstring.split('\n')
    f2.close()
    return stopwords_list


def movestopwords(arr3):
    '''
    去除停用词,统计词频
    参数 file_path:停用词文本路径 stopwords:停用词list counts: 词频统计结果
    return：词频统计结果
    '''
    file_path = 'cn_stopwords.txt'
    stopwords = stopwordslist(file_path)
    true_list = []
    for word in arr3:
        if word not in stopwords:
            true_list.append(word)
    cipin = {}
    cipin = Counter(true_list)
    return cipin


def drawcounts(counts):
    '''
    绘制词频统计表
    参数 counts: 词频统计结果 num:绘制topN
    return：None
    '''
    num = 10
    name_list = []
    count_list = []
    word_counts_top10 = counts.most_common(num)  # 获取前10最高频的词
    print(word_counts_top10)
    for word in word_counts_top10:
        name_list.append(word[0])
        count_list.append(word[1])
    # 设置显示中文
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体

    plt.figure(figsize=(20, 15))

    plt.bar(range(len(count_list)), count_list, color='r', tick_label=name_list, facecolor='#9999ff', edgecolor='white')

    # 这里是调节横坐标的倾斜度，rotation是度数，以及设置刻度字体大小
    plt.xticks(rotation=45, fontsize=20)
    plt.yticks(fontsize=20)

    plt.legend()
    plt.title('''《青春有你第2季第10期上》评论词频统计表top10''', fontsize=24)
    plt.savefig('/home/aistudio/work/top10.jpg')
    plt.show()
    return

def drawcloud(word_counts):
    '''
    根据词频绘制词云图
    参数 word_counts:统计出的词频结果
    return：none
    '''
    # 词频展示
    mask = np.array(Image.open('background.jpg')) # 定义词频背景
    wc = wordcloud.WordCloud(
        font_path='simhei.ttf', # 设置字体格式
        mask=mask, # 设置背景图
        width = 1000,
        height = 700,
        background_color = "white",
        max_words=200, # 最多显示词数
        max_font_size=100 # 字体最大值
    )
    wc.generate_from_frequencies(word_counts) # 从字典生成词云
    wc.to_file('/home/aistudio/work/WORDCLOUD.jpg') # 保存图像
    #image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
    #wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
    plt.imshow(wc) # 显示词云
    plt.axis('off') # 关闭坐标轴
    plt.show() # 显示图像

def text_detection():
    '''
    使用hub对评论进行内容分析
    return：分析结果

    '''
    test_text=[]
    porn_detection_lstm=hub.Module(name="porn_detection_lstm")
    f3=open('comment.txt','r',encoding='utf-8')
    for line in f3:
        if len(line.strip())==1:
            continue
        else:
            test_text.append(line)
    f3.close()
    input_dict={"text":test_text}
    # 注意这里用的是GPU
    results=porn_detection_lstm.detection(data=input_dict,use_gpu=True,batch_size=1)
    #print(results)
    for index,item in enumerate(results):
        if item['porn_detection_key']=='porn':
            print(item['text'],':',item['porn_probs'])

if __name__ == "__main__":
    list1=crawl_comments()
    #print(list1)
    list2=clear_special_char(list1)
    #print(list2)
    list3=fenci(list2)
    #print(list3)
    dict1=movestopwords(list3)
    #print(dict1)
    drawcounts(dict1)
    drawcloud(dict1)
    text_detection()
    print("success！")
