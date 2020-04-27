# 爬取百度图片中《青春有你2》中前五位参赛选手信息，返回页面数据
import json
import re
import requests
import datetime
from bs4 import BeautifulSoup
import os

name=['yushuxin',
      'xujiaqi',
      'zhaoxiaotang',
      'anqi',
      'wangchengxuan']

# 爬取每个选手的百度百科图片，并进行保存
# def crawl_pic_urls():
#     '''
#     爬取每个选手的百度百科图片，并保存
#     '''
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
#     }
#     url='https://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1587902681650_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&ctd=1587902681652%5E00_1652X817&sid=&word=%E7%8E%8B%E6%89%BF%E6%B8%B2%E4%B8%AA%E4%BA%BA%E7%85%A7%E7%89%87'
#     try:
#         response = requests.get(url, headers=headers)
#         print(response.status_code)
#         html=response.content.decode()
#         results=re.findall('"objURL":"(.*?)",',html)
#
#         down_pic(results)
#     except Exception as e:
#         print(e)

# def down_pic(pic_urls):
#     '''
#     根据图片链接列表pic_urls, 下载所有图片，保存在以name命名的文件夹中,
#     '''
#     path = 'train/'  + name + '/'
#
#     if not os.path.exists(path):
#         os.makedirs(path)
#
#     for i, pic_url in enumerate(pic_urls):
#         try:
#             pic = requests.get(pic_url, timeout=15)
#             string = str(i + 1) + '.jpg'
#             with open(path + string, 'wb') as f:
#                 f.write(pic.content)
#                 print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
#         except Exception as e:
#             print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
#             print(e)
#             continue

def write_pic_path():
    for i in range(5):
        f1=open('train_list.txt','a')
        pic_num = 0
        for (dirpath, dirnames, filenames) in os.walk('train/'+name[i]+'/'):
            for filename in filenames:
                f1.write('train/'+name[i]+'/'+filename+' '+str(i)+'\n')
                pic_num += 1
        f1.close()

if __name__ == '__main__':

  # 从每个选手的百度百科页面上爬取图片,并保存
  #   crawl_pic_urls()
    write_pic_path()
    print("所有信息爬取完成！")
