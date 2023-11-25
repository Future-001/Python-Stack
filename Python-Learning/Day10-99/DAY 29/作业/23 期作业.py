# 使用基于TCP协议的socket套接字，完成qq聊天的功能（连接+通信循环）。
#  服务端：
        #  服务端模拟qq客服，可以与客户实现正常聊天。
        #  服务端可以选择勿扰模式，如果选择勿扰模式，则给客户端统一回复：‘您好，我现在有事不在，请稍后联系’。
        #  客户在正常（非正常退出）时，服务端不受影响运行正常。
#  客户端：
        #  客户端可以实现与qq客户的正常聊天。
        #  客户端可以选择正常退出聊天。
        #  使用基于TCP协议的socket套接字，完成一个用户登录认证的需求。

# 服务端：
# 等待客户端来发送数据：用户名，密码（密文）。
# 本地文件查看用户名密码是否合法。
# 给客户端返回登录成功与否的信息：合法：登录成功。否则：用户名或者密码错误。
# 客户端：
# 用户输入： 用户名，密码。
# 将用户名以及密文密码发送到服务端进行校验。
# 接收服务端的验证消息。



# 面试题小练习：
# 将列表中得元素根据位数合并成字典
lst = [1,2,4,6,8,16,32,64,128,256,512,1024,32769,65536,4294967296,]
# {1:[1,2,4,6,8],2:[16,32,64,],3:[128,256,512,],4:[1024,],5:[32769,65536,],10:[4294967296],}
dic = {}
for i in lst:
    if len(str(i)) not in dic:
        dic[len(str(i))]=[i,]
    else:
        dic[len(str(i))].append(i)
print(dic)

# 方法2：
dic2 = {}
for j in lst:
    dic2[len(str(j))].append(j) if dic2.get(len(str(j))) else dic2.setdefault(len(str(j)),[j,])
    # 这里之前被我改错了，好像是不能在判断的表达式里面赋值来着
print(dic2)

# 请用尽量简洁的方法将二位数组转化成一维数组lst = [[1,2,3],[4,5,6],[7,8,9]]
lst = [[1,2,3],[4,5,6],[7,8,9]]
print([j for k in lst for j in k ])   # for 循环，外层在第一个。

# 将 aaabbcccd 这种形式的字符串压缩成a3b2c3d1这种形式
