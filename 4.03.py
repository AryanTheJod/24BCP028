def alphanum():
    a = str(input("Enter a string: "))
    b = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    c = 0
    for char in b:
        c = c + a.count(char)
    d = "0123456789"
    e = 0
    for inte in d:
        e = e + a.count(inte)
    print("There are" , c ,"alphabets and", e , "numbers in the string.")

alphanum()
