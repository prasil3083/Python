#class and object

"""n=Demo()
m=Demo()               #--->you can make multiple objects of same class

print(n.a)
print(m.b)
"""


def value() :
    x=int(input("\nenter the value of a:"))
    y=int(input("\nenter the value of b:"))

    return x, y

class Demo:
    a="prasil"
    b=3083

    def sum(a,b):
        print(a+b)

    def sub(a,b):
        print(a-b)

    def mul(a,b):
        print(a*b)

    def div(a,b):
        print(a/b)

while True:
    c=int(input('''
1.sum
2.sub
3.mul
4.div:'''))

    if c==1:
        a,b=value()
        Demo.sum(a,b);

    elif c==2:
        a,b=value()
        Demo.sub(a,b);

    elif c==3:
        a,b=value()
        Demo.mul(a, b);

    elif c==4:
        a,b=value()
        Demo.div(a,b);

    else:
        print("invalid input")
        continue

    d=input("\ndo you want to countinue y(yes)/n(no):")
    if d=='y':
        continue
    elif d=='n':
        break
    else:
        print("invalid input")