def compute(n):
    summ=0
    k=n
    l=0
    for i in range(k):
        if i==0:
            n=(k*(10**i))
        elif i!=0:
            n=n+(k*(10**i))
        summ+=n
    print(summ)
compute(n=int(input("Enter a value:")))

    
