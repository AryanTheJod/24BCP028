def listoftuples(start, end):
    return [(x, x**2, x**3) for x in range(start, end+1)]

print(listoftuples(int(input("Starting number :")),int(input("ending number :"))))
