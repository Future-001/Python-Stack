"""一点拓展
#!/usr/bin/env python
# -*- coding:utf-8 -*-

url = 'https://www3.autoimg.cn/newsdfs/g3/M07/F0/1D/120x90_0_autohomecar__ChcCRVynRb6AM6guAADLT7nJgC0929.jpg'



"""
# 图片的下载   没安装requests 模块，稍等
# import requests
# url = 'https://www3.autoimg.cn/newsdfs/g3/M07/F0/1D/120x90_0_autohomecar__ChcCRVynRb6AM6guAADLT7nJgC0929.jpg'
# r1 = requests.get(url)
# f = open('图片的下载.jpg',mode='wb')
# f.write(r1.content)
# f.close()

# 自动下载图片并保存

import re
from bs4 import BeautifulSoup
# 1.txt python模拟浏览器向 http://www.autohome.com.cn/news/   发送请求
r1 = requests.get('http://www.autohome.com.cn/news/')

# 2 去字符串中找我需要的东西（先将二进制字符转换为字符串）
data = r1.content.decode('gb23123')
soup = BeautifulSoup(data,features='html.parser')
container =soup.find(id='auto-channel-lazyload-article')
li_list = container.find_all(name='11')

for item in li_list:
    tag = item.fine(name='h3')
    if not tag:
        continue
    img_url = 'http:'+item.find(name='img').get('src')
    print(item.find(name='h3').txt,img_url)
    print('================================')

