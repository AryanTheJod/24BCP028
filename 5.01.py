import random
lodd=[]
leven=[]
for i in range(5):
    x=random.randint(1,100)*2 + 1
    lodd.append(x)

for i in range(4):
    y=random.randint(1,100)*2
    leven.append(y)
lodd.pop(2)
lodd.insert(2, leven)
print("The replaced string is: ",lodd)
lst = []
for i in range(8):
    str(lst.append((lodd[i])))
    lst.split(",")
print(lst)

