name='mette'
print('没有 __name__ 判断，执行全部')
def read():
    print(f'我的名字是 {name}')
def change():
    global name
    print(name)
    name='KEVIN METTE'
    print(f"我现在改名了，我叫  {name}")