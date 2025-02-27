s=set()
while len(s)<5:
    s.add(input("Enter name : "))
print(s)
nm = input("Enter a name to modify: ")
if nm in s:
    newnm = input("Enter another name : ")
    s.remove(nm)
    s.add(newnm)
else:
    print(nm," is missing in ze values.")
print("removing 2 values : ")
print(s.pop()," is removed")
print(s.pop()," is removed")
print("Final set : ", s)
