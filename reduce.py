from functools import reduce
def sum(a,b):
    return a+b
lst=[1,2,3,4,5]
s= reduce(sum,[z for z in range(1,5)]) # short hand ke badle lst bhi chalega
print(s)
