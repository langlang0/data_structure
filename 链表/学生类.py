class Student:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age

    def study(self):
        print("%s在学习"%(self.name))

    def rest(self):
        print("%s在休息"%(self.name))

a = Student('张三','男',23)
a.rest()