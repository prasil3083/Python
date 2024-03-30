import random

while True:
    a=["rock","paper","scissor"]
    b=random.choice(a)

    c=int(input('''
1.rock
2.paper
3.scissor:'''))

    if c==1:
        c="rock"
    
    elif c==2:
        c="paper"

    elif c==3:
        c="scissor"

    if (b==c):
        print("\nit's a draw")
        print(b)
        print(c)
        continue

    elif(b=='rock' and c=='paper'):
        print("\nyou win")
        print(b)
        print(c)
        continue

    elif(b=='rock' and c=='scissor'):
        print("\nyou lose")
        print(b)
        print(c)
        continue

    elif(b=='paper' and c=='rock'):
        print("\n you lose")
        print(b)
        print(c)
        continue

    elif(b=='paper' and c=='scissor'):
        print("\n you win")
        print(b)
        print(c)
        continue

    elif(b=='scissor' and c=='paper'):
        print("\n you lose")
        print(b)
        print(c)
        continue

    elif(b=='scissor' and c=='rock'):
        print("\n you win")
        print(b)
        print(c)
        continue

    else :
        print("wrong5 input")