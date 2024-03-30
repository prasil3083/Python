class Area():
    def findarea(self,a=None,b=None):
        if a!=None and b!=None:
            print("area =",a*b)
        
        elif a!=None:
            print("area =",a*a)

        else:
            print("Invalid input")

p=Area()
p.findarea()
p.findarea(10)
p.findarea(10,20)

#OR

"""class Area():
    def findarea(a=None,b=None):
        if a!=None and b!=None:
            print("area =",a*b)
        
        elif a!=None:
            print("area =",a*a)

        else:
            print("Invalid input")

Area.findarea()
Area.findarea(10)
Area.findarea(10,15)"""

#overridding

class A1:
    def name(a):
        print("hello boss")

class A2(A1):
    def name(a):
        print("hello prasil")

obj=A2()
obj.name()
