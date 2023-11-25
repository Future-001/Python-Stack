class Player(Car,Weapon):
    def __init__(self,name,sex,age,ad,hp):
        self.name=name
        self.sex=sex
        self.age=age
        self.ad=ad
        self.hp=hp
        self.car=Car()
        self.weapon=Weapon()

class Weapon():
    def 普攻(self,person2):
        person2.hp = person2.hp - self.ad
        print('%s赤手空拳打了%s %s滴血，%s还剩%s血。' % (
            self.name, person2.name, self.ad,
            person2.name, person2.hp))
    def pan(self,person2):
        self.pan_ad=20
        person2.hp = person2.hp - self.pan_ad
        print('%s使用%s打了%s %s滴血，%s还剩%s血。'%(
              self.name,'平底锅',person2.name,self.pan_ad,
              person2.name,person2.hp))
    def ax(self ,person2):
        self.ax_ad=50
        person2.hp = person2.hp - self.pan_ad
        print('%s使用%s砍伤了%s %s滴血，%s还剩%s血。'%(
              self.name, '斧头', person2.name, self.ax_ad,
              person2.name, person2.hp))
    def rod(self,person2):
        self.rod_ad=65
        person2.hp = person2.hp - self.pan_ad
        print('%s使用%s打了%s %s滴血，%s还剩%s血。'
                %(self.name, '双截棍', person2.name, self.rod_ad,
                person2.name, person2.hp))
class Car():
    def bike(self):
        self.bike_speed=60
        print('%s骑着%s开着%s迈的车行驶在赛道上。' % (self.name, '自行车', self.bike_speed))
    def yamh(self):
        self.yamh_speed=80
        print('%s骑着%s开着%s迈的车行驶在赛道上。'% (self.name, 'yamh', self.yamh_speed))
    def beemar(self):
        self.beemar_speed=120
        print('%s骑着%s开着%s迈的车行驶在赛道上。' %(self.name, '宝马', self.beemar_speed))


苍井井=Player('苍井井','女',18,20,200)
东尼木木=Player('东尼木木','男',20,30,150)
波多多=Player('波多多','女',19,50,80)
苍井井.car=Car()
苍井井.car.bike()
# 苍井井.weapon.普攻(波多多)



# #完成下列需求（利用武器打人掉的血量为武器的ad + 人的ad）：
# #1.txt）苍井井骑着小踏板开着60迈的车行驶在赛道上。
# car=Car()
# # weapon=Weapon()
# 苍井井.Car=car
# 苍井井.Car.bike(苍井井)
# #（2）东尼木木骑着宝马开着120迈的车行驶在赛道上。
# 东尼木木.Car=car
# 东尼木木.Car.beemar(东尼木木)
# #（3）波多多骑着雅马哈开着80迈的车行驶在赛道上。
# 波多多.Car=car
# 波多多.Car.yamh(波多多)
# #（4）苍井井赤手空拳打了波多多20滴血，波多多还剩xx血。
# weapon=Weapon()
# 苍井井.Weapon=weapon
# 苍井井.Weapon.普攻(苍井井,波多多)
# #（5）东尼木木赤手空拳打了波多多30滴血，波多多还剩xx血。
# 东尼木木.Weapon=weapon
# 东尼木木.Weapon.普攻(东尼木木,波多多)
# #（6）波多多利用平底锅打了苍井井一平底锅，苍井井还剩xx血。
# 波多多.Weapon=weapon
# 波多多.Weapon.pan(波多多,苍井井)
# #（7）波多多利用斧子打了东尼木木一斧子，东尼木木还剩xx血。
# 波多多.Weapon.ax(波多多,东尼木木)
#
# #（8）苍井井骑着宝马打了骑着小踏板的东尼木木一双节棍，东尼木木哭了，还剩xx血。（选做）
# 苍井井.Car.beemar(苍井井)
#
# # （9）波多多骑着小踏板打了骑着雅马哈的东尼木木一斧子，东尼木木哭了，还剩xx血。（选做）