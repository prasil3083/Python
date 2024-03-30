import pickle

file=open("example_of_pickel.txt","rb")

l=pickle.load(file)

while True:
    a=int(input('''what you want to know
1.name
2.age
3.status
'''))

    if a==1:
        c=l.get('name')
        print("name:",c)
        break
        
    elif a==2:
        c=l.get('age')
        print("age:",c)
        break

    elif a==3:
        c=l.get('status')
        print("status:",c)
        break

    else:
        print("invalid input")