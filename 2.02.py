a=int(input("Enter 1st value:"))
b=int(input("Enter 2nd value:"))
c=int(input("Enter 3rd value:"))
if a>b and a>c and b>c:
    print(a,"is largest")
    print(c,"is smallest")
elif a>b and a>c and b<c:
    print(a,"is largest")
    print(b,"is smallest")
elif b>c and a>c:
    print(b,"is largest")
    print(c,"is smallest")
elif b>c and a<c:
    print(b,"is largest")
    print(a,"is smallest")
elif c>a and c>b and a>b:
    print(c,"is largest")
    print(b,"is smallest")
else:
    print(c,"is largest")
    print(a,"is smallest")
