course={
    'php':{'duration':'2months','fees':15000},

    'python':{'duration':'5months','fees':1},

    'java':{'duration':'11months','fees':5000}
}
# print(course)
# print(course["python"]['fees'])

course['python']['fees']=1111111

for x,y in course.items():
    print(x,y['duration'],y['fees'])
