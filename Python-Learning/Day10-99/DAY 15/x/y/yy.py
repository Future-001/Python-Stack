"""z--->x
做几个测试吧，相互引用，主要是练习 __all__
练习相对引用
"""

def main():
    for i in range(5):
        print(f'y{i}={i+1}')

age =888
age1 = 666

# __all__=['age']
if __name__ == '__main__':
    main()