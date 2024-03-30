#getter and setter

class A:
    def __init__(a):
        a.name=""
    
    def getname(a):
        return a.name

    def setname(a,b):
        a.name=b

A1=A()
A1.setname("prasil")
a=A1.getname()
print(a)
print(A1.getname())
