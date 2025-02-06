def armstrong():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")

armstrong()

def auto():
    num = int(input("Enter a number you want to check: \n"))
    num_of_digits = len(str(num))
    square = num**2
    last_digits = square%pow(10,num_of_digits)
    if last_digits == num:
        print("Yes, {} is an automorphic number".format(num))
    else:
        print("No, {} is not an automorphic number".format(num))
auto()

def pal():
    n=int(input("Enter number:"))
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")

pal()

