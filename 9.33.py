import random
numbers=set()
while len(numbers)<10:
    c=random.randint(-15,15)
    numbers.add(c)

lst1=[ele**2 for ele in numbers]
print(lst1)
