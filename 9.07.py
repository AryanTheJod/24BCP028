def ispalindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

print(ispalindrome("A man, a plan, a canal, Panama!")) 
