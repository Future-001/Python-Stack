# 2.完成一个商城购物车的程序。
# 商品信息在shopping.txt文件中存储的，存储形式：
goods="""name price
电脑 1999
鼠标 10
游艇 20
美女 998
"""
with open('shopping.txt',encoding='utf-8',mode='w') as f :
    f.write(goods)
# 要求:
# 1.txt，用户先给自己的账户充钱：比如先充3000元。
account_balance=0
while 1:
    print('账户余额为 {0}'.format(account_balance))
    anwser=input('是否充值余额(y充值,q退出）:>>> ')
    if anwser.upper() == 'Q':
        break
    elif anwser.upper() == 'Y':
        account_balance = input('请输入充值金额:>>> ')
        if account_balance.isdecimal():
            account_balance=int(account_balance)
            print('账户余额为 {0}'.format(account_balance))
            break
        else:
            print('请输入纯数字！')
    else :
        print('输入非法！')

# 2，读取商品信息文件将文件中的数据转化成下面的格式：
# goods = [{"name": "电脑", "price": 1999},
# {"name": "鼠标", "price": 10},
# {"name": "游艇", "price": 20},
# {"name": "美女", "price": 998},]
with open('shopping.txt',encoding='utf-8',mode='r') as f ,\
    open('shopping1.txt', encoding='utf-8', mode='w') as f1:
    goods =[]
    l = ['name','price']
    f.readline()
    l1 = f.readlines()
    for i in range(len(l1)):
        dic = {}
        t = l1[i].strip()
        for j in range(len(l)):
            dic[l[j]] = (t.split(' '))[j]
        goods.append(dic)
    f1.write(str(goods))


# 3，页面显示 序号 + 商品名称 + 商品价格，如：
# 1.txt 电脑 1999
# 2 鼠标 10
# …
with open('shopping1.txt',encoding='utf-8',mode='r') as f :
    # goods = f.readlines()       # 因为我在写入文件时，将列表转换为了字符串，所以，写入后  读出来后的返回值就是长度为1的列表
    print(f.read(),type(f.read()))  # read读出来的数据就是 字符串类型。那我稍微改改是不是就好了呢,
    # 又遇到一个问题，字符串类型的数据，里面是列表，我怎么只取里面的列表呢？
    print(goods,type(goods))
#  这个问题还是没解决，取巧了，用了上一问题的goods
    for i,j in enumerate(goods):
        print(i+1,j.get('name'),j.get('price'))

# g = [{'name': '电脑', 'price': '1999'}, {'name': '鼠标', 'price': '10'}, {'name': '游艇', 'price': '20'}, \
#       {'name': '美女', 'price': '998'}]
# for i,j in enumerate(g):
#     print(i+1.txt,j.get('name'),j.get('price'))

# 4，用户输入选择的商品序号，然后打印商品名称及商品价格,并将此商品，添加到购物车(自己定义购物车)，用户还可继续添加商品。
paying = []
sum = 0
while 1:
    choice = input('请输入你选择的商品序号(q退出,n结算)>>> ')
    if choice.upper() == 'Q':
        break
    elif choice.isdecimal():
        choice = int(choice)-1
        if choice in range(0,len(goods)):
            print(goods[choice].get('name'),goods[choice].get('price'))
            paying.append(goods[choice])
        else:
            print('没有该商品')
    elif choice.upper() =='N':
        while 1:
            sum=0
            for i in paying:
                sum += int(i.get('price'))
            for g in paying:
                print('你选择的商品是： ', g.get('name'),g.get('price'))
            print('总价为： {} yuan'.format(sum))
            if account_balance<sum:
                dele = input('余额不足，请删除某件商品.请输入你想删除的商品序号:>>> ')
                if dele.isdecimal():
                    dele = int(dele)-1
                    if dele in range(0,len(goods)+1):
                        if goods[dele] in paying:
                            paying.remove(goods[dele])
                            # for f in paying:
                            #     print('你选择的商品是',f.get('name'),g.get('price'))
                        else :
                            print('其中没有该商品')
                else:
                    print('输入有误.')
            else:
                account_balance-=sum
                break
        break
    else:
        print('输入有误,请重新输入！')
print('总金额为： %d yuan,余额为 %d yuan' %(sum,account_balance))

# 5，如果用户输入的商品序号有误，则提示输入有误，并重新输入。
#
# 6，用户输入n为购物车结算，依次显示用户购物车里面的商品，数量及单价，若充值的钱数不足，则让用户删除某商品，直至可以购买，若充值的钱数充足，则可以直接购买。
#
# 7，用户输入Q或者q退出程序。
#
# 8. 退出程序之后，依次显示用户购买的商品，数量，单价，以及此次共消费多少钱，账户余额多少，并将购买信息写入文件。