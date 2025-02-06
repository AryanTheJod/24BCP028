def fact():
    n = int(input("Enter number whose fact. u want : "))
    fact = i = 1
    while i <= n:
        fact = fact*i
        i+=1
    print("The fact of ",n , " is ", fact)

fact()
