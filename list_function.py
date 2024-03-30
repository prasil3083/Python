#1.for removinf element
# for delet
"""del
pop()
remove()
clear()"""

# del function
"""a=[10,20,30]
del a[1]
print(a)"""
#output:[10, 30]

#pop() function
"""a=[10,20,30]

print(a.pop(2))
print(a)"""
#output:30
#       [10, 20]

#remove function
"""a=[10,20,30]
a.remove(10)
print(a)"""

#output:[20, 30]

#clear function

"""a=[10,20,30]
a.clear()
print(a)"""

#output:[]

#2:for updating element

"""a=[10,20,30,40,50]
a[2]=3083
print(a)"""

#output:[10, 20, 3083, 40, 50]

"""insert()
   append()
   extends()"""

#insert method

"""a=[10,20,30,40,50]
a.insert(0,123)
print(a)"""

#output:[123, 10, 20, 30, 40, 50]

#append function

"""a=[10,20,30,40,50]
a.append(120)
print(a)"""
#output:[10, 20, 30, 40, 50, 120]

"""a=[10,20,30,40,50]
b=[60,70,80,90,100]
a.append(b)
print(a)"""
#output:[10, 20, 30, 40, 50, [60, 70, 80, 90, 100]]

#extend function

"""a=[10,20,30,40,50]
b=[60,70,80,90,100]
a.extend(b)
print(a)"""

#output:[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

"""
   count()
   max()
   min()
   sort()
   revers()
   index()"""

"""a=[10,20,30,40,50,60,70,80,30]
b=a.count(30)
print(b)"""
#output:2

"""a=[10,20,30,40,50,60,70,80,90]
b=max(a)
print(b)"""
#output:90

"""a=["hello","world"]
b=max(a)
print(b)"""
#output:world

a=[10,20,30,40,50,60,70,80,90]
