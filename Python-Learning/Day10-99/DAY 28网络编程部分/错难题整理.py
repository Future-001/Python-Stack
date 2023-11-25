# 判断一个字典中是否有这些key： ‘AAA’,’BB’,’C’,’DD’,’EEE’(不使用for while)
re = any(['AAA','BBB','C','DD','EEE']) in {'AAA':123,"BB":1,'C':111,'DD':222,'EEE':999}
print(re)
# 这里错误的原因是 any 是其中的元素有一个为真就为真,所以 True 肯定不在字典里面了。
print(('AAA','BBB','C','DD','EEE') in {'AAA':123,"BB":1,'C':111,'DD':222,'EEE':999})

# 一种方法，集合的子集，但觉得不是最好的，只能判断都在
s1 = {'AAA','BBB','C','DD','EEE'}
print(s1.issubset({'AAA':123,"BB":1,'C':111,'DD':222,'EEE':999}.keys()))  # 还是不对
