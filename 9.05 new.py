def ispangram(a):
    if set("abcdefghijklmnopqrstuvwxyz") <= set(a.lower()):
        print("'",a,"'"," is a pangram")
    else:
        print("'",a,"'"," is not a pangram")
print(ispangram("The quick brown fox jumps over the lazy dog"))
print(ispangram("Crazy Fredrick bought many very exquisite opal jewels"))
print(ispangram(input("Write a string for whick you want to check if it's pangram: ")))
    
    
