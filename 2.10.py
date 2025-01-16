l=int(input("Enter length:"))
b=int(input("Enter breadth:"))
a=l*b
p=2*(l+b)
if a>p:
    print("Area is greater than perimeter")
elif a<p:
    print("Perimeter is greater than area")
else:
    print("Area and perimeter are equal")
