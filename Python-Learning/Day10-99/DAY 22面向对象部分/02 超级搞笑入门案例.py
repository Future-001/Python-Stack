# 引入：  游戏公司
#                 人狗大战，  人： 血条，技能，武器，名字，性别，职业，等级
#                           狗： 名字，品种，血条，技能
#                 alex = {'name':'alex','sex':'不详','job':'搓澡工”,'level':0,'hp':250,'weapon':'搓澡巾'}
#                 '太白'=dict(name='太白',...............}
#             你怎么保证所有的玩家刚开始初始化的时候都拥有所有的属性？
#             每来一个新的玩家，我们都手动创建一个新的字典，然后向字典里添值，这样怎么样？
#             人和狗的技能怎么去写，不同的物种不同技能啊？

# def Person(name,sex,job,hp,ad,weapon,level = 0):     # 人模子  同样，还可以创建一个 狗模子
#     dic={'name':name,'sex':sex,'job':job,'hp':hp,'ad':ad,'weapon':weapon,"level":level}
#     return dic
#
# def Dog(name,kind,hp,ad):       # 狗模子
#     dic = dict(name=name,kind=kind,hp=hp,ad=ad)
#     return dic
# alex = Person('alex','不详','搓澡工',250,1,'搓澡巾')
# wusir = Person('wusir','male','法师',500,249,'打狗棒')
# 小白 = Dog('小白','柯基',1000,499)
# 小黑 = Dog('小黑','泰迪',500,199)
# # 总之，就是将他们写为一个通用化的技能，，但是会将参数 人，狗 的参数传错了呢？ 容错性很低。
#
# def 搓(person,dog):
#     dog['hp']-=person['ad']
#     print("%s 通过搓技能攻击了%s ,%s 掉了%s点血" %(person['name'],dog['name'],dog['name'],person['ad']))
#
# def 舔(dog,person):
#     person['hp']-=dog['ad']
#     print(" %s 通过舔攻击了%s ,%s 掉了%s点血" %(dog['name'],person['name'],person['name'],dog['ad']))
#
# 舔(wusir,小黑) # 哈哈哈哈，二者之间没有相关性，所以会出现错误的情况


def Person(name,sex,job,hp,ad,weapon,level = 0):     # 人模子  同样，还可以创建一个 狗模子
    def 搓(dog):
        dog['hp'] -= dic['ad']
        print("%s 通过搓技能攻击了%s ,%s 掉了%s点血" % (dic['name'], dog['name'], dog['name'], dic['ad']))
    dic={'name':name,'sex':sex,'job':job,'hp':hp,'ad':ad,'weapon':weapon,"level":level,'action':搓}
    return dic

def Dog(name,kind,hp,ad):       # 狗模子
    def 舔(person):
        person['hp'] -= dic['ad']  # 闭包了。
        print(" %s 通过舔攻击了%s ,%s 掉了%s点血" % (dic['name'], person['name'], person['name'],dic['ad']))
    dic = dict(name=name,kind=kind,hp=hp,ad=ad,action=舔)
    return dic

alex = Person('alex','不详','搓澡工',250,1,'搓澡巾')
wusir = Person('wusir','male','法师',500,249,'打狗棒')
小白 = Dog('小白','柯基',1000,499)
小黑 = Dog('小黑','泰迪',500,199)

小白['action'](alex)
