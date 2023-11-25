# 练习
li=[1,2,'Taibai',[1,'alex',3]]
# 1.txt taibai 大写放回原处
# 2  [1.txt,'alex',3] 中增加一个元素，小男孩教育
# 3  修改 alex 为  alexsb
li[2]=li[2].upper()
print(li)
li[3].insert(1,'小男孩教育')
print(li)
print(li[3][2]+'sb')
print(li)
li[3][2]=li[3][2]+'sb'
print(li)


