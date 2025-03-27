a=lambda a:a%10==0
n=int(input("Enter number of entries: "))
lst2=[]
for i in range(n):
    lst2.append(int(input("Enter entry: ")))

f2=filter(a,lst2)
print(list(f2))
