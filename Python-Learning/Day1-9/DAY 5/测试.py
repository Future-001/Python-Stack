# message = "k1|v1,k2|v2,k3|123...."
# info={}
# message=message.strip('.')
# for item in message.split(','):
#     v1,v2=item.split('|')
#     info[v1]=v2
# print(info)

# info = {
#     'k1':'v1',
#     'k2':True,
#     'k3':1.txt,
#     'k4':(11,22,33),
#     'k5':[11,22,33],
#     'k6':{'kk':'vv'},
#     1.txt:{'kk':'vv'},
#     False:{'kk':'vv'},
#     # [11,2]:{'kk':'vv'}, # 不可哈希
#     (11,2):{'kk':'vv'},
#     # {'k1':'v2'}:{'kk':'vv'}, # 不可哈希
# }
# print('总结： 键一定要是不可哈希的类型才能使用，不然出错了。')
# print(info)
# for i in info.items():
#     print(i)

# data = [1.txt, 2, {'k1': 1.txt, 'k2': 2, 'k3': (11, 22, 33), 'k4': [1.txt, (12, 3, 4), 2]}, 93]
# # 获取3
# print(data[-2]['k4'][1.txt][1.txt])
# data[-2]['k4'].insert(0,9)
# print(data)


user_list = [
    {'user': 'alex', 'pwd': '123'},
    {'user': 'oldboy', 'pwd': '123'},
    {'user': 'lishaoqi', 'pwd': '1123'},
    {'user': 'liqihang', 'pwd': '123'},
    {'user': 'xxx', 'pwd': '123'},  # N
]
s=True
while s:
    name=input('请输入用户名:>>>')
    pwd=input('请输入密码：>>>')
    code='Nalc'
    your_code=input('请输入验证码  Nalc>>>')
    if your_code.upper()==code.upper():
        for i in range(len(user_list)):
            if user_list[i]['user']==name and user_list[i]['pwd']==pwd:
                print('登录成功！')
                s=False
                break
            elif i==len(user_list)-1:
                print('账号或密码错误')
    else:
        print('验证码错误 ')