import pickle

#dump() for serialize
#load() for de-serialize

a={'name':'prasil',
'age':19 ,'status':'student'}
b=open("example_of_pickel.txt","wb")
pickle.dump(a, b)

b.close()

