def ispalindrome(s):
    a=""
    for x in range(-1,-len(s)-1,-1):
        a=""+str(s(x))
    if a==s:
        print(s," is a palindrome.")
    else:
        print(s," is not a palindrome")
ispalindrome(str(input("Enter a string: ")))
    
