x1 = int(input("Enter coord x1:"))
y1 = int(input("Enter coord y1:"))
x2 = int(input("Enter coord x2:"))
y2 = int(input("Enter coord y2:"))
x3 = int(input("Enter coord x3:"))
y3 = int(input("Enter coord y3:"))
if (x1*(y2-y3)+y1*(x3-x2)+(x2*y3)-(x3*y2))==0:
    print("The points lie on a line.")
else:
    print("The points do not lie on a line")
