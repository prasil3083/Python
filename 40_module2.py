"""import module1 

while True:
    x=int(input('''
enter 1 for sum 
enter 2 for multiplication\n:'''))

    if x==1:
        a=int(input("enter the first value:"))
        b=int(input("\nenter the second value:"))
        print(module1.sum(a,b))

        break

    elif x==2:
        a=int(input("enter the first value:"))
        b=int(input("\nenter the second value:"))
        print(module1.mul(a,b))

        break

    else :
        print("envalid input")

        continue"""

"""import module1 as p

while True:
    x=int(input('''
enter 1 for sum 
enter 2 for multiplication\n:'''))

    if x==1:
        a=int(input("enter the first value:"))
        b=int(input("\nenter the second value:"))
        print(p.sum(a,b))

        break

    elif x==2:
        a=int(input("enter the first value:"))
        b=int(input("\nenter the second value:"))
        print(p.mul(a,b))

        break

    else :
        print("envalid input")

        continue"""

#only calling specific function
from module1 import sum

a=int(input("enter the first value:"))
b=int(input("\nenter the second value:"))
print(sum(a,b))

from module1 import *

a=int(input("enter the first value:"))
b=int(input("\nenter the second value:"))

print(sum(a,b))
print(mul(a,b))
