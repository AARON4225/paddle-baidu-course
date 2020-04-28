# 爬取百度图片中《青春有你2》中前五位参赛选手信息，返回页面数据
import json
import re
import requests
import datetime
from bs4 import BeautifulSoup
import os

#arr是所有的comment列表
arr = []
def crawl_comments():
    last_id = '240737767121'
    comment_num=0
    for i in range(50):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        url='https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.11.5&authcookie=null&business_type=17&content_id=15068748500&hot_size=0&last_id='+last_id+'&page=&page_size=20&types=time'
        try:
            response = requests.get(url, headers=headers)
            print(response.status_code)
            html=response.content.decode()
            # print(html)
            results=re.findall(r'"content":"(.*?)"',html)
            # print(results)
            comment_num+=len(results)
            write_comments(results)
            id_list=re.findall(r'"id":"(.*?)"',html)
            last_id=id_list[-1]
            print(last_id)
        except Exception as e:
            print(e)
    print(comment_num)

def write_comments(comments):
    f1=open('comment.txt','a',encoding='utf-8')
    for i in range(len(comments)):
            #f1.write(comments[i]+'\n')
            arr.append(comments[i])
    f1.close()

def write_star_name():
    with open('20200428.json', 'r', encoding='UTF-8') as file:
        json_array = json.loads(file.read())
    f2=open('newdict.txt','a',encoding='utf-8')
    for star in json_array:
        name = star['name']
        f2.write(name+' '+'9999\n')
    f2.close()

if __name__ == '__main__':
    # crawl_comments()
    # print(arr)
    write_star_name()
    print("success！")
