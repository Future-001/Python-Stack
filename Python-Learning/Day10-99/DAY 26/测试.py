class Wechatpay:pass
class Alipay:pass

# 写一个自定义模块，里面有你自己实现的 mypickle  和 myjson,我只要给你传递一个参数 pickle 或者 json
# 接下来的内容就用 pickle 或者 json方式进行操作。

class Authentic:
    def __init__(self):pass
    def register(self):pass
    def login(self):pass
l = [('登录','login'),('注册','register')]    # 不用字典是因为python2中无序，保持通用性
# 循环这个列表
# 显示序号 用户要进行的操作
# 用户输入序号
# 你通过序号找到对应的 login 或者register
# 先实例化
# 调用对应的方法，完成登录或注册

# 运行程序，用户输入用户名，密码，性别
# 实例化对象，  不能用异常处理。
# 用户输入任意内容，如果输入的是属性名，打印属性值
# 如果输入的是方法名，调用方法
# 如果什么都不是，不做操作

