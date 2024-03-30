import json

#mostly used in API
"""p='{"name":"prasil","status":"student","subject":["python","java"]}'"""
a={'name':'prasil','fees':30000}

f=json.dumps(a)

print(f)
print(type(f))
print(type(a))