#overloading
l=[10,20,30,40,50]
print(len(l))

s="prasil"
print((len(s)))

class Name():
    def A(A,name=''):
        print("hii "+name)

obj=Name()
obj.A()
obj.A('prasil')

#over ridding
class A1:
    def name(a):
        print("hello boss")

class A2(A1):
    def name(a):
        print("hello prasil")

obj=A2()
obj.name()
