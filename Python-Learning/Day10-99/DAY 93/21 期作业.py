# 对战角色数据
#
# Player:
# {
#     UserName:"Player1",
#     ATC:20,
#     DEF:20,
#     LIFE:300,
#     Equip:[]
#     Package:[
#         {name:"大砍刀",atc:20,def:-5,life:0},
#         {name:"黄金甲",atc:-5,def:20,life:200},
#         {name:"小红药",atc:5,def:0,life:100},
#     ]
# }
# 使用 Python + MongoDB 来实现
#
# 1.txt.角色装备道具 ATC DEF LIFE 相应提高
#
# 2.Package中的道具移动到 Equip 中
#
# 3.创建两个角色,之间互相PK,将PK记录存储在对战Log
#
# 对战log:
#
# {
#     PlayList:["play1","play2"],
#     PK_list:[
#         {
#             atcplayer:"player1",
#             defplayer:"player2",
#             info:"play1 atc play2 ,play2 life -15"
#         },
#         {
#             atcplayer:"player2",
#             defplayer:"player1",
#             info:"play2 atc play1 ,play1 life -10"
#         }
#     ]
# }