import requests
# ret = requests.get('https://www.baidu.com/')
# print(ret.content.decode('utf-8'))

# import requests
# ret = requests.get('https://movie.douban.com/top250?start=0&amp;filter=')
# print(ret.content.decode('utf-8'))
# print(ret.text)

import requests
ret = requests.get('http://www.csdn.com/')
print(ret.content.decode('utf-8'))