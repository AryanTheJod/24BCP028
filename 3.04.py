x = str(input("Enter a string :"))
y = str(input("Enter a sub string:"))
if (y in x):
    x = x.replace(y,"")
    print(x)
else:
    print("The substring is not in the string")
