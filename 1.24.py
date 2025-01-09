a=int(input("Enter first :"))
b=int(input("Enter second :"))
a,b=b,a
print("The swapped values are:\n a=",a,"\tb=",b)
print(id(a),id(b))
