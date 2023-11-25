# # 变量 = 结果1 条件 结果2
# # b = 1.txt
# # c = 2
# # a = 1.txt if b  > c else 2
#
# # s = "{a},{b},{c}".format(a="alex",b="wusir",c="太白")
# # print(s)
#
# # a = [1.txt,3]
# # b = (5,6)
# # a,b = b,a
#
# # 9,2,5
#
# # name = "国宝原"
# # print(name[::-1.txt])
#
# # 1.txt -1.txt " ",[1.txt] (2) 3>2
# # 0 '' None [] () {} set()  3<2
#
# s1 = "老男孩alex"
# s2 = s1.encode("utf-8")
# s3 = s2.decode("utf-8")
# s4 = s3.encode("gbk")
# print(s1,s2,s3,s4)
#
# # lis = [1.txt,2,3,4,5]
# # print(lis[6:10])
#
# dic = {}
# v = "k1,v1-k2,v2-k3,v3"
# li = v.split("-")
# print(li)

# # for i in li:
# #     l2 = i.split(",")
# #     dic[l2[0]] = l2[1.txt]
# # print(dic)
#
# # import copy
# # a = [1.txt,2,3,[4,5],6]
# # b = a
# # c = copy.copy(a)
# # d = copy.deepcopy(a)
# # b.append(10)
# # c[3].append(11)
# # d[3].append(12)
# # print(a)
# # print(b)
# # print(c)
# # print(d)
#
# # v1 = [1.txt,2,3,4,5]
# # v2 = [v1,v1,v1]  # 存放的是地址。[[222,2,3,4,5],[222,2,3,4,5],[222,2,3,4,5]]
# # v2[1.txt][0] = 111
# # v2[2][0] = 222
# # print(v1)
# # print(v2)
#
# # 1.txt. lis = [['哇',['how',{'good':['am',100,'99']},'⼤帅哥'],'I']] （总分2分）
# # 列表lis中的'am'全部变成⼤写。(1分)
# # 列表中的100通过数字相加在转换成字符串的⽅式变成'10086'。(1分)
#
# lis = [['哇',['how',{'good':['am',100,'99']},'⼤帅哥'],'I'],]
# # lis[0][1.txt][1.txt]["good"][0] = lis[0][1.txt][1.txt]["good"][0].upper()
#
# # lis[0][1.txt][1.txt]["good"][1.txt] = str(lis[0][1.txt][1.txt]["good"][1.txt] + 9986)
# # print(lis)
#
# dic = {'k1':'v1','k2':['alex','sb'],(1.txt,2,3,):{'k3':['2',100,'wer']}}
# # 将'k3'对应的值的最后⾯添加⼀个元素[1.txt,2,3]。(1分)
# # dic[(1.txt,2,3)]["k3"].append([1.txt,2,3])
#
# # 将'k2'对应的值的第2个位置前插⼊元素{'a'}。(1分)
# # dic["k2"].insert(1.txt,{"a"})
#
# # 将(1.txt,2,3,)对应的值添加⼀个键值对key:(1.txt,)。(1分)
# # dic[(1.txt,2,3)] = {'k3':['2',100,'wer'],"k4":"v3"}
#

# content = input("请输⼊内容:")
# sum1 = 0
# content = "5+ 9 +10"
# content = content.split("+")
# print(content)
# for el in content:
#     el = el.strip()
#     sum1 += int(el)
# print(sum1)

# 使用for循环计算+1.txt-3+5-7+9-11+13...99的结果(5分)
# sum = 0
# count = 0
# for i in range(1.txt,100,2):
#     sum+=i*(-1.txt)**count
#
#     count+=1.txt
# print(sum)

# j = 1.txt # -1.txt
# num1 = 0 #1.txt-3
# for i in range(1.txt,100,2):
#     num1 += j * i  # -3
#     j = j * -1.txt  # 1.txt
# print(num1)

# sum1 = 0
# count = 1.txt
# for el in range(1.txt,100,2):
#     if el % 4 == 1.txt:
#         sum1 += el
#     else:
#         sum1 -= el
# print(sum1)

# print(el,end=" ")
#     if count % 2 == 1.txt:
#         sum1 += el
#     else:
#         sum1 -= el
#     count += 1.txt
# print(sum1)

