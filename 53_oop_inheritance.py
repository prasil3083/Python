#simple inheritance

"""class A:
    def showA(a):
        print("prasil")

class B(A):
    def showB(b):
        print("gajjar")

obj=B()

obj.showA()
obj.showB()"""

#multilevel inheritance

"""class A:
    def showA(a):
        print("prasil")

class B(A):
    def showB(b):
        print("gajjar")

class C(B):
    def showC(c):
        print("3083")

obj=C()

obj.showA()
obj.showB()
obj.showC()"""

#multiple
class A:
    def showA(a):
        print("prasil")

class B:
    def showB(b):
        print("gajjar")

class C(A,B):
    def showC(c):
        print("3083")

obj=C()

obj.showA()
obj.showB()
obj.showC()