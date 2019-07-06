#! /usr/bin/python
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("I see the name is" + self.name)


class Ex_student(Student):
    pass


p1 = Student("Shreeti", 12)
p1.myfunc()

p2 = Ex_student("Riyom", 13)
p2.myfunc()
