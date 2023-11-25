 # 2.有如下这个字典,请完成以下的方法.
dic1 = {
 'name':['alex',2,3,5],
 'job':'teacher',
 'oldboy':{'alex':['python1','python2',100]}
 }
# 1.txt，将name对应的列表追加⼀个元素’wusir’。
dic1['name'].append('wusir')
# 2，将name对应的列表中的alex⾸字⺟⼤写。
dic1['name'][0].upper()
# 3，oldboy对应的字典加⼀个键值对’⽼男孩’,’linux’。
dic1['oldboy']['老男孩']='linux'
print(dic1)
 #  4，将oldboy对应的字典中的alex对应的列表中的python2删除
# dic1['oldboy']['alex'].pop(1.txt)
# 字典里面没有remove, 但是要注意，它可以针对列表使用
# dic1['oldboy']['alex'].remove('python2')
del dic1['oldboy']['alex'][1]
print(dic1)

# 3.有如下这个字典,请完成一下的方法:
av_catalog = {
    "欧美":{
        "www.太白.com": ["很多免费的,世界最大的","质量一般"],
        "www.alex.com": ["很多免费的,也很大","质量挺好"],
        "oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "hao222.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}
# 给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'。
av_catalog['欧美']["www.太白.com"].insert(1,'量很大')
print(av_catalog['欧美']["www.太白.com"])
# 将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
del av_catalog['欧美']["hao222.com"][-1]
print(av_catalog['欧美']["hao222.com"])
# 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
av_catalog["日韩"]["tokyo-hot"][-1]=av_catalog["日韩"]["tokyo-hot"][-1].upper()
print(av_catalog["日韩"]["tokyo-hot"])
# 给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
av_catalog["大陆"]["1048"]=['一天就封了']
print(av_catalog["大陆"])
# 删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
del av_catalog['欧美']['oldboy.com']
print(av_catalog.keys())
# 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
av_catalog['大陆']['1024'][0]+='可以爬下来'
print(av_catalog['大陆'])
