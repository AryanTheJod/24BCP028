def divby10(a):
    return True if a%10 == 0 else False

lst1= ['A','a','P','q','4','7','+','r','E','Z']
f1= filter(str.isalpha,(lst1))
print(list(f1))

lst2=[10,20,25,29,50]
f2=filter(divby10,lst2)
print(list(f2))
