import random
numbers=set()
while len(numbers5)<10:
    c=random.randint(15,45)
    numbers.add(c)
    less=0
    for i in numbers:
        if i < 30:
            less+=1
        s1={x for x in numbers if x > 35}
    numbers-=s1
print("The set is ", numbers)
print("The number less than 30 are :", less)
numbers=numbers-s1
print(numbers)
