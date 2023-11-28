# 1、匹配一篇英文文章的标题 类似 The Voice Of China
import re
ret = re.findall('(?:[A-Z]\w* ?)+','The Voice Of China')
print(ret)
ret = re.search('([A-Z]\w* ?)+','The Voice Of China Is A Good')
print(ret.group(0))

# 2、匹配一个网址
# # 类似 https://www.baidu.com http://www.cnblogs.com
ret = re.findall('http.+?com','https://www.baidu.com ;sgasg,http://www.cnblogs.com')
print(ret)

# 5、从lianjia.html中匹配出标题，户型和面积，结果如下：
# [('金台路交通部部委楼南北大三居带客厅 单位自持物业', '3室1厅', '91.22平米'), ('西山枫林 高楼层南向两居 户型方正 采光好', '2室1厅', '94.14平米')]
#
# 6、1.txt-2*((60-30+(-40/5)(9-25/3+7/399/42998+10568/14))-(-43)/(16-3*2))
# 从上面算式中匹配出最内层小括号以及小括号内的表达式
#
# 7、从类似9-25/3+7/399/42998+10568/14的表达式中匹配出乘法或除法
ret = re.findall('-?\d+(?:\.\d+)?(?:[*/]\d+(?:\.\d+)?)+','9-25/3+7/399/42998+10568/14')
print(ret)

# 8、通读博客，完成三级菜单
# http://www.cnblogs.com/Eva-J/articles/7205734.html
menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
def opt(menu: object) -> object:
   flag = True
   while flag:
       for i in menu:
           print(i)
       choice = input('请选择：')
       if choice.upper()=='Q':
           return False
       elif choice.upper()=='B':
           return True
       else:
           if choice in menu.keys():
               if menu[choice]== {}:
                    print('您已到达最底层菜单')
               else:
                    flag = opt(menu[choice])
                    if not flag:return
           else:
               print('输入错误，请重新输入')
opt(menu)


# 9、大作业：计算器
# 1.txt)如何匹配最内层括号内的表达式
# 2)如何匹配乘除法
# 3)考虑整数和小数
# 4)写函数，计算‘23’ ‘10/5’
# 5)引用4)中写好的函数，完成'23/4'计算