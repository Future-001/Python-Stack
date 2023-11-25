# print('=======================join======================')
# print('将列表转化为字符串类型：')
# s1=['李荣浩','张柏芝','陈冠希']
# s2="+".join(s1)
# print(s2)
#
# print()
# print(7//3)
#
#
# count = 3
#
# while count > 0:
#     user = input("user:")
#     pwd = input("password:")
#     if user == 'alex' and pwd == 'alex3714':
#         print("登录成功！")
#         break
#     else:
#         print(f"你是Alex吗?这都记不住！剩余次数{count - 1.txt}")
#     count -= 1.txt
#
# print('asdgaeda '.split('a'))
#
# s=input('请输入内容：')
# print(s.count('s'))

# 8.使用while循环分别正向和反向对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言。" 进行打印。
# msg = "伤情最是晚凉天，憔悴厮人不堪言。"
# i=0
# while i<len(msg):
#     print(msg[i])
#
#     i+=1.txt
#     print(msg[-i])

# s=input('请输入内容：')
# print(s[:4].count('a'))

# content=input('请输入字符串:')
# count=0
# for i in content:
#     if i.upper()==i:
#         count+=1.txt
# print(count)
#
# le=len(content)
# i=0
# count=0
# while i<le:
#     if content[i].upper()==content[i]:
#         count+=1.txt
#     i+=1.txt
# print(count)

# content=input('请输入字符串:')
# cap_count=0
# num_count=0
# min_count=0
# for i in content:
#     if i.isdecimal()==True:
#         num_count+=1.txt
#     if i.isalpha():
#         if i.upper()==i:
#             cap_count+=1.txt
#         if i.lower()==i:
#             min_count+=1.txt
# print('大写字母数量是'+str(cap_count), '小写字母数量是{} 有{}个数字'.format(min_count,num_count) )


# s=input('请输入：')
# j=1.txt
# for i in s:
#     if i==s[-j]:
#         j+=1.txt
#     else :
#         print('不是回文')
#         break
#     if j==len(s):
#         print('是回文')

# print(' 采用方式一 字符串相等 ：')
# s=input('请输入：')
# s1=s[-1.txt::-1.txt]
# if s1==s:
#     print('是回文！')
# else :
#     print('不是回文')


# while 1.txt:
# # 输入A，则显示走大路回家，然后在让用户进一步选择：
#     select=input('请输入选择 A B C：')
#     if select.upper()=='A':
#         print('走大路回家。')
# # 是选择公交车，还是步行？
#         select2 = input('请输入回家的方式：')
#         # 选择公交车，显示10分钟到家，并退出整个程序。
#         if select2 =='公交车':
#             print('10分钟到家')
#             break
#         # 选择步行，显示20分钟到家，并退出整个程序。
#         if select2 == '步行':
#             print('20分钟到家')
#             break
# # 输入B，则显示走小路回家，并退出整个程序。
#     elif select.upper()=='B':
#         print('走小路回家。')
# # 输入C，则显示绕道回家，然后在让用户进一步选择：
#     elif select.upper()=='C':
#         print('绕道回家。')
# # 是选择游戏厅玩会，还是网吧？
#         select3=input('游戏厅 or 网吧：')
#         # 选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
#         if select3=='游戏厅':
#             print('一个半小时到家，爸爸在家，拿棍等你。')
#             continue
#         # 选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。
#         if select3=='网吧':
#             print('两个小时到家，妈妈已做好了战斗准备。')
#             continue
#     print('输入错误，请重新输入！')


# num1 = input("请输入：") # asdfd123sf2312
# num2 = input("请输入：") # a12dfd183sf23
# str1=str2=''
# for i in num1:
#     if i.isdecimal():
#         str1+=''.join(i)
#         print(str1)
# for i in num2:
#     if i.isdecimal():
#         str2 += ''.join(i)
#         print(str2)
# print(str1,str2)
# print(int(str1)+int(str2))

print(" 采用方式一 字符串相等 ：")