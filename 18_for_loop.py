# there is three things inbuit in this one range function

# range(5)
    #  >start=0
    #  >condition<5 means end=4
    #  >increment=1

 # range(1,5)
    #  >start=1
    #  >condition<5 means end=4
    #  >increment=1

 # range(1,5,2)
    #  >start=1
    #  >condition<5 means end=4
    #  >increment=2


# example 1
for n in range(5):
    print(n)
print()


    # example 2
for n in range(1,6):
    print(n)
print()

# example 3
for n in range(-2,6,1):
    print(n)

print("another example with list")

# to print list by for loop
a=[111,2,3,4,5,6]

for b in range(-1,-7,-1):
    print(a[b])

