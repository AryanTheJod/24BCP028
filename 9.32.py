a=[1,2,3,4,5,6]
b=[6,5,4,3,2,1]
c=lambda d,e: d+e
f=list(map(c,a,b))
print(f)
