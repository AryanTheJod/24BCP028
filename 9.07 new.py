def ispalindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

print(ispalindrome(str(input("Enter string which you wanna check for palindrome cond :")))) 
