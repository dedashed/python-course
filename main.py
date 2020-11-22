import math

oldnum = "39"

n1 = oldnum[0]
n2 = oldnum[1] 

print(type(int(n1)))

newnum = math.ceil(int(n1) / int(n2))

print(newnum)
print(type(newnum))

