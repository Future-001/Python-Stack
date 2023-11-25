# 看代码写结果
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def __call__(self, *args, **kwargs):
        print(self.num)
class RoleConfig(StarkConfig):
    def __call__(self, *args, **kwargs):
        print(self.num)
v1 = StarkConfig(1)
v2 = RoleConfig(11)
v1()    # 地址加括号，给我看懵了
v2()  # 可能是这个__call__ 有用，输出就是 1 11



print()
# 看代码写结果
# class StarkConfig(object):
#     def __init__(self, num):
#         self.num = num
#     def run(self):
#         self()
#     def __call__(self, *args, **kwargs):
#         print(self.num)
# class RoleConfig(StarkConfig):
#     def __call__(self, *args, **kwargs):
#         print(345)
#     def __getitem__(self, item):
#         return self.num[item]
# v1 = RoleConfig('alex')
# v2 = StarkConfig("wupeiqi")
# print(v1[1.txt])
# print(v2[2])

# 补全代码
# class Context:
#     pass
# with Context() as ctx:
#     ctx.do_something()


# 补全代码
# class BaseAuthentication(object):
#     """
#     All authentication classes should extend BaseAuthentication.
#     """
#
#     def authenticate(self, request):
#         """
#         Authenticate the request and return a two-tuple of (user, token).
#         """
#         raise NotImplementedError(".authenticate() must be overridden.")
#
#
# class Foo(BaseAuthentication):
#     def authenticate(self, request):
#         pass
#
#
# obj = Foo()
# obj.authenticate()
