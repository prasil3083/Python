"""a=[10,20,30,40,50,60,120]
for n in a:
    print(n)"""
#out put:10
#        20
#        30
#        40
#        50
#        60
#        120
   
"""a=[10,20,30,40,50,60,120]
b=len(a)
for n in range(b):
    print(a[n])"""
#out put:10
#        20
#        30
#        40
#        50
#        60
#        120

"""a=[10,20,30,40,50,60,120]
b=len(a)
for n in range(b):
    if(n%2!=0):
        print(a[n])
    else:
        continue"""
#out put:20
#        40
#        60

#list iteration in revers
a=[10,20,30,40,50,60,120]
b=len(a)
for n in range(b-1,-1,-1):
    print(a[n])

#output:120
#       60
#       50
#       40
#       30
#       20
#       10