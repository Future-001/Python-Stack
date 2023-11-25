class Car:
    def bike(self):
        bike_speed = 60
        print(f'{self.owner.name}骑着小踏板开着{bike_speed}迈的车行驶在赛道上.')

    def yamh(self):
        yamh_speed = 80
        print(f'{self.owner.name}骑着雅马哈开着{yamh_speed}迈的车行驶在赛道上.')

    def beemar(self):
        beemar_speed = 120
        print(f'{self.owner.name}骑着宝马开着{beemar_speed}迈的车行驶在赛道上.')

class Player:
    def __init__(self, name, sex, age, ad, hp):
        self.name = name
        self.sex = sex
        self.age = age
        self.ad = ad
        self.hp = hp
        self._weapon = Weapon()
        self._weapon.owner = self
        self._car = Car()
        self._car.owner = self  # 设置车辆的所有者为玩家自身

    @property
    def car(self):
        return self._car

    @property
    def weapon(self):
        return self._weapon

class Weapon:
    def 普攻(self, person2):
        person2.hp = person2.hp - person2.ad
        print(f'{self.owner.name}赤手空拳打了{person2.name} {person2.ad}滴血，{person2.name}还剩{person2.hp}血.')

    def pan(self, person2):
        pan_ad = 20
        person2.hp = person2.hp - pan_ad
        print(f'{self.owner.name}使用平底锅打了{person2.name} {pan_ad}滴血，{person2.name}还剩{person2.hp}血.')

# 创建玩家对象
苍井井 = Player('苍井井', '女', 18, 20, 200)
东尼木木 = Player('东尼木木', '男', 20, 30, 150)
波多多 = Player('波多多', '女', 19, 50, 80)

# 使用方法来实现功能
苍井井.car.bike()
东尼木木.car.beemar()
波多多.weapon.pan(苍井井)
