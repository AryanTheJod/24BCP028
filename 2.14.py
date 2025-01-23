x1 = int(input("Enter marks of first subject:"))
x2 = int(input("Enter marks of secpnd subject:"))
x3 = int(input("Enter marks of third subject:"))
t = x1+x2+x3
avg = t/3
print("For first grade")
if x1 <= 39:
    print("Fail")
elif 40 <= x1 <= 44:
    print("P")
elif 45 <= x1 <= 49:
    print("C")
elif 50 <= x1 <= 54:
    print("B")
elif 55 <= x1 <= 59:
    print("B+")
elif 60 <= x1 <= 69:
    print("A")
elif 70 <= x1 <= 79:
    print("A+")
elif 80 <= x1 <= 100:
    print("O")
else:
    print("Not applicable.")

print("For second grade")
if x2 <= 39:
    print("Fail")
elif 40 <= x2 <= 44:
    print("P")
elif 45 <= x2 <= 49:
    print("C")
elif 50 <= x2 <= 54:
    print("B")
elif 55 <= x2 <= 59:
    print("B+")
elif 60 <= x2 <= 69:
    print("A")
elif 70 <= x2 <= 79:
    print("A+")
elif 80 <= x2 <= 100:
    print("O")
else:
    print("Not applicable.")

print("For third grade")
if x3 <= 39:
    print("Fail")
elif 40 <= x3 <= 44:
    print("P")
elif 45 <= x3 <= 49:
    print("C")
elif 50 <= x3 <= 54:
    print("B")
elif 55 <= x3 <= 59:
    print("B+")
elif 60 <= x3 <= 69:
    print("A")
elif 70 <= x3 <= 79:
    print("A+")
elif 80 <= x3 <= 100:
    print("O")
else:
    print("Not applicable.")

