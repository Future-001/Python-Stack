# 看代码分析结果
"""=============================== 不太理解的========================="""
func_list = []

for i in range(10):
    func_list.append(lambda: i)

v1 = func_list[0]()
v2 = func_list[5]()
print(v1, v2)

# 看代码分析结果
#
# func_list = []
#
# for i in range(10):
#     func_list.append(lambda x: x + i)
#
# for i in range(0, len(func_list)):
#     result = func_list[i](i)
#     print(result)


# 看代码分析结果
#
func_list = []

for i in range(10):
    func_list.append(lambda x: x + i)

v1 = func_list[0](2)
v2 = func_list[5](1)
print(v1, v2)


# 看代码写结果【面试题】
print()
def func(name):
    v = lambda x: x + name
    return v
v1 = func('武沛齐')
v2 = func('alex')
v3 = v1('银角')
v4 = v2('金角')
print(v1, v2, v3, v4)

# 看代码写结果
#
# NUM = 100
# result = []
# for i in range(10):
#     func = lambda: NUM  # 注意：函数不执行，内部代码不会执行。
#     result.append(func)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)


# 看代码写结果【面试题】
#
# result = []
# for i in range(10):
#     func = lambda: i  # 注意：函数不执行，内部代码不会执行。
#     result.append(func)
#
# print(i)
# print(result)
# v1 = result[0]()
# v2 = result[9]()
# print(v1, v2)