import random

a=random.randrange(1, 10)

while True :
    b=int(input("enter your guess:"))

    if b==a :
        print("\nyour right")
        break

    elif b>=a :
        print("\nguess lower no")
        continue

    elif b<=a :
        print("\nguess higher no")
        continue

    else :
        print("\ninvalid input")
        continue
