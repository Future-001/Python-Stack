def get():
    print("我在哪一个包里面",__name__)

print("in api.py")

# 绝对导入  from glance.api import policy