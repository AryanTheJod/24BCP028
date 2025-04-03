f = open("C:\\Users\\24BCP028\\Desktop\\Marks 2.csv","a+")
rlno = input("Enter roll no. [Enter to end.] : ")
while rlno:
    nm = input("Enter name :")
    cp2,maths2,chemistry = input("Enter Marks of CP2, Maths2 and Chemistry :").split()
    f.write(rlno+","+nm+","+cp2+","+maths2+","+chemistry+"\n")
    rlno = input("Enter roll no. : [Enter to end.]")
f.close()


