s =' slgfjsgoaetp[a hsktl '
# 不用len 获取代码的长度。
print(s.index('l '))

# 怎么会忘记 for 呢？？？？？？？？？尬住了
count=0
for i in s:
    count+=1
print(count)

ll = [1,2,3,4,5]
count=0
for j in ll:
    count+=1
print(count)


# 这样写代码太low了，重复代码太多，，，，代码的可读性太差了

def my_len(s):
    count = 0
    for i in s:
        count+=1
    print(count)

print(my_len(ll))


