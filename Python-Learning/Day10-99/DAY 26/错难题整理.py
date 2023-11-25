# 看代码写结果
class UserInfo(object):
    pass
class Department(object):
    pass
class StarkConfig(object):
    def __init__(self, num):
        self.num = num
    def changelist(self, request):
        print(self.num, request)
    def run(self):
        self.changelist(999)
class RoleConfig(StarkConfig):
    def changelist(self, request):
        print(666, self.num)
class AdminSite(object):
    def __init__(self):
        self._registry = {}
    def register(self, k, v):
        self._registry[k] = v(k)
site = AdminSite()
site.register(UserInfo, StarkConfig)
site.register(Department, StarkConfig)
print(len(site._registry))   # 2
for k, row in site._registry.items():
    row.run()  # 会出错了，因为 num 没有初始化  ======>  没有初始化，稍等，这里存的是 字典的键类型？？？？
# <class '__main__.UserInfo'> 999
# <class '__main__.Department'> 999