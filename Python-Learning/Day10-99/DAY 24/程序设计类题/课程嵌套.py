# 编写类完成以下的嵌套关系
# """
# 角色：学校、课程、班级
# 要求：
# 	1. 创建北京、上海、深圳三所学校。
# 	2. 创建课程
# 		北京有三种课程：Linux、Python、Go
# 		上海有两种课程：Linux、Python
# 		深圳有一种课程：Python
# 	3. 创建班级(班级包含：班级名称、开班时间、结课时间、班级人数)
# 		北京Python开设：21期、22期
# 		北京Linux开设：2期、3期
# 		北京Go开设：1期、2期
# 		上海Python开设：1期、2期
# 		上海Linux开设：2期
# 		深圳Python开设：1期、2期
# """
class Course():
    course_1="Python"
    def __init__(self,course):
        self.course="Linux"

class Class_(school,Course):
    def cl(self,class_name,start_date,end_date,num):
class school(Course,Class):
    def sch(self,name):
        self.school_name=name
北京=school("北京")
上海=school("上海")
深圳=school("深圳")

