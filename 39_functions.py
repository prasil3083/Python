#defining function
"""def name():
    {
    print("prasil")
}"""

#calling function
"""name()"""

#defining funtion with arguments
"""def sumdata(a,b):
    {
        print(a+b)
    }"""

"""sumdata(10, 20)"""

#or

"""a=int(input("enter the vaue of a:"))
b=int(input("enter the vaue of b:"))
sumdata(a,b)"""

#set default value(farenheit to celsius)
"""def sumdata(a,b=5/9):
    {
        print((a-32)*b)
    }

a=int(input("enter the celsius of a:"))
sumdata(a)"""

#use return in function
def sumdata(a,b):
    c=a+b
    return c
a=int(input("enter the vaue of a:"))
b=int(input("enter the vaue of b:"))

s=sumdata(a, b)
print(s)
