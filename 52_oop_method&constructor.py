class Demo:
    b=10
    def __init__(a):
        print("welcome buddy")  #--->counstructor
    def value(a):
        a.c=a.b*a.b
        print(a.c)

    def value1(self,e,f):
        print(e+f)
        print(self)

obj=Demo()
obj.value()
obj.value1(10,14)
        

#or

class Demo:
    b=10
    def value(a):
        a.c=a.b*a.b
        print(a.c)

    def value1(a,b):
        print(a+b)

obj=Demo
obj().value()
Demo.value1(10,14)
        