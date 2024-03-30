import datetime

#for printing current date n time

d=datetime.datetime.now()
print(d)

# for creating date objects
d=datetime.datetime(2023,2,14)
print(d)

print(datetime.datetime(2022,3,5))

d=datetime.datetime.now()
a=d.strftime("%b")
b=d.strftime("%B")
c=d.strftime("%m")
e=d.strftime("%y")
f=d.strftime("%Y")
g=d.strftime("%H")
h=d.strftime("%I")
j=d.strftime("%M")
i=d.strftime("%p")
print(d)
print("\n",a)
print("\n",b)
print("\n",c)
print("\n",e)
print("\n",f)
print("\n",g)
print("\n",h)
print("\n",i)
print("\n",j)