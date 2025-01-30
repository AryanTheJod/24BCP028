a = int(input("Enter a number: "))
def prime():
    factors = 0
    for b in range(2,a):
        if a%b == 0:
            factors = factors + 1
        else:
            factors = factors + 0
    if factors == 0:
        print(a, " is prime")
    else:
        print(a, " is not prime")

def perfect():
    b = 0
    for i in range(1,a):
        if a%i == 0:
            b+=i
    if b == a:
        print(a," is perfect. ")
    else:
        print(a, " is not perfect.")

def armstrong():
    
    
        
            
        
