# # 练习：打印：0 ~ 100之间的偶数。
# # for i in range(0,101):
# #     if i % 2 == 0:
# #         print(i)
#
# # for i in range(0,101,2):
# #     print(i)
#
# # 练习：goods = ['汽车','飞机','大炮']
# # goods = ['汽车','飞机','大炮']
# #
# # for i in range(0,len(goods)):
# #     print(i,goods[i])
# # num = input('请输入要选择的商品序号：')
# # num = int(num)
# #
# # text = "您选择的是：%s" %(goods[num],)
# # print(text)
#
# # 练习：goods = ['汽车','飞机','大炮']
# # goods = ['汽车','飞机','大炮']
# #
# # for i in range(0,len(goods)):
# #     print(i+1.txt,goods[i])
# # num = input('请输入要选择的商品序号：')
# # num = int(num) - 1.txt
# # text = "您选择的是：%s" %(goods[num],)
# # print(text)
#
# # 5. 写代码，有如下列表，利用切片实现每一个功能
# """
# #
# #    ```python
# #    li = [1.txt, 3, 2, "a", 4, "b", 5,"c"]
# #    ```
# #
# #    - 通过对li列表的切片形成新的列表 [1.txt,3,2]
# #    - 通过对li列表的切片形成新的列表 ["a",4,"b"]
# #    - 通过对li列表的切片形成新的列表  [1.txt,2,4,5]
# #    - 通过对li列表的切片形成新的列表 [3,"a","b"]      li[1.txt:-1.txt:2]
# #    - 通过对li列表的切片形成新的列表 [3,"a","b","c"]  li[1.txt::2]
# #    - 通过对li列表的切片形成新的列表  ["c"]
# #    - 通过对li列表的切片形成新的列表 ["b","a",3]
# """
#
# # 6. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
# """
#    ```python
#    0 武沛齐
#    1.txt 景女神
#    2 肖大侠
#    ```
# """
# # 7. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：
# """
#    ```python
#    1.txt 武沛齐
#    2 景女神
#    3 肖大侠
#    ```
# """
# # 8. 写代码，有如下列表，按照要求实现每一个功能。
# """
#    ```python
#    lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1.txt"]], 89], "ab", "adv"]
#    ```
#    - 将列表lis中的"k"变成大写，并打印列表。
#         lis[2] = "K"
#         lis[2] = lis[2].upper()
#
#         lis[3][0] = lis[3][0].upper()
#    - 将列表中的数字3变成字符串"100"
#         li[1.txt] = '100'
#    - 将列表中的字符串"tt"变成数字 101
#         li[3][2][1.txt][0] = 101
#    - 在 "qwe"前面插入字符串："火车头"
#         li[3].insert(0,'火车头')
# """
#
# # 9. 写代码实现以下功能
# """
#    - 如有变量 googs = ['汽车','飞机','火箭'] 提示用户可供选择的商品：
#
#      ```python
#      0,汽车
#      1.txt,飞机
#      2,火箭
#      ```
#
#    - 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。
# """
#
# # 10. 请用代码实现
# """
#     li = "alex"
#     利用下划线将列表的每一个元素拼接成字符串"a_l_e_x"
#     value = "_".join(li)
#
#     # 练习一： users = ['贺鹏飞','朱海','城根'] 通过，将列表中的元素拼接："贺鹏飞,珠海,城根"
#     # users = ['贺鹏飞','朱海','城根']
#     # users = ('贺鹏飞','朱海','城根')
#     # result = ",".join(users)
#     # print(result)
#
# """
#
# # 11. 利用for循环和range找出 0 ~ 100 以内所有的偶数，并追加到一个列表。
# """
# data_list = []
# for i in range(0,101):
#     if i % 2 == 0:
#         data_list.append(i)
#
#
# data_list = []
# for i in range(0,101,2):
#     data_list.append(i)
# """
# # 12. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。
# """
# data_list = []
# for i in range(0,51):
#     if i % 3 == 0:
#         data_list.append(i)
# print(data_list)
# """
# # 13. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：
# """
# data_list = []
# for i in range(0,51):
#     if i % 3 == 0:
#         data_list.insert(0,i)
# print(data_list)
# """
#
# # 14. 查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。
# """
#     ```python
#     li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
#     ```
# """
#
# """
# li = ["TaiBai ", "alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
# data_list = []
# for item in li:
#     item = item.strip()
#     if item.startswith('a'):
#         data_list.append(item)
#
# for item in data_list:
#     print(item)
# """
#
# # 15. 判断是否可以实现，如果可以请写代码实现。
# """
#     ```python
#     li = ["alex",[11,22,(88,99,100,),33] "WuSir", ("ritian", "barry",), "wenzhou"]
#     ```
#     - 请将 "WuSir" 修改成 "武沛齐"
#     - 请将 ("ritian", "barry",) 修改为 ['日天','日地']
#     - 请将 88 修改为 87
#     - 请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "文周"
#         del li[-1.txt]
#         li.insert(0,'文周')
#     - 请将 "wenzhou" 删除，然后再在列表第0个索引位置插入 "wenzhou"
#         deleted = li.pop()
#         li.insert(0,deleted)
# """
#
# # 16. 面试题 & 书写规范
# """
# v1 = 1.txt
# v2 = (1.txt)
# v3 = (1.txt,)
# print(type(v1),type(v2),type(v3))
# """
# # data = [(1.txt),(2),(3)] # [1.txt,2,3]
#
#
# # 17. 用户输入
# # content = input("请输入：") # 5 + 99+7+  2+ uu + 7y ...
# """
# total = 0
# content = "5 + 99+7+  2+ uu + 7y"
# num_list = content.split('+') # ["5  ",' 99',"7",'  2', ' uu '..]
# for item in num_list:
#     item = item.strip()
#     if item.isdigit():
#         total += int(item)
# print(total)