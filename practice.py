#for remove specific element using del function
"""a=[b for b in range(1,101)]
x=int(input("enter the number you want to remove:\n"))
y=0
for num in a:
    if num==x:
        break
    else:
        y=y+1

del a[y]
print(a)"""

#delete method
"""a=[10,20,30,40,50,60,70,80,90]
del a[8]
print(a)"""

#remove method
"""a=[10,20,30,40,50,60,70,80,90]
a.remove(30)
print(a)"""

#pop method
"""a=[10,20,30,40,50,60,70,80,90]
print(a.pop(3))
print(a)"""

#clear method
"""a=[10,20,30,40,50,60,70,80,90]
a.clear()
print(a)"""

#update methods
"""a=[10,20,30,40,50,60,70,80,90]
a[2]=125
print(a)"""

#insert method
"""a=[10,20,30,40,50,60,70,80,90]
a.insert(2,234)
print(a)"""

#append method
"""a=[10,20,30,40,50,60,70,80,90]
a.append(120)
print(a)"""

#SPLIT function
"""p=input("enter the sentence")
p=p.split();
print(p)"""

#Stack 

"""p=[]
while True:
    c=int(input('''
1.Push ele
2.Delete ele
3.Show last ele
4.Display whole list
5.Exit
:'''))
    
    if c==1:
        o=int(input("enter the element you ant to insert:"))
        p.append(o)
        print(p)
    
    elif c==2:
        if len(p)==0:
            print("list is empty:")
        else:
            p.pop()
    
    elif c==3:
        print("the last element is ",p[-1]," ")

    elif c==4:
        print(p)

    elif c==5:
        break

print("bye bye")"""


#Queue

p=[]
while True:
    c=int(input('''
1.Push ele
2.Delete frist ele
3.Show frist ele
4.Display whole list
5.Exit
:'''))
    
    if c==1:
        o=int(input("enter the element you ant to insert:"))
        p.append(o)
        print(p)
    
    elif c==2:
        if len(p)==0:
            print("list is empty:")
        else:
            p.pop(0)
    
    elif c==3:
        print("the frist element is ",p[0]," ")

    elif c==4:
        print(p)

    elif c==5:
        break

print("bye bye")