import json

#for writiong json file
l=[10,20,30,40,40]
data=json.dumps(l)
a=open("50_jsondummyfile.json","w")
a.write(data)
a.close()


# for reading json file
a=open("50_jsondummyfile.json","r")

b=a.read()
data=json.loads(b)

print(data)

