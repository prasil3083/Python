import json

a='{"name":"prasil","status":"student","subject":["python","java"]}'

c='["prasil","suthar"]'

b=json.loads(a)
d=json.loads(c)

print(b)
print(type(b))

print(d)
print(type(d))

for x,y in b.items():
    print(x,y)