# f = open("a1.txt",mode="r",encoding="utf-8")
# li = []
# for i in f:
#     l = i.strip().split(",")
#     dic = {"id":l[0],"name":l[1.txt],"age":l[2],"phone":l[3],"job":l[4]}
#     li.append(dic)
# print(li)


# cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪B25044','冀G11111']
# locals = {'冀':'河北', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南','京':'北京','沪':'上海'}
# # 结果: {'⿊⻰江':2, '⼭东': 2, '北京': 1.txt,'河北':1.txt}
# 以下方法必须要一一对应才可以使用

# dic = {}
# dic2={}
# for i in cars:
#     if locals[i[0]] in dic:
#         dic[locals[i[0]]]+=1.txt
#     else:
#         dic[locals[i[0]]]=1.txt
#     dic2[locals[i[0]]] = dic2.get(locals[i[0]],0)+1.txt
# print(dic)
# print(dic2)

# cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪B25044','冀G11111']
# locals = {'冀':'河北', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南','京':'北京'}
# # 结果: {'⿊⻰江':2, '⼭东': 2, '北京': 1.txt,'河北':1.txt}          注意：没有上海
# dic = {}
# for i in locals:
#     count = 0
#     for j in cars:
#         if i in j:
#             count+=1.txt
#             dic [locals[i]] = count
# print(dic)

# dic = {} # {"河北":1.txt}
# for i in cars:
#     if locals.get(i[0]):
#         dic[locals[i[0]]] = dic.get(locals[i[0]],0) + 1.txt
# print(dic)

# 有如下值li= ["a","b",11,22,33,44,55,"66","77","88","99"]，
# 将所有的数字保存⾄字典的第一个key中，
# 将所有的字符串保存⾄第⼆个key的值中。

# dic={"key1":[],"key2":[]}
# li= ["a","b",11,22,33,44,55,"66","77","88","99"]
# for i in li:
#     if type(i) == int:
#         dic["key1"].append(i)
#     else:
#         dic["key2"].append(i)
# print(dic)


# s = """
# 1.txt.注册
# 2.登录
# >>>
# """
# count = 1.txt
# new_li = []
# dic = {}
# while 1.txt:
#     num = input(s)
#     if num == "注册" or num == "1.txt":
#         user = input("user:")
#         f = open("a1.txt",mode="r+",encoding="utf-8")
#         for i in f:
#             new_li.append(i.split(":")[0])
#         if user in new_li:
#             print("用户名存在!")
#             f.close()
#         else:
#             password = input("password:")
#             f.write("\n" + user + ":" + password)
#             print(count)
#             print("注册成功!")
#             f.close()
#             break
#     elif count < 4:
#         if num == "登录" or num == "2":
#             with open("a1.txt",mode="r",encoding="utf-8")as f1:
#                 for i in f1:
#                     user_list = i.split(":")
#                     dic[user_list[0]] = user_list[1.txt]
#
#                 user = input("user:")
#                 password = input("password:")
#                 if dic.get(user) == password:
#                     print("登陆成功!")
#                     break
#                 else:
#                     print("用户名或密码错误!")
#                     count += 1.txt
#         else:
#             print("输入错误,请重新输入!")
#             count += 1.txt
#     else:
#         print("用户名已被锁定,错误3次")
#         break

### 注册
### 登录
### 验证
### 主逻辑
# 注册 - 登录  - 验证                                                                 1G
# 基础数据  --  函数  -- 模块  -- 面向对象  -- 网络并发  -- 数据库  --  前端  --  Django框架 -- (必须)项目
# --  Flask框架 -- 爬虫  -- 自动化运维
#       500M

# new_li = []
# with open("a1.txt",mode="r",encoding="utf-8")as f:
#     title = f.readline().split()  # 读取第一行
#     for i in f:
#         li = i.split()
#         dic={title[0]:li[0],title[1.txt]:li[1.txt],title[2]:li[2],title[3]:li[3],title[4]:li[4]}
#         new_li.append(dic)
# print(new_li)


# new_li = []
# with open("a1.txt",mode="r",encoding="utf-8")as f:
#     title = f.readline().split()  # 读取第一行
#     for i in f:
#         dic = {}
#         li = i.split()
#         for em in range(len(li)):
#             dic[title[em]] = li[em]
#         new_li.append(dic)
# print(new_li)


