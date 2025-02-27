import random
numbers=set()
less=0
for i in range(100):
    randomno=random.randint(15,45)
    if randomno<30:
        less+=1
    numbers.add(randomno)
    if len(numbers)==10:
        break
print("The set is ", numbers)
print("The number less than 30 are :", less)
s1={x for x in numbers if x > 35}
numbers=numbers-s1
print(numbers)
