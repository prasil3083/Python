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
p=input("enter the sentence")
p=p.split();
print(p)