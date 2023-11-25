# 要让函数在调用时不执行  这样更简洁一点，就是直接先封装成为一个函数就可以了，然后用 __name__
def main():
    # 自定义一个模块玩一玩
    print('hello world')

    def y():
        for i in range(20):
            yield print(f'这是第{i}个包子')

    ret = y()
    for j in range(4):
        next(ret)

    print('老板，还有包子吗？')
    t = ret.__next__()  # 注意 ： 他的返回值位空
    print(t)
    print(ret.__next__())

    print(__name__)

age1=44
age2=66
age='我就不让用'
__all__=['age1','age2']

if __name__=='__main__':
    main()
