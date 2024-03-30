# a="hiii i {1} am Deval {0} and "
# b="i am {} years old"
# print(a.format(85,11)+b.format(25))



# name=input("name:")
# age=input("age:")
# a="hii i am {n} and i am {a} years old"

# print(a.format(a=age,n=name))



a="hii i am {a:^10} and i am {b} years old"
print(a.format(a='Deval',b=20))




v="hii i am {a:<10} and i am {b} years old"
print(v.format(a='Deval',b=20))