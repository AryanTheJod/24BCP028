def listoftuples(start, end):
    lst=[]
    for x in range(start, end+1):
        a=(x,x**2,x**3)
        lst.append(a)
    print(lst)
print(listoftuples(int(input("Starting number :")),int(input("ending number :"))))
