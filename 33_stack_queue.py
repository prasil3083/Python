# stack have LIFO structure
# a=[]

# while True:
#     c=int(input('''    1.insert element
#     2.delete element
#     3.peek element
#     4.display stack
#     5.exit'''))

#     if c==1:
#         n=input("enter the value:")
#         a.append(n)
#         print(a)
#     elif c==2:
#         l=len(a)
#         if l==0:
#             print("stack is empty")
#         else:
#             print(a.pop())
#             print(a)
#     elif c==3:
#         l=len(a)
#         if l==0:
#             print("stack is empty")
#         else:
#             print("the last element is",a[-1])
#     elif c==4:
#         print(a)
#     elif c==5:
#         break
#     else:
#         print("invalid input")
#         continue


# FIFO structure in Queue

a=[]

while True:
    c=int(input('''    1.insert element
    2.delete element
    3.peek element
    4.display stack
    5.exit'''))

    if c==1:
        n=input("enter the value:")
        a.append(n)
        print(a)
    elif c==2:
        l=len(a)
        if l==0:
            print("stack is empty")
        else:
            print(a[0])
            del a[0]
            print(a)
    elif c==3:
        l=len(a)
        if l==0:
            print("stack is empty")
        else:
            print("the last element is",a[-1])
    elif c==4:
        print(a)
    elif c==5:
        break
    else:
        print("invalid input")
        continue


        