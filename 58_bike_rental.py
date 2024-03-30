tb=100

while True:
    r=int(input('''
1.display available stocks.
2.request a bike for rent.
3.exit.'''))
    if r==1:
        print("\navailable stocks :",tb)
        continue
    elif r==2:
        q=int(input("\n how many bikes you want to rent:"))
        if q>tb:
            print("\nsorry currently we have only ",tb,"no of bikes")
            continue
        elif q<tb:
            tb=tb-q
            print("\nyour rent will we :",q*10,"Rs")
            continue
        else:
            print("\nenter valid no")
    elif r==3:
        break
    else:
        print("enter valid choice")
    