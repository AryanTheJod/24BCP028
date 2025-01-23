x1 = int(input("Enter coord of centre x1:"))
y1 = int(input("Enter coord of centre y1:"))
x2 = int(input("Enter coord of point x2:"))
y2 = int(input("Enter coord of point y2:"))
r = int(input("Enter radius:"))
if(x2-x1)**2+(y2-y1)**2 == r**2:
    print("Point lies on Circle.")
elif(x2-x1)**2+(y2-y1)**2 > r**2:
    print("Point lies outside the Circle.")
else:
    print("Point lies inside.")
                
