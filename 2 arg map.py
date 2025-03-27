def fun(n1,n2):
    return n1*n2
lst1=[1,2,3,4,5,6,7]
lst2=[2,3,4,5,6,7,8]
b=list(map(fun,lst1,lst2))
print(b)
