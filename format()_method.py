#format Method
"""b="enter yor name {},and your age is {}"
n="prasil"
a=18
print(b.format(n,a))
"""
#output:"enter yor name prasil,and your age is 18"

"""b="your name is {1},and your age is {0}"
n="prasil"
a=18
print(b.format(a,n))"""

#output:your name is prasil,and your age is 18

"""name=input("name:")
age=int(input("age:"))
b="your name is {},and your age is {}"
print(b.format(name,age))
"""
#output:your name is prasil,and your age is 19
"""
name=input("name:")
age=int(input("age:"))
b="your age is {1},and your name is {0}"
print(b.format(name,age))
"""
#output:your age is 19,and your name is prasil